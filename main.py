import pygame
import random
import time
pygame.font.init()

WIDTH, HEIGHT= 1000, 800
window= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Destroyers")
BG= pygame.image.load("677271.png")
player_width= 40
player_height= 60
player_vel= 5
font=pygame.font.SysFont("comicsans", 24)
starwidth= 10
starheight=30
star_vel= 3

def draw(player, elapsed_time, stars):
    window.blit(BG, (0, 0))
    time_display= font.render(f"Time: {round(elapsed_time)}s", 1, "red")
    window.blit(time_display, (10,10))
    pygame.draw.rect(window,"blue", player)

    for star in stars:
        pygame.draw.rect(window, "purple", star)

    pygame.display.update()
def main():
    pygame.init()
    run=True
    player= pygame.Rect(200, HEIGHT - player_height, player_width, player_height)
    clock= pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0
    star_add_inc= 2000
    star_count=0
    stars =[]
    hit=False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        if star_count>star_add_inc:
            for i in range(5):
                star_x=random.randint(0, WIDTH - starwidth)
                star = pygame.Rect(star_x, -starheight, starwidth, starheight)
                stars.append(star)
            star_add_inc=max(200, star_add_inc-50)
            star_count=0

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-player_vel>=0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.width<=WIDTH:
            player.x += player_vel
        if keys[pygame.K_DOWN] and player.y+player_vel + player.height<=HEIGHT:
            player.y += player_vel
        if keys[pygame.K_UP] and player.y-player_vel>=550:
            player.y -= player_vel

        for star in stars[:]:
            star.y += star_vel
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit=True
                break

        if hit:
            lost_text= font.render("Destroyed bro!", 1, "red")
            window.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    pygame.quit()

if __name__=="__main__":
    main()

