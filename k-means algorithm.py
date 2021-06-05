import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("K-Means")

running = True

clock = pygame.time.Clock()

background = (214, 214, 214)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_PANEL = (249, 255, 230)

font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render('Run', True, WHITE)
text_random = font.render('Random', True, WHITE)
text_algorithm = font.render('Algorithm', True, WHITE)
text_reset = font.render('Reset', True, WHITE)

K = 0
err = 0
points = []

while running:
    clock.tick(60)
    screen.fill(background)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw interface
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

    # K button +
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(text_plus, (865, 50))

    # K button -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(text_minus, (970, 50))

    # K value
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (1050, 50))

    # run button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(text_run, (900, 150))

    # random button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(text_random, (865, 250))

    # Algorithm button by sklearn
    pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))
    screen.blit(text_algorithm, (855, 550))

    # Reset button
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(text_reset, (875, 450))

    # error text
    text_error = font.render("Error = " + str(int(err)), True, BLACK)
    screen.blit(text_error, (850, 350))

    # Draw mouse poisition
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True, BLACK)
        screen.blit(text_mouse, (mouse_x + 5, mouse_y + 5))

    # End draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # create point on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)
                print(points)

            # Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                K += 1
                print("Press K +")

            # Change K button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
                print("Press K -")

            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                print("run pressed")

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                print("random")

            # Reset button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print("reset")

            # algorithm button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print("algorithm")

    # draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1]+ 50), 6)
        pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
    pygame.display.flip()

pygame.quit()
