import pygame, sys, Funcoes

def Menu():

    #Inicio da tela do menu
    pygame.init()

    InMenu = True

    #Adquirindo o tamanho da tela do computador utilizado:
    ScreenDimensions = pygame.display.get_desktop_sizes()[0]

    pygame.display.set_caption('Plane Crush - 1.0.2')

    Menu_Screen = pygame.display.set_mode(ScreenDimensions)

    #A imagem de fundo do menu é carregada e posta na mesma escala da tela.
    ImagemMenu = pygame.image.load('Startwallpaper.jpg')
    ImagemMenu = pygame.transform.scale(ImagemMenu, (ScreenDimensions))

    while InMenu:

        Menu_Screen.blit(ImagemMenu, (0,0))

        #Classe para os botões do menu(Os botões se ajustam às dimensões da tela utilizada.)
        class Botao:

            def __init__(self, x, y, imagem):

                self.imagename = imagem
                self.imagem = pygame.image.load(imagem)
                self.imagem = pygame.transform.scale(self.imagem, ((20/100 * ScreenDimensions[0]), (7/100 * ScreenDimensions[1])))
                self.rect = self.imagem.get_rect()
                self.rect.center = (x, y)

            def Selfdraw(self):

                BotaoPressionado = False

                Mouse_pos = pygame.mouse.get_pos()

                #verifica-se a posição do ponteiro em relação ao botão(Se o mouse está encima do botão) e se o botão é clicado:
                if self.rect.collidepoint(Mouse_pos):

                    self.imagem = pygame.transform.scale(self.imagem, ((28/100 * ScreenDimensions[0]), (10/100 * ScreenDimensions[1])))

                    if pygame.mouse.get_pressed()[0] == 1:
                        BotaoPressionado = True
                        return BotaoPressionado
                    
                else:
                    #A imagem é recarregada por conta da perda de qualidade ao mudar a escala:
                    self.imagem = pygame.transform.scale(pygame.image.load(self.imagename), ((25/100 * ScreenDimensions[0]), (9/100 * ScreenDimensions[1])))
                
                Menu_Screen.blit(self.imagem, (self.rect.x, self.rect.y))


        pygame.font.init()

        Mfont = pygame.font.SysFont('lucidahandwriting', int(3 / 100 * ScreenDimensions[0]))

        Mvfont = pygame.font.SysFont('lucidahandwriting', int(1 / 100 * ScreenDimensions[0]))

        text_ = Mfont.render('Plane Crush', True, (255, 170, 10))
        textv = Mvfont.render('v1.0.2', True, (255, 170, 10))

        Menu_Screen.blit(text_, ((ScreenDimensions[0] - (80 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (75 / 100 * ScreenDimensions[1]))))
        Menu_Screen.blit(textv, ((ScreenDimensions[0] - (42 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (71.5 / 100 * ScreenDimensions[1]))))

        BotaoInicio = Botao((ScreenDimensions[0] - (20/100 * ScreenDimensions[0])), (ScreenDimensions[1] - (40/100 * ScreenDimensions[1])), 'BotaoInicio.png')
        BotaoHistorico = Botao((ScreenDimensions[0] - (20/100 * ScreenDimensions[0])), (ScreenDimensions[1] - (30/100 * ScreenDimensions[1])), 'BotaoHistorico.png')
        BotaoSair = Botao((ScreenDimensions[0] - (20/100 * ScreenDimensions[0])), (ScreenDimensions[1] - (20/100 * ScreenDimensions[1])), 'BotaoSair.png')

        #Se o botão de Inicio retornar 'clicado', continuar para o jogo:
        if BotaoInicio.Selfdraw() == True:

            Funcoes.MainSector()
            
        if BotaoHistorico.Selfdraw():

            Funcoes.Historico()

        #Se o botão de saida retornar 'clicado', continuar para o jogo:
        if BotaoSair.Selfdraw():
            
            InMenu = False
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()


        pygame.display.update()


Menu()