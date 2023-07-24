import pygame
from load_assets import *

mario_sheet = Load_assets("mario_sheet.png")
level_sheet = Load_assets("bg-1-1.png")


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 400))
    level = [4000, 500]
    pygame.display.set_caption("Scuffed mario")
    running = True

    player_speed = 3
    player_pos = [300, 192]
    mario_sprites = []
    anim_step = [3, 3, 6, 1]
    step_count = 0
    state = 0
    last_update = pygame.time.get_ticks()
    anim_cd = 250
    frame = 0
        
    cam_pos = pygame.math.Vector2()
    direction = "none"

    level1 = level_sheet.load_image("data/bg-1-1.png")

    # Load all the sprites states (idle, run, jump, dead)
    # and the sprites that match
    for anim in anim_step:
        temp_sprite_list = []
        for _ in range(anim):
            temp_sprite_list.append(mario_sheet.get_sprites(step_count, 16, 16, 1))
            step_count += 1
        mario_sprites.append(temp_sprite_list)

    while running:
        player_rec = pygame.Rect(player_pos[0], player_pos[1], 16, 16)
        screen.fill((255,255,255))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        cam_pos.x = player_rec.centerx - screen.get_width() // 2
        cam_pos.y = player_rec.centery - screen.get_height() // 2
        level_offset = player_rec.topleft + cam_pos
        
        # Update animations
        current_tick = pygame.time.get_ticks()
        if current_tick - last_update >= anim_cd:
            frame += 1
            last_update = current_tick
            if frame >= len(mario_sprites[state]):
                frame = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
            cam_pos.x += player_speed
            state = 1
            direction = "right"
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
            cam_pos.x -= player_speed
            state = 1
            direction = "left"
        else:
            state = 0
            frame = 0


        # Render sprite
        screen.blit(level1, (0 - level_offset.x ,0))
        pygame.draw.rect(screen, "red", player_rec)

        if direction == "right":
            screen.blit(mario_sprites[state][frame], (player_pos[0], player_pos[1]))
        elif direction == "left":
            screen.blit(pygame.transform.flip(mario_sprites[state][frame], True, False), (player_pos[0], player_pos[1]))
        else:
            screen.blit(mario_sprites[state][frame], (player_pos[0], player_pos[1]))

        # stop the player from moving off screen
        player_pos[0] = max(0, min(player_pos[0], level1.get_width()))


        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()