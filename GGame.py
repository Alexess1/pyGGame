import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 300), ) #flags=pygame.NOFRAME
pygame.display.set_caption('NEGGA')
icon = pygame.image.load('asets/negga.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('asets/bg.jpg')

myfoun = pygame.font.Font('founts/PostalShrift.ttf', 40)

walk_right = [
    pygame.image.load('asets/Right1.png'),
    pygame.image.load('asets/Right1.png'),
    pygame.image.load('asets/Right2.png'),
    pygame.image.load('asets/Right2.png')
]

walk_left = [
    pygame.image.load('asets/Left1.png'),
    pygame.image.load('asets/Left1.png'),
    pygame.image.load('asets/Left2.png'),
    pygame.image.load('asets/Left2.png')
]

Player_anim_count = 0

bg_x = 0
Player_speed = 5
Player_x = 100
Player_y = 175

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/bg_sound.mp3')
bg_sound.play()
running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[Player_anim_count], (Player_x, Player_y))
    else:
        screen.blit(walk_right[Player_anim_count], (Player_x, Player_y))


    if keys[pygame.K_LEFT] and Player_x > 5:
        Player_x -= Player_speed
    elif keys[pygame.K_RIGHT] and Player_x < 500:
        Player_x += Player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                Player_y -= (jump_count ** 2) / 2
            else:
                Player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    if Player_anim_count == 3:
        Player_anim_count = 0
    else:
        Player_anim_count += 1
    pygame.display.update()

    if bg_x == -600:
        bg_x = 0
    else:
        bg_x -= 5

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_9:
                screen.fill((147, 24, 255))

    clock.tick(20)