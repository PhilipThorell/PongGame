import pygame
import random


pygame.init()

screen = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Pong Game")

game_started = False
main_menu_bool = True
help_menu_bool = False
AI = False
two_player_help_menu_bool = False
two_player = False
victory = False
the_winner = ""

player_1_y = 325
player_2_y = 325
player_1_speed = 0
player_2_speed = 0
ball_center_x = 650
ball_center_y = 400
ball_speed_x = 4.5
ball_speed_y = 5.5
ball_velocity_x = ball_speed_x
ball_velocity_y = ball_speed_y
ball_speed_change_x = 0
ball_speed_change_y = 0

player_1_score = 0
player_2_score = 0

clock = pygame.time.Clock()


def main_menu():
    pygame.draw.rect(screen, "#FFFFFF", (300, 100, 700, 200))
    pygame.draw.rect(screen, "#000000", (315, 115, 670, 170))
    font = pygame.font.Font("freesansbold.ttf", 100)
    text_surface = font.render("PONG GAME", True, "#FFFFFF")
    text_rect = text_surface.get_rect(center=(650, 200))
    screen.blit(text_surface, text_rect)

    pygame.draw.rect(screen, "#FFFFFF", (500, 450, 300, 100))
    start_font = pygame.font.Font("freesansbold.ttf", 65)
    text_surface = start_font.render("START", True, "#000000")
    text_rect = text_surface.get_rect(center=(650, 500))
    screen.blit(text_surface, text_rect)

    pygame.draw.rect(screen, "#FFFFFF", (500, 600, 300, 100))
    two_player_font = pygame.font.Font("freesansbold.ttf", 37)
    text_surface = two_player_font.render("TWO PLAYERS", True, "#000000")
    text_rect = text_surface.get_rect(center=(650, 650))
    screen.blit(text_surface, text_rect)


def start_help_menu():
    font = pygame.font.Font("freesansbold.ttf", 30)
    text_surface = font.render("You are on the left and moves up and down with ", True, "#FFFFFF")
    text_rect = text_surface.get_rect(center=(650, 320))
    screen.blit(text_surface, text_rect)
    text2_surface = font.render("W and S or Up Arrow and Down Arrow", True, "#FFFFFF")
    text2_rect = text2_surface.get_rect(center=(650, 360))
    screen.blit(text2_surface, text2_rect)

    ready_font = pygame.font.Font("freesansbold.ttf", 50)
    pygame.draw.rect(screen, "#FFFFFF", (950, 640, 250, 100))
    text_surface = ready_font.render("READY", True, "#000000")
    text_rect = text_surface.get_rect(center=(1075, 690))
    screen.blit(text_surface, text_rect)


def two_player_help_menu():
    font = pygame.font.Font("freesansbold.ttf", 30)
    text_surface = font.render("player 1 is on the left and moves up and down with W and S", True, "#FFFFFF")
    text_rect = text_surface.get_rect(center=(650, 350))
    screen.blit(text_surface, text_rect)
    text_surface = font.render("player 2 is on the right and moves up", True, "#FFFFFF")
    text_rect = text_surface.get_rect(center=(650, 420))
    screen.blit(text_surface, text_rect)
    text_surface = font.render("and down with Up Arrow and Down Arrow", True, "#FFFFFF")
    text_rect = text_surface.get_rect(center=(650, 450))
    screen.blit(text_surface, text_rect)

    ready_font = pygame.font.Font("freesansbold.ttf", 50)
    pygame.draw.rect(screen, "#FFFFFF", (950, 640, 250, 100))
    text_surface = ready_font.render("READY", True, "#000000")
    text_rect = text_surface.get_rect(center=(1075, 690))
    screen.blit(text_surface, text_rect)


def game_screen():
    global player_1_y, player_2_y, player_1_score, player_2_score, ball_center_x, ball_center_y
    global ball_velocity_x, ball_velocity_y, ball_speed_change_x, ball_speed_change_y, the_winner
    global game_started, victory, two_player, player_1_speed, player_2_speed

    pygame.draw.rect(screen, "#FFFFFF", (50, player_1_y, 20, 150))
    pygame.draw.rect(screen, "#FFFFFF", (1230, player_2_y, 20, 150))

    score_font = pygame.font.Font("freesansbold.ttf", 40)
    score_text_surface = score_font.render(f"{player_1_score}-{player_2_score}", True, "#FFFFFF")
    score_text_rect = score_text_surface.get_rect(center=(650, 30))
    screen.blit(score_text_surface, score_text_rect)

    player_1_y += player_1_speed
    player_1_y = max(0, min(player_1_y, 650))

    player_2_y += player_2_speed
    player_2_y = max(0, min(player_2_y, 650))

    ball((ball_center_x, ball_center_y))

    ball_center_x += (ball_velocity_x + ball_speed_change_x)
    if ball_center_x <= 90:
        if player_1_y <= ball_center_y <= player_1_y + 150:
            ball_velocity_x = ball_speed_x
            ball_speed_change_x = abs(ball_speed_change_x)
            ball_speed_change_x += 0.5
    if ball_center_x >= 1210:
        if player_2_y <= ball_center_y <= player_2_y + 150:
            ball_velocity_x = -ball_speed_x
            ball_speed_change_x = -ball_speed_change_x
            ball_speed_change_x += -0.5

    ball_center_y += (ball_velocity_y + ball_speed_change_y)
    if ball_center_y >= 780:
        ball_velocity_y = -ball_speed_y
        ball_speed_change_y = -ball_speed_change_y
        ball_speed_change_y += -0.5
    if ball_center_y <= 0:
        ball_velocity_y = ball_speed_y
        ball_speed_change_y = abs(ball_speed_change_y)
        ball_speed_change_y += 0.5

    if ball_center_x >= 1280:
        ball_center_x = 650
        ball_center_y = 400
        player_1_y = 325
        player_2_y = 325
        ball_speed_change_x = 0
        ball_speed_change_y = 0
        ball_velocity_x = -ball_speed_x
        player_1_score += 1
    if ball_center_x <= 0:
        ball_center_x = 650
        ball_center_y = 400
        player_1_y = 325
        player_2_y = 325
        ball_speed_change_x = 0
        ball_speed_change_y = 0
        ball_velocity_x = ball_speed_x
        player_2_score += 1

    if AI:
        if ball_center_x > 600 and ball_center_y < (player_2_y + 75):
            player_2_speed = -5.5
        elif ball_center_x > 0 and ball_center_y > (player_2_y + 75):
            player_2_speed = 5.5
        else:
            bool = random.random
            if bool:
                player_2_speed = 5.5
            else:
                player_2_speed = -5.5

    if player_1_score == 3:
        if two_player:
            the_winner = "PLAYER 1 WINS!"
        else:
            the_winner = "YOU WIN!"
        game_started = False
        victory = True
    if player_2_score == 3:
        if two_player:
            the_winner = "PLAYER 2 WINS!"
        else:
            the_winner = "AI WINS!"
        game_started = False
        victory = True


def victory_screen(winner):
    global player_1_score, player_2_score
    player_1_score = 0
    player_2_score = 0

    font = pygame.font.Font("freesansbold.ttf", 100)
    text_surface = font.render(f"{winner}", True, "#FFFFFF")
    text_rect = text_surface.get_rect(center=(650, 400))
    screen.blit(text_surface, text_rect)

    button_font = pygame.font.Font("freesansbold.ttf", 35)
    pygame.draw.rect(screen, "#FFFFFF", (950, 640, 250, 100))
    button_text_surface = button_font.render("MAIN MENU", True, "#000000")
    button_text_rect = button_text_surface.get_rect(center=(1075, 690))
    screen.blit(button_text_surface, button_text_rect)

    button_font = pygame.font.Font("freesansbold.ttf", 35)
    pygame.draw.rect(screen, "#FFFFFF", (100, 640, 250, 100))
    button_text_surface = button_font.render("PLAY AGAIN", True, "#000000")
    button_text_rect = button_text_surface.get_rect(center=(225, 690))
    screen.blit(button_text_surface, button_text_rect)


def handle_keys():
    global player_1_speed, player_2_speed
    keys = pygame.key.get_pressed()
    if two_player:
        if keys[pygame.K_w]:
            player_1_speed = -5.5
        elif keys[pygame.K_s]:
            player_1_speed = 5.5
        else:
            player_1_speed = 0

        if keys[pygame.K_UP]:
            player_2_speed = -5.5
        elif keys[pygame.K_DOWN]:
            player_2_speed = 5.5
        else:
            player_2_speed = 0
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_1_speed = -5.5
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_1_speed = 5.5
        else:
            player_1_speed = 0


def ball(center=(650, 400)):
    pygame.draw.circle(screen, "#FFFFFF", center, 20)


running = True
while running:
    screen.fill("#000000")

    if main_menu_bool:
        main_menu()
    elif help_menu_bool:
        start_help_menu()
    elif two_player_help_menu_bool:
        two_player_help_menu()
    elif game_started:
        handle_keys()
        game_screen()
    elif victory:
        victory_screen(the_winner)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if main_menu_bool:
                if 500 <= mouse[0] <= 800 and 450 <= mouse[1] <= 550:
                    main_menu_bool = False
                    help_menu_bool = True
                    AI = True
                if 500 <= mouse[0] <= 800 and 600 <= mouse[1] <= 700:
                    main_menu_bool = False
                    two_player_help_menu_bool = True
                    two_player = True
            elif help_menu_bool:
                if 950 <= mouse[0] <= 1200 and 640 <= mouse[1] <= 740:
                    help_menu_bool = False
                    game_started = True
            elif two_player_help_menu_bool:
                if 950 <= mouse[0] <= 1200 and 640 <= mouse[1] <= 740:
                    two_player_help_menu_bool = False
                    game_started = True
            elif victory:
                if 950 <= mouse[0] <= 1200 and 640 <= mouse[1] <= 740:
                    victory = False
                    main_menu_bool = True
                if 100 <= mouse[0] <= 350 and 640 <= mouse[1] <= 740:
                    victory = False
                    game_started = True

    pygame.display.update()
    clock.tick(60)
