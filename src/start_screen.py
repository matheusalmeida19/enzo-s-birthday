import pygame
import sys  

def show_start_screen(screen):
    pygame.init()
    
    pygame.mixer.init()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("assets/songs/song1.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)  # -1 para repetir indefinidamente
    
    # Carregar imagem de fundo
    bg_img = pygame.image.load("assets/img/bg2.jpg")
    bg_img = pygame.transform.scale(bg_img, (screen.get_width(), screen.get_height()))
    
    
    # Definir cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

  
    font = pygame.font.Font("assets/fonts/mine.ttf", 40)

    # Criar texto
    title_text = font.render("Enzo's Birthday", True, (75, 0, 130))
    instructions_text = pygame.font.Font("assets/fonts/mine.ttf", 20).render("Pressione ENTER para jogar", True, (75, 0, 130))

    # Loop da tela inicial
    running = True
    while running:
        screen.blit(bg_img, (0, 0))

        # Posicionar texto no centro da tela
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 200))
        screen.blit(instructions_text, (screen.get_width() // 2 - instructions_text.get_width() // 2, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False  # Sai do loop ao pressionar ENTER

        pygame.display.update()
