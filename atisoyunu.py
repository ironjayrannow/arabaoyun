import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roket Oyunu")

BG = pygame.transform.scale(pygame.image.load("yol.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
CAR_WIDTH = 40
CAR_HEIGHT = 60
CAR_VEL = 3

FONT = pygame.font.SysFont("komikaaxisnormal", 30)

def draw(player, elapsed_time, cars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Zaman: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for car in cars:
        pygame.draw.rect(WIN, "blue", car)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    car_add_increment = 2000
    car_count = 0

    cars = []
    hit = False

    while run:
        car_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if car_count > car_add_increment:
            for _ in range(17):
                car_x = random.randint(0, WIDTH - CAR_WIDTH)
                car = pygame.Rect(car_x, -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
                cars.append(car)
            car_add_increment = max(200, car_add_increment - 50)
            car_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for car in cars[:]:
            car.y += CAR_VEL
            if car.y > HEIGHT:
                cars.remove(car)
            elif car.y + car.height >= player.y and car.colliderect(player):
                cars.remove(car)
                hit = True
                break

        if hit:
            lost_text =  FONT.render("Kaybettin HAHAHA!", 1 , "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break    

        draw(player, elapsed_time, cars)

    pygame.quit()


if __name__ == "__main__":
    main()     
