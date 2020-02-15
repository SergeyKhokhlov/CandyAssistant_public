# подключение библиотек
import pygame
import time
import random
import zipfile
import sqlite3
import sys
import os

pygame.init()
width, height = 841, 901
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-man")
all_sprites = pygame.sprite.Group()  # группа всех спрайтов
wall_group = pygame.sprite.Group()  # группа спрайтов стен
point_group = pygame.sprite.Group()  # группа спрайтов очков
candylevel_group = pygame.sprite.Group()
pygame.mouse.set_visible(False)  # Отключение видимости мыши
end_screen_enemy = pygame.sprite.Group()  # группа спрайтов врагов на конечном экране
particles = pygame.sprite.Group()  # группа спрайтов звезд на конечном экране
settings_group = pygame.sprite.Group()  # группа спрайтов на настройках
change_value = pygame.sprite.Group()  # группа спрайтов изменяемых элементов
fl_HESOYAM = False  # пасхалка
fl_GOD = False  # пасхалка
title_width = 30
gravity = 0.5  # переменная для изменения скорости звезд на выигрышном экране
settings_running = False  # переменная для начала настроек
generating_level = 0  # переменная закрытия некоторых блоков
title_height = 30
candycash_count = 0  # переменная для кол-ва очков
candylevel_count = 0
cell = 0  # выбранная ячейка в меню
coord_x = 0
attemp = 0  # кол-во попыток для врагов чтобы развернуться
coord_y = 0
fl_death = False  # переменная отвечающая за смерть и выгрыш героя
win_music = False  # переменная отвечающая за проигрыш музыки победы
screen_rect = (0, 0, width, height)
prev_pac_man = 'right'
stars = ['files/Pac-man/data/star.png', 'files/Pac-man/data/green_star.png',
         'files/Pac-man/data/Communist_star.png',
         'files/Pac-man/data/red_star.png']  # список изображений звёзд
rotate_pacman = False  # переменная отвечающая за поворот пакмена
change_coord_pacman_menu = False  # переменная отвечающая за изменения координат пакмена в меню
is_load_level = False
level = 'Лёгкий'  # уровень сложности
volume = 0.5  # громкость музыки
pygame.mixer.music.load('files/Pac-man/data/pacman_beginning.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(volume)
r, g, b = (random.randrange(50, 255), random.randrange(50, 255),
           random.randrange(50, 255))  # цвет
arr_color = [r, g, b]  # список цветов
ischangedatabase = True
pacmen_start_screen_sprites = pygame.sprite.Group()  # группа спрайтов начального героя
player_group = pygame.sprite.Group()  # группа спрайтов для пакмена в игре
start_screen_sprites = pygame.sprite.Group()  # группа начальных партиклов
enemy_start_screen_sprites = pygame.sprite.Group()  # группа спрайтов начального врага
left_enemy_group = pygame.sprite.Group()  # группа спрайтов врагов
levels = ['level', 'level2', 'level3', 'level4', 'level5']  # список уровней
levelload = random.choice(levels)  # рандомный уровень
levelload1 = levelload + '.2.0'  # уровень без очков
levelload2 = levelload + '.3.0'  # уровень закрывающий блоки
main_running = True  # переменная для запуска основного цикла приложения
menu_running = True  # переменная для запуска основного цикла меню
settings_running = True  # переменная для запуска основного цикла настроек
pause = False  # переменная паузы
game_running = True  # переменная для запуска основного цикла игры

z = zipfile.ZipFile('CandyBase.zip')
pasw = 'Q5du7cc4opEQ1189'.encode()
z.extractall(pwd=pasw)
z.extract("CandyBase.db", pwd='Q5du7cc4opEQ1189'.encode())


# функция выхода
def terminate():
    pygame.quit()
    sys.exit()


# создание частиц
def create_particles(position, count):
    numbers = range(-5, 6)  # список скоростей звезд
    for number in range(count):
        Particle(position, random.choice(numbers), random.choice(numbers))


# счетчик
def candycash_counter():
    global candycash_count, candylevel_count
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 25)
    text = font.render(str(str(candycash_count) + " " + str(candylevel_count)), 0, (255, 255, 255))
    text_x = 750  # положение
    text_y = 330  # положение
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)


# конечный экран
def end_screen(fl):
    global win_music, ischangedatabase
    # проверка на поражение или победу
    if fl:
        # проигрыш
        game_over_image = pygame.image.load(
            'files/Pac-man/data/game_over.png')  # Музыка при проигрыше
        screen.blit(game_over_image, (225, 325))
        end_screen_enemy.draw(screen)
        end_screen_enemy.update()
    else:
        # победа
        if not win_music:
            # Музыка при выигрыши
            music_win = 'files/Pac-man/data/sound_win.mp3'
            pygame.mixer.music.load(music_win)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(volume)
            win_music = True
        win_image = pygame.image.load('files/Pac-man/data/win.png')  # загрузка выигрышной картинки
        screen.blit(win_image, (275, 325))
        create_particles((random.randint(0, 800), 0), random.randint(0, 5))  # создание звезд
        particles.draw(screen)
        particles.update()
    if ischangedatabase:
        change_database()
        ischangedatabase = False


def change_database():
    global candylevel_count, candycash_count
    con = sqlite3.connect('CandyBase.db')
    cur = con.cursor()
    cur.execute('SELECT [CandyCash], [CandyLevel] FROM [resources] LIMIT 500')
    temp = cur.fetchall()
    candycash = 0
    level = 0
    for i in temp:
        candycash = int(i[0]) + candycash_count
        level = int(i[1]) + candylevel_count
    sql = "DELETE FROM resources"
    cur.execute(sql)
    info_database = [str(candycash), str(level)]
    cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
    con.commit()
    with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
        myzip.write('CandyBase.db')


# Частицы
class Particle(pygame.sprite.Sprite):
    global stars
    fire = []  # список всех звезд
    for scale in (range(30)):
        fire.append(pygame.transform.scale(pygame.image.load(random.choice(stars)),
                                           (scale, scale)))  # добавление в список звезду

    def __init__(self, pos, dx, dy):
        super().__init__(particles)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = gravity

    def update(self):
        # изменение положения звезд
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()  # удаление звезды при выходе за экран


# враги на последнем экране
class End_screen_enemies(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(end_screen_enemy)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        # изменение положения
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.x = (self.rect.x + 5) % width
        time.sleep(0.03)


# Класс пакмен
class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, speed_x=6, speed_y=0):
        # разворот спрайта пакмена
        for player in all_sprites:
            try:
                if player.can_kill:  # Если в группе всех спрайтов это пакмен
                    all_sprites.remove(player)  # удаляем
            except AttributeError:
                pass
        super().__init__(all_sprites, player_group)
        self.frames = []
        self.can_kill = True  # переменная позволяющая удалять пакмена для его разворота
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x * title_width, y * title_width)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.mask = pygame.mask.from_surface(self.image)
        self.prev_speed_x = self.speed_x
        self.prev_speed_y = self.speed_y

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self, x=0, y=0, direction=0):  # движение пакмена
        global wall_group, candylevel_group
        global coord_x, coord_y, candycash_count, candylevel_count
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        # проверка на выхождение за карту
        self.rect.x %= 828
        self.rect.y %= 898
        if x == 0 and y == 0:
            # движение
            self.rect.x += self.speed_x
            if pygame.sprite.spritecollideany(self, wall_group):
                if fl_HESOYAM is False:  # пасхалка
                    self.rect.x -= self.speed_x
                    self.cur_frame = 2
                if rotate_pacman:
                    self.cur_frame = 1
            self.rect.y += self.speed_y
            if pygame.sprite.spritecollideany(self, wall_group):
                if fl_HESOYAM is False:  # пасхалка
                    self.rect.y -= self.speed_y
                    self.cur_frame = 2
                if rotate_pacman:
                    self.cur_frame = 1
        else:
            self.speed_x = x
            self.speed_y = y
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            if pygame.sprite.spritecollideany(self, wall_group):
                if fl_HESOYAM is False:
                    self.rect.x -= self.speed_x
                    self.rect.x -= self.speed_x
                    self.rect.y -= self.speed_y
                    self.speed_y = self.prev_speed_y
                    self.speed_x = self.prev_speed_x
                    self.cur_frame = 2
                if rotate_pacman:
                    self.cur_frame = 1
                return
            else:
                self.prev_speed_x = self.speed_x
                self.prev_speed_y = self.speed_y
                return
        # сбор монет
        if pygame.sprite.spritecollide(self, point_group, True):
            candycash_count += 1
        if pygame.sprite.spritecollide(self, candylevel_group, True):
            candylevel_count += 1
        coord_x = self.rect.x
        coord_y = self.rect.y

    def update_image(self, sheet, rows, col):
        x, y = self.rect.x, self.rect.y
        self.cur_frame = 0
        self.frames = []
        self.rect = pygame.Rect(0, 0, sheet.get_width() // col, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(col):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
        self.rect = self.rect.move(x, y)

    def wall(self, x, y):  # функция для проверки столкновения пакмена со стенами при поворотах
        self.rect.x += x
        self.rect.y += y
        if pygame.sprite.spritecollideany(self, wall_group):
            self.rect.x -= x
            self.rect.y -= y
            return True
        self.rect.x -= x
        self.rect.y -= y
        return False


class Wall(pygame.sprite.Sprite):  # класс стен
    def __init__(self, x, y, color=(0, 0, 0)):
        super().__init__(wall_group)
        self.image = pygame.Surface((title_width - 6, title_height - 6))
        pygame.draw.rect(self.image, color,
                         (0, 0, title_width - 6, title_height - 6), 2)
        self.rect = self.image.get_rect().move(title_width * x,
                                               title_height * y)


class CandyCash(pygame.sprite.Sprite):  # класс очков
    def __init__(self, x, y):
        super().__init__(all_sprites, point_group)
        self.image = pygame.Surface((8, 8))
        pygame.draw.circle(self.image, (255, 255, 173), (4, 4), 5, 0)
        self.rect = self.image.get_rect().move(title_width * x + 5,
                                               title_height * y + 6)


class CandyLevel(pygame.sprite.Sprite):  # класс очков
    def __init__(self, x, y):
        super().__init__(all_sprites, candylevel_group)
        self.image = pygame.Surface((8, 8))
        pygame.draw.circle(self.image, (255, 0, 0), (4, 4), 5, 0)
        self.rect = self.image.get_rect().move(title_width * x + 5,
                                               title_height * y + 6)


# Класс который создаёт и управляет врагами
class Enemy(pygame.sprite.Sprite):
    def __init__(self, sheet, color, columns, rows, x, y):
        global level
        super().__init__(all_sprites, left_enemy_group)
        self.frames = []
        self.color_enemy = color
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x * title_width, y * title_width)
        self.speed_x = 6
        self.speed_y = 0
        self.speed_enemy = 6
        # Выбор скорости врага
        if level == "Сложный":
            self.speed_enemy = 10
        self.way_enemy = None
        self.start_enemy_motion = True  # переменная для начального хождения врагов
        self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):  # движение врагов по карте
        global attemp, fl_death, candycash_count, generating_level
        if self.start_enemy_motion and self.rect.x == 402:
            self.x_coord = self.rect.x
            self.y_coord = self.rect.y
            self.frames = []
            self.cut_sheet(pygame.image.load(self.color_enemy + '_up.png'), 2, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.rect.x = self.x_coord
            self.rect.y = self.y_coord
            self.rect.y -= 6
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y += 6
                self.start_enemy_motion = False
        elif self.start_enemy_motion and not pygame.sprite.spritecollideany(self, wall_group):
            if self.rect.x > 402:
                self.rect.x -= 6
            else:
                self.rect.x += 6
        elif not self.start_enemy_motion:
            if attemp < 40:
                self.way_enemy = random.choice(['up', 'left', 'right'])
                attemp += 1
            else:
                generating_level = 1
            # Если пакман движется вниз то выполнится это условие
            if self.way_enemy == 'down':
                self.x_coord = self.rect.x
                self.y_coord = self.rect.y
                self.frames = []
                self.cut_sheet(pygame.image.load(self.color_enemy + '_down.png'), 2, 1)
                self.cur_frame = 0
                self.image = self.frames[self.cur_frame]
                self.rect.x = self.x_coord
                self.rect.y = self.y_coord
                self.rect.y += self.speed_enemy
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.y -= self.speed_enemy
                    self.way_enemy = random.choice(['up', 'left', 'right'])

            # Если пакман движется вверх то выполнится это условие
            if self.way_enemy == 'up':
                self.x_coord = self.rect.x
                self.y_coord = self.rect.y
                self.frames = []
                self.cut_sheet(pygame.image.load(self.color_enemy + '_up.png'), 2, 1)
                self.cur_frame = 0
                self.image = self.frames[self.cur_frame]
                self.rect.x = self.x_coord
                self.rect.y = self.y_coord
                self.rect.y -= self.speed_enemy
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.y += self.speed_enemy
                    self.way_enemy = random.choice(['down', 'left', 'right'])
            # Если пакман движется влево то выполнится это условие
            if self.way_enemy == 'left':
                self.x_coord = self.rect.x
                self.y_coord = self.rect.y
                self.frames = []
                self.cut_sheet(pygame.image.load(self.color_enemy + '_left.png'), 2, 1)
                self.cur_frame = 0
                self.image = self.frames[self.cur_frame]
                self.rect.x = self.x_coord
                self.rect.y = self.y_coord
                self.rect.x -= self.speed_enemy
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.x += self.speed_enemy
                    self.way_enemy = random.choice(['down', 'up', 'right'])
            # Если пакман движется вправо то выполнится это условие
            if self.way_enemy == 'right':
                self.x_coord = self.rect.x
                self.y_coord = self.rect.y
                self.frames = []
                self.cut_sheet(pygame.image.load(self.color_enemy + '_right.png'), 2, 1)
                self.cur_frame = 0
                self.image = self.frames[self.cur_frame]
                self.rect.x = self.x_coord
                self.rect.y = self.y_coord
                self.rect.x += self.speed_enemy
                if pygame.sprite.spritecollideany(self, wall_group):
                    self.rect.x -= self.speed_enemy
                    self.way_enemy = random.choice(['down', 'up', 'left'])

        if pygame.sprite.spritecollideany(self, player_group):
            if fl_GOD is False:  # пасхалка
                global volume
                pygame.mixer.music.load('files/Pac-man/data/game_over.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(volume)
                fl_death = True
            else:
                candycash_count += 100
                self.kill()


def load_level(filename):  # загрузка уровня
    filename = 'files/Pac-man/data/' + filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]
    return level_map


def generate_level(level):  # генерация уровня в игре
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                CandyCash(x, y)
            if level[y][x] == "*":
                CandyLevel(x, y)
            if level[y][x] == '#':
                Wall(x, y, (r, g, b))
            if level[y][x] == '@':
                Player(pygame.image.load('files/Pac-man/data/Pac-man_right.png'), 3, 1, x, y)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '$':
                color_enemy = random.choice(['files/Pac-man/data/orange_enemy',
                                             'files/Pac-man/data/blue_enemy',
                                             'files/Pac-man/data/pink_enemy',
                                             'files/Pac-man/data/red_enemy'])
                Enemy(pygame.image.load(color_enemy + '_right.png').convert_alpha(), color_enemy,
                      2, 1, x, y)
            if level[y][x] == '%':
                color_enemy = random.choice(['files/Pac-man/data/orange_enemy',
                                             'files/Pac-man/data/blue_enemy',
                                             'files/Pac-man/data/pink_enemy',
                                             'files/Pac-man/data/red_enemy'])
                Enemy(pygame.image.load(color_enemy + '_left.png').convert_alpha(), color_enemy,
                      2, 1, x, y)


level = ['level.txt', 'level2.txt', 'level3.txt', 'level4.txt', 'level5.txt']
generate_level(load_level(random.choice(level)))

while game_running:  # цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if not pause:  # проверка на паузу
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # движение пакмена
                    for i in player_group:
                        if fl_HESOYAM or not i.wall(15, 0) and prev_pac_man != 'right':
                            player_group = pygame.sprite.Group()
                            Player(pygame.image.load(
                                'files/Pac-man/data/Pac-man_right.png').convert_alpha(),
                                   3, 1,
                                   coord_x / title_width, coord_y / title_height, 6, 0)
                            prev_pac_man = 'right'
                            rotate_pacman = False
                if event.key == pygame.K_DOWN:  # движение пакмена
                    for i in player_group:
                        if fl_HESOYAM or not i.wall(0, 15) and prev_pac_man != 'down':
                            player_group = pygame.sprite.Group()
                            Player(pygame.image.load(
                                'files/Pac-man/data/Pac-man_down.png').convert_alpha(),
                                   1, 3,
                                   coord_x / title_width, coord_y / title_height, 0, 6)
                            prev_pac_man = 'down'
                            rotate_pacman = False
                if event.key == pygame.K_LEFT:  # движение пакмена
                    for i in player_group:
                        if fl_HESOYAM or not i.wall(-15, 0) and prev_pac_man != 'left':
                            player_group = pygame.sprite.Group()
                            Player(pygame.image.load(
                                'files/Pac-man/data/Pac-man_left.png').convert_alpha(),
                                   3, 1,
                                   coord_x / title_width, coord_y / title_height, -6, 0)
                            prev_pac_man = 'left'
                            rotate_pacman = True
                if event.key == pygame.K_UP:  # движение пакмена
                    for i in player_group:
                        if fl_HESOYAM or not i.wall(0, -15) and prev_pac_man != 'up':
                            player_group = pygame.sprite.Group()
                            Player(pygame.image.load(
                                'files/Pac-man/data/Pac-man_up.png').convert_alpha(), 1,
                                   3,
                                   coord_x / title_width, coord_y / title_height, 0, -6)
                            prev_pac_man = 'up'
                            rotate_pacman = True
                if event.key == pygame.K_ESCAPE:  # пауза
                    pause = True
                    pygame.mixer.music.pause()
        else:
            if event.type == pygame.KEYDOWN:  # снятие паузы
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.unpause()
                    pause = False
    if not pause:  # изменение поля если нет паузы
        screen.fill((0, 0, 0))
        wall_group = pygame.sprite.Group()
        if generating_level == 0:  # закрытие блоков после выхода врагов из спавна
            generate_level(load_level(levelload1 + '.txt'))
        else:
            generate_level(load_level(levelload2 + '.txt'))
        candycash_counter()  # запуск счетчика
        all_sprites.draw(screen)
        wall_group.draw(screen)
        time.sleep(0.06)  # задержка
        player_group.update()
        left_enemy_group.update()
        pygame.display.flip()
        if fl_death is True or len(point_group) == 0 or \
                len(left_enemy_group) == 0:  # выигрыш или проигрыш
            game_running = False  # остановка игрового цикла
            end_screen_running = True  # запуск цикла конечного экрана
    else:  # затухание экрана
        screen2 = pygame.Surface((width, height))
        screen2.set_colorkey((255, 255, 255))
        screen2.set_alpha(7)
        screen.blit(screen2, (0, 0))
        pygame.display.flip()
        time.sleep(0.03)

end_screen_enemy = pygame.sprite.Group()  # враги на конечном экране
End_screen_enemies(pygame.image.load('files/Pac-man/data/end_screen_error.png').convert_alpha(),
                   2, 1, 0, 516)
End_screen_enemies(
    pygame.image.load('files/Pac-man/data/end_screen_error2.png').convert_alpha(),
    2, 1, 0, 290)

while end_screen_running:  # цикл конечного экрана
    number = 1  # переменная для того чтобы после выигрыша не запускалася проигрыш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
            # выход
        if event.type == pygame.KEYDOWN:
            terminate()
    screen.fill((0, 0, 0))
    if number == 1:  # запуск экрана проигрыша или выгрыша
        end_screen(fl_death)  # функция проигрыша и выигрыша
    pygame.display.flip()
pygame.quit()  # выход из игры
# конец!
