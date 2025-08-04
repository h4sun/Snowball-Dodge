import pygame
import os
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Run From Snow")
clock = pygame.time.Clock()

def game_loop():
    score = 0
    velocity = 10
    character_velocity = 10
    snowball_width, snowball_height = 75, 75
    character_width, character_height = 150, 200

    snowball_surface = pygame.image.load(os.path.join("assets/snowball.png"))
    snowball_surface_scaled = pygame.transform.scale(
        snowball_surface, (snowball_width, snowball_height)).convert_alpha()
    snowball_rect = snowball_surface_scaled.get_rect(
        midbottom=(random.randint(0, width - snowball_width), 0))

    character_surface = pygame.image.load(os.path.join("assets/character.png"))
    character_surface_scaled = pygame.transform.scale(
        character_surface, (character_width, character_height)).convert_alpha()
    character_rect = character_surface_scaled.get_rect(
        midbottom=(100, height))

    snowball_counter = 0

    running = True
    while running:
        screen.fill("gray")

        text = pygame.font.Font(None, 50)
        text_surface = text.render("Score: " + str(score), True, "black")
        screen.blit(text_surface, (0, 0))
        screen.blit(character_surface_scaled, character_rect)
        screen.blit(snowball_surface_scaled, snowball_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if character_rect.x + character_width + character_velocity < width:
                character_rect.x += character_velocity
        if keys[pygame.K_a]:
            if character_rect.x - character_velocity > 0:
                character_rect.x -= character_velocity

        snowball_rect.y += velocity
        if snowball_rect.y > height:
            snowball_rect.y = 0
            snowball_rect.x = random.randint(0, width - snowball_width)
            snowball_counter += 1
            score += 1
            if snowball_counter % 10 == 0:
                velocity += 1
            if snowball_counter % 25 == 0:
                character_velocity += 1

        if character_rect.colliderect(snowball_rect):
            running = False

        pygame.display.update()
        clock.tick(60)

    return score

def end_screen(final_score):
    waiting = True
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 30)

    while waiting:
        screen.fill("black")

        end_text = font.render(f"Game Over! Your Score: {final_score}", True, "white")
        restart_text = small_font.render("Press R to Restart or Q to Quit", True, "white")

        screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 2 - 50))
        screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Restart
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        pygame.display.update()
        clock.tick(30)

def main():
    while True:
        score = game_loop()
        end_screen(score)

if __name__ == "__main__":
    main()
