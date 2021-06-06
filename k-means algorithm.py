import pygame
from random import randint
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("K-Means")
running = True
clock = pygame.time.Clock()

background = (214, 214, 214)
BACKGROUND_PANEL = (249, 255, 230)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)

COLOR = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRASS, GRAPE]

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
clusters = []
labels = []

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
                labels = []

                # assign point to closet cluster
                for p in points:
                    distance_to_cluster = []
                    for c in clusters:
                        distances = distance(p, c)
                        distance_to_cluster.append(distances)

                    min_distance = min(distance_to_cluster)
                    label = distance_to_cluster.index(min_distance)
                    labels.append(label)

                # update clusters
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1
                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x, new_cluster_y]
                print("run")

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                clusters = []
                for i in range(K):
                    random_point = [randint(0, 700), randint(0, 500)]
                    clusters.append(random_point)
                print("random")

            # Reset button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print("reset")

            # algorithm button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print("algorithm")

    # draw cluster
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLOR[i], (int(clusters[i][0]) + 50, int(clusters[i][1]) + 50), 10)

    # draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)

        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
        else:
            pygame.draw.circle(screen, COLOR[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5)
    pygame.display.flip()

pygame.quit()
