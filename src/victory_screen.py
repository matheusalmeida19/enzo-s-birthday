# src/victory_screen.py
import pygame

def show_victory_screen(screen):
    pygame.init()

    # Iniciar música da tela de vitória
    pygame.mixer.stop()
    pygame.mixer.music.load("assets/songs/song2.mp3")
    pygame.mixer.music.play(-1)  # -1 para repetir indefinidamente
    
    
    
    # Definir cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Carregar fundo da tela de vitória (se tiver uma imagem, adicione aqui)
    victory_bg = pygame.image.load("assets/img/bg_victory.png")
    victory_bg = pygame.transform.scale(victory_bg, (screen.get_width(), screen.get_height()))

    # Carregar fonte pixelada
    font = pygame.font.Font("assets/fonts/mine.ttf", 40)
    small_font = pygame.font.Font("assets/fonts/mine.ttf", 20)

    # Criar textos
    title_text = font.render("Happy Birthday!", True, WHITE)
    replay_text = small_font.render("Pressione R para Jogar Novamente", True, WHITE)
    menu_text = small_font.render("Pressione M para Menu Inicial", True, WHITE)

    running = True
    while running:
        screen.blit(victory_bg, (0, 0))  # Exibir fundo
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 150))
        screen.blit(replay_text, (screen.get_width() // 2 - replay_text.get_width() // 2, 200))
        screen.blit(menu_text, (screen.get_width() // 2 - menu_text.get_width() // 2, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Jogar novamente
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/songs/song1.mp3")  # Retomar a música do jogo
                    pygame.mixer.music.play(-1)
                    return "replay"
                if event.key == pygame.K_m:  # Voltar ao menu inicial
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/songs/song1.mp3")  # Música da tela inicial
                    pygame.mixer.music.play(-1)
                    return "menu"
            

        pygame.display.update()
