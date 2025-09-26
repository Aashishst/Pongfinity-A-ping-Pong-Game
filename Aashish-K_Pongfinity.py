import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Multiplayer Pongfinity Game")
clock = pygame.time.Clock()

x = 100
y = 150
X = 230
Y = 155
speed = 1
direction = 1
d_x = 1

intro = pygame.font.SysFont('Harlow Solid', 45)
start_font = pygame.font.SysFont('Harlow Solid', 30)
score_font = pygame.font.SysFont('Harlow Solid', 35)

P_Score = 0
P_Highscore = 0
P_LastScore = 0

O_Score = 0
O_Highscore = 0
O_LastScore = 0

S_Score = 0
S_Highscore = 0
S_LastScore = 0

scorefont = pygame.font.SysFont("Harlow Solid", 38)
S_font = pygame.font.SysFont("Harlow Solid", 35)

def load_score(filename):
    try:
        with open(filename, "r") as f:
            return int(f.read().strip())
    except:
        return 0

def save_score(value, filename):
    with open(filename, "w") as f:
        f.write(str(value))

P_Highscore = load_score("highscore.txt")
P_LastScore = load_score("score.txt")

O_Highscore = load_score("O_highscore.txt")
O_LastScore = load_score("O_score.txt")

S_Highscore = load_score("S_highscore.txt")
S_LastScore = load_score("S_score.txt")

WIDTH, HEIGHT = 600, 600

player = pygame.Rect(50, HEIGHT // 2 - 40, 10, 80)
opponent = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 40, 10, 80)
S_player = pygame.Rect(WIDTH // 2 - 20, HEIGHT - 90, 80, 10)

scoreboard = pygame.Surface((600, 70), pygame.SRCALPHA)
scoreboard.fill((30, 30, 30, 108))

player_border = pygame.Rect(10, 80, 5, 505)
opp_border = pygame.Rect(WIDTH - 15, 80, 5, 505)
S_border = pygame.Rect(10, HEIGHT - 40, WIDTH - 20, 5)

boundary = pygame.Rect(0, scoreboard.get_height(), WIDTH, HEIGHT - scoreboard.get_height())

ball_size = 15
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
ball_speed = 3
ball_dx = random.choice([-1, 1]) * ball_speed
ball_dy = random.choice([-1, 1]) * ball_speed

single_button = pygame.Rect(100, 240, 195, 45,)
double_button = pygame.Rect(320, 240, 195, 45,)

def menu():
    global x, X, direction, d_x, start_game_rect
    screen.fill((0, 0, 0))
    outline = pygame.draw.rect(screen, (0, 0, 255), (20, 20, 560, 560), width=3, border_radius=5)
    outline_2 = pygame.draw.rect(screen, (0, 255, 255), (30, 30, 540, 540), width=3, border_radius=5)
    pygame.draw.rect(screen, (3, 218, 197), single_button, width=3, border_radius=8)
    pygame.draw.rect(screen, (3, 218, 197), double_button, width=3, border_radius=8)
    game_text = intro.render("Pongfinity", True, (0, 255, 255))
    screen.blit(game_text, (200, 60))
    s_text = start_font.render("Single Player", True, (3, 218, 197))
    d_text = start_font.render("Multi Player", True, (3, 218, 197))
    screen.blit(s_text, (single_button.x + 12, single_button.y + 2))
    screen.blit(d_text, (double_button.x + 12, double_button.y + 2))
    p_prev = score_font.render(f"P Prev: {P_LastScore}", True, (52, 18, 197))
    p_high = score_font.render(f"P High: {P_Highscore}", True, (52, 18, 197))
    o_prev = score_font.render(f"O Prev: {O_LastScore}", True, (255, 100, 0))
    o_high = score_font.render(f"O High: {O_Highscore}", True, (255, 100, 0))
    s_prev = score_font.render(f"S Prev: {S_LastScore}", True, (200, 200, 200))
    s_high = score_font.render(f"S High: {S_Highscore}", True, (200, 200, 200))
    screen.blit(p_prev, (120, 320))
    screen.blit(p_high, (310, 320))
    screen.blit(o_prev, (120, 370))
    screen.blit(o_high, (310, 370))
    screen.blit(s_prev, (120, 420))
    screen.blit(s_high, (310, 420))
    x += speed * direction
    if x > 100:
        direction = -1
    elif x < 80:
        direction = 1
    X += speed * d_x
    if X > 100:
        d_x = -1
    elif X < 80:
        d_x = 1
    pygame.display.flip()

def Single(keys):
    global S_Score, S_Highscore, ball_dx, ball_dy, running, S_player, ball
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 100, 0), S_player, border_radius=20)
    pygame.draw.rect(screen, (255, 100, 0), S_border, border_radius=10)
    screen.blit(scoreboard, (0, 0))
    S_score_text = S_font.render(f"Score: {S_Score}", True, (255, 100, 0))
    S_High_Text = S_font.render(f"High Score: {S_Highscore}", True, (255, 100, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    if keys[pygame.K_LEFT]:
        S_player.x-= 7
    if keys[pygame.K_RIGHT]:
        S_player.x += 7
    ball.x += ball_dx
    ball.y += ball_dy
    if ball.top <= 70 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.colliderect(S_player):
        ball_dy *= -1
        
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.colliderect(S_border):
        save_score(S_Score, "S_score.txt")
        running = False
    S_player.clamp_ip(boundary)
    screen.blit(S_score_text, (60, 13))
    screen.blit(S_High_Text, (300, 13))
    
    if ball.colliderect(S_player):
        # check which side was hit
        if abs(ball.right - S_player.left) < 12:
            ball.right = S_player.left - 1
            ball_dx = -abs(ball_dx)

        elif abs(ball.left - S_player.right) < 12:
            ball.left = S_player.right + 1
            ball_dx = abs(ball_dx)


    # add score on valid bounce
        S_Score += 5
        if S_Score > S_Highscore:
            S_Highscore = S_Score
            save_score(S_Highscore, "S_highscore.txt")

    # always clamp ball inside screen after moves
    if ball.left < 0:
        ball.left = 0
        ball_dx = abs(ball_dx)
    elif ball.right > WIDTH:
        ball.right = WIDTH
        ball_dx = -abs(ball_dx)

    pygame.display.flip()

def Double(keys):
    global P_Score, O_Score, P_Highscore, O_Highscore, ball_dx, ball_dy, running, player, opponent, ball
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 10, 255), player, border_radius=20)
    pygame.draw.rect(screen, (255, 100, 0), opponent, border_radius=20)
    pygame.draw.rect(screen, (0, 10, 255), player_border, border_radius=10)
    pygame.draw.rect(screen, (255, 100, 0), opp_border, border_radius=10)
    screen.blit(scoreboard, (0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    score_text = scorefont.render(f"Score: {P_Score}", True, (0, 10, 255))
    screen.blit(score_text, (40, 10))
    O_score_text = scorefont.render(f"Score: {O_Score}", True, (255, 100, 0))
    screen.blit(O_score_text, (420, 10))
    if keys[pygame.K_w]:
        player.y -= 7
    if keys[pygame.K_s]:
        player.y += 7
    if keys[pygame.K_UP]:
        opponent.y -= 7
    if keys[pygame.K_DOWN]:
        opponent.y += 7
    player.clamp_ip(boundary)
    opponent.clamp_ip(boundary)
    ball.x += ball_dx
    ball.y += ball_dy
    if ball.top <= 70 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_dx *= -1
                
    if ball.colliderect(player):
        if abs(ball.right - player.left) < 12:
            ball.right = player.left - 1
            ball_dx = -abs(ball_dx)
        elif abs(ball.left - player.right) < 12:
            ball.left = player.right + 1
            ball_dx = abs(ball_dx)

        P_Score += 5
        if P_Score > P_Highscore:
            P_Highscore = P_Score
            save_score(P_Highscore, "highscore.txt")

    if ball.colliderect(opponent):
        if abs(ball.right - opponent.left) < 12:
            ball.right = opponent.left - 1
            ball_dx = -abs(ball_dx)
        elif abs(ball.left - opponent.right) < 12:
            ball.left = opponent.right + 1
            ball_dx = abs(ball_dx)
            
        O_Score += 5
        if O_Score > O_Highscore:
            O_Highscore = O_Score
            save_score(O_Highscore, "O_highscore.txt")
    
    if ball.left <= 0 or ball.right >= WIDTH:
        save_score(P_Score, "score.txt")
        save_score(O_Score, "O_score.txt")
        running = False
        
    if ball.colliderect(player_border) or ball.colliderect(opp_border):
        save_score(P_Score, "score.txt")
        save_score(O_Score, "O_score.txt")
        running = False
    pygame.display.flip()

in_menu = True
in_game = False
mode_single = False
running = True

menu()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and in_menu:
            if single_button.collidepoint(event.pos):
                in_game = True
                in_menu = False
                mode_single = True
                ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
                ball_dx = random.choice([-1, 1]) * ball_speed
                ball_dy = random.choice([-1, 1]) * ball_speed
                S_Score = 0
                S_player.x = WIDTH // 2 - 40
            if double_button.collidepoint(event.pos):
                in_game = True
                in_menu = False
                mode_single = False
                ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
                ball_dx = random.choice([-1, 1]) * ball_speed
                ball_dy = random.choice([-1, 1]) * ball_speed
                P_Score = 0
                O_Score = 0
                player.y = HEIGHT // 2 - 40
                opponent.y = HEIGHT // 2 - 40
    if in_menu:
        menu()
    elif in_game:
        keys = pygame.key.get_pressed()
        if mode_single:
            Single(keys)
        else:
            Double(keys)
    clock.tick(60)

pygame.quit()
save_score(P_Score, "score.txt")
if P_Score > P_Highscore:
    save_score(P_Score, "highscore.txt")
save_score(O_Score, "O_score.txt")
if O_Score > O_Highscore:
    save_score(O_Score, "O_highscore.txt")
save_score(S_Score, "S_score.txt")
if S_Score > S_Highscore:
    save_score(S_Score, "S_highscore.txt")
    
if mode_single:
  print("\nGame Over! | Single Player Stats ⬇️ ")
  print(f"Single-Player Score: {S_Score}")
  print(f"Single-Player Highscore: {S_Highscore}\n")

if not mode_single:
    print("\nGame Over! | Multiplayer Stats ⬇️ ")
    print(f" Player Score: {P_Score}")
    print(f"Player Highscore: {P_Highscore}")
    print(f"Opponent Score: {O_Score}")
    print(f"Opponent Highscore: {O_Highscore}\n")