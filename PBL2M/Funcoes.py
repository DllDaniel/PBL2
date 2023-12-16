import pygame, random, pickle

def Historico():

    with open('Historico.txt', 'a') as file:
        pass

    with open('Historico.txt', 'r') as file:
        primeira_linha = file.readline()
        if primeira_linha == '':
            primeira_linha = 0
        pontos = int(primeira_linha)
        segunda_linha = file.readline(1)
        if segunda_linha == '':
            segunda_linha = 0
        vitorias = int(segunda_linha)
        terceira_linha = file.readline(2)
        if terceira_linha == '' or terceira_linha == '\n':
            terceira_linha = 0
        derrotas = int(terceira_linha)

    InHistorico = True

    ScreenDimensions = pygame.display.get_desktop_sizes()[0]

    HistoricoScreen = pygame.display.set_mode(ScreenDimensions)

    ImagemHistorico = pygame.image.load('Historico.png')
    ImagemHistorico = pygame.transform.scale(ImagemHistorico, (ScreenDimensions))

    pygame.font.init()

    hfont = pygame.font.SysFont('lucidahandwriting', int(3 / 100 * ScreenDimensions[0]))

    texth = hfont.render('Total de pontos:', True, (255, 170, 10))
    texthp = hfont.render(f'{pontos}', True, (255, 170, 10))
    texth2 = hfont.render('Total de vitórias:', True, (255, 170, 10))
    texthp2 = hfont.render(f'{vitorias}', True, (255, 170, 10))
    texth3 = hfont.render('Total de derrotas:', True, (255, 170, 10))
    texthp3 = hfont.render(f'{derrotas}', True, (255, 170, 10))


    while InHistorico:

        HistoricoScreen.blit(ImagemHistorico, (0,0))
        HistoricoScreen.blit(texth, ((ScreenDimensions[0] - (160 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (94 / 100 * ScreenDimensions[1]))))
        HistoricoScreen.blit(texthp, ((ScreenDimensions[0] - (45 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (94 / 100 * ScreenDimensions[1]))))
        HistoricoScreen.blit(texth2, ((ScreenDimensions[0] - (130 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (72 / 100 * ScreenDimensions[1]))))
        HistoricoScreen.blit(texthp2, ((ScreenDimensions[0] - (60 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (72 / 100 * ScreenDimensions[1]))))
        HistoricoScreen.blit(texth3, ((ScreenDimensions[0] - (130 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (50 / 100 * ScreenDimensions[1]))))
        HistoricoScreen.blit(texthp3, ((ScreenDimensions[0] - (60 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (50 / 100 * ScreenDimensions[1]))))

        class Botao:

            def __init__(self, x, y, imagem):

                self.imagename = imagem
                self.imagem = pygame.image.load(imagem)
                self.imagem = pygame.transform.scale(self.imagem, ((5/100 * ScreenDimensions[0]), (5/100 * ScreenDimensions[1])))
                self.rect = self.imagem.get_rect()
                self.rect.center = (x, y)

            def Selfdraw(self):

                BotaoPressionado = False

                Mouse_pos = pygame.mouse.get_pos()

                #verifica-se a posição do ponteiro em relação ao botão(Se o mouse está encima do botão) e se o botão é clicado:
                if self.rect.collidepoint(Mouse_pos):

                    self.imagem = pygame.transform.scale(self.imagem, ((6/100 * ScreenDimensions[0]), (6/100 * ScreenDimensions[1])))

                    if pygame.mouse.get_pressed()[0] == 1:
                        BotaoPressionado = True
                        return BotaoPressionado
                    
                else:
                    #A imagem é recarregada por conta da perda de qualidade ao mudar a escala:
                    self.imagem = pygame.transform.scale(pygame.image.load(self.imagename), ((5/100 * ScreenDimensions[0]), (5/100 * ScreenDimensions[1])))
                
                HistoricoScreen.blit(self.imagem, (self.rect.x, self.rect.y))

        BotaoMenu = Botao((ScreenDimensions[0] - (50/100 * ScreenDimensions[0])), (ScreenDimensions[1] - (20/100 * ScreenDimensions[1])), 'MenuButton.png')

        if BotaoMenu.Selfdraw():

                return True
        
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

def GameOver():
        
    Gov = True

    ScreenDimensions = pygame.display.get_desktop_sizes()[0]

    GameOverscreen = pygame.display.set_mode(ScreenDimensions)

    GameOverimage = pygame.image.load('Startwallpaper.jpg')
    GameOverimage = pygame.transform.scale(GameOverimage, (ScreenDimensions))
    
    while Gov:

        GameOverscreen.blit(GameOverimage, (0, 0))

        GameOverfont = pygame.font.SysFont('lucidahandwriting', int(3 / 100 * ScreenDimensions[0]))

        text_ =GameOverfont.render('Sem movimentos', True, (255, 170, 10))
        text2 =GameOverfont.render('Você perdeu!', True, (255, 170, 10))

        GameOverscreen.blit(text_, ((ScreenDimensions[0] - (100 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (85 / 100 * ScreenDimensions[1]))))
        GameOverscreen.blit(text2, ((ScreenDimensions[0] - (100 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (75 / 100 * ScreenDimensions[1]))))

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
                
                GameOverscreen.blit(self.imagem, (self.rect.x, self.rect.y))

        BotaoMenu = Botao((ScreenDimensions[0] - (50/100 * ScreenDimensions[0])), (ScreenDimensions[1] - (20/100 * ScreenDimensions[1])), 'MenuButton.png')

        if BotaoMenu.Selfdraw():

            return True

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

def EndState(Pontos):

    Win = False

    if Pontos > 35000:

        with open('Historico.txt', 'a') as file:
            pass

        with open('Historico.txt', 'r') as file:
            primeira_linha = file.readline()
            if primeira_linha == '':
                primeira_linha = 0
            pontos = int(primeira_linha)
            segunda_linha = file.readline(1)
            if segunda_linha == '':
                segunda_linha = 0
            vitorias = int(segunda_linha)

        pontos_passados = Pontos
        novo_total_pts = pontos + pontos_passados

        novo_total_vit = vitorias + 1

        with open('Historico.txt', 'r+') as file:
            file.seek(0)  
            file.write(str(novo_total_pts) + '\n')  
            file.write(str(novo_total_vit) + '\n') 

        Win = True

        ScreenDimensions = pygame.display.get_desktop_sizes()[0]

        EndScreen = pygame.display.set_mode(ScreenDimensions)

        EndImage = pygame.image.load('Startwallpaper.jpg')
        EndImage = pygame.transform.scale(EndImage, (ScreenDimensions))
        
        while Win:

            EndScreen.blit(EndImage, (0, 0))

            endfont = pygame.font.SysFont('lucidahandwriting', int(3 / 100 * ScreenDimensions[0]))

            text_ = endfont.render('Partida finalizada', True, (255, 170, 10))
            text2 = endfont.render('Você ganhou!', True, (255, 170, 10))

            EndScreen.blit(text_, ((ScreenDimensions[0] - (100 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (85 / 100 * ScreenDimensions[1]))))
            EndScreen.blit(text2, ((ScreenDimensions[0] - (100 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (75 / 100 * ScreenDimensions[1]))))

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
                    
                    EndScreen.blit(self.imagem, (self.rect.x, self.rect.y))

            BotaoMenu = Botao((ScreenDimensions[0] - (50/100 * ScreenDimensions[0])), (ScreenDimensions[1] - (20/100 * ScreenDimensions[1])), 'MenuButton.png')

            if BotaoMenu.Selfdraw():

                return True

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

#Esta função verifica a possibilidade de mudança de uma gema(somente quando uma cadeira puder ser formada)
#(O método utilizado é um pouco confuso de primeira, possívelmente não muito confiável mas foi o que eu consegui pensar pra encaixar no resto do código sem copiar de outro lugar)
def SeeAll(PlanesMt):

    #Verificando os lados(direita e esquerda)
    for SeeL in range(6):
        for SeeC in range(3):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL][SeeC + 2].imagename == PlanesMt[SeeL][SeeC + 3].imagename:
                PlanesMt[SeeL][SeeC].setmudavelx(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelx(False)
        for SeeC in range(5, 2, -1):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL][SeeC - 2].imagename == PlanesMt[SeeL][SeeC - 3].imagename:
                PlanesMt[SeeL][SeeC].setmudavelx(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelx(False)

    #Verificando as colunas(acima e abaixo)
    for SeeL in range(3):
        for SeeC in range(6):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL + 2][SeeC].imagename == PlanesMt[SeeL + 3][SeeC].imagename:
                PlanesMt[SeeL][SeeC].setmudavely(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavely(False)
    for SeeL in range(5, 2, -1):
        for SeeC in range(6):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 2][SeeC].imagename == PlanesMt[SeeL - 3][SeeC].imagename:
                PlanesMt[SeeL][SeeC].setmudavely2(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavely2(False)


    #Verificando entre duas gemas(se uma gema está entre duas iguais na outra linha)
    for SeeL in range(1, 6):
        for SeeC in range(5):
                if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC + 1].imagename == PlanesMt[SeeL - 1][SeeC - 1].imagename:
                    PlanesMt[SeeL][SeeC].setmudavelxy(True)
                else:
                    PlanesMt[SeeL][SeeC].setmudavelxy(False)
    for SeeL in range(4):
        for SeeC in range(1, 5):
                if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL + 1][SeeC + 1].imagename == PlanesMt[SeeL + 1][SeeC - 1].imagename:
                    PlanesMt[SeeL][SeeC].setmudavelxy2(True)
                else:
                    PlanesMt[SeeL][SeeC].setmudavelxy2(False)

    #Verificando ao lado de duas gemas na outra linha:           
    for SeeL in range(1, 6):
        for SeeC in range(5, 1, -1):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC - 1].imagename == PlanesMt[SeeL - 1][SeeC - 2].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy5(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy5(False)
    for SeeL in range(1, 6):
        for SeeC in range(4):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC + 1].imagename == PlanesMt[SeeL - 1][SeeC + 2].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy4(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy4(False)
    for SeeL in range(5):
        for SeeC in range(5, 1, -1):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL + 1][SeeC - 1].imagename == PlanesMt[SeeL + 1][SeeC - 2].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy6(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy6(False)
    for SeeL in range(5):
        for SeeC in range(4):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL + 1][SeeC + 1].imagename == PlanesMt[SeeL + 1][SeeC + 2].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy3(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy3(False)          

    #Verificando abaixo ou acima de duas gemas na outra coluna:  
    for SeeL in range(1, 6):
        for SeeC in range(5):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC + 1].imagename == PlanesMt[SeeL - 2][SeeC + 1].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy7(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy7(False)
    for SeeL in range(4):
        for SeeC in range(5):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL + 1][SeeC + 1].imagename == PlanesMt[SeeL + 2][SeeC + 1].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy10(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy10(False)
    for SeeL in range(1, 6):
        for SeeC in range(5, 1, -1):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC - 1].imagename == PlanesMt[SeeL - 2][SeeC - 1].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy9(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy9(False)
    for SeeL in range(4):
        for SeeC in range(5, 0, -1):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL + 1][SeeC - 1].imagename == PlanesMt[SeeL + 2][SeeC - 1].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy11(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy11(False)

    #Verificando entre duas gemas na outra coluna:
    for SeeL in range(1, 5):
        for SeeC in range(5):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC + 1].imagename == PlanesMt[SeeL + 1][SeeC + 1].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy8(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy8(False)
    for SeeL in range(1, 5):
        for SeeC in range(5, 0, -1):
            if PlanesMt[SeeL][SeeC].imagename == PlanesMt[SeeL - 1][SeeC - 1].imagename == PlanesMt[SeeL + 1][SeeC - 1].imagename:
                PlanesMt[SeeL][SeeC].setmudavelxy12(True)
            else:
                PlanesMt[SeeL][SeeC].setmudavelxy12(False)
            
#Esta função verifica conjuntos de gemas iguais para retira-las do tabuleiro e contar os pontos resultantes dos conjuntos
def Match(PlanesMt):

    Stream = 0

    for VerL in range(6):
        for Vercld in range(4):
            if PlanesMt[VerL][Vercld].imagename == PlanesMt[VerL][Vercld + 1].imagename == PlanesMt[VerL][Vercld + 2].imagename:
                if Vercld < 2 and PlanesMt[VerL][Vercld + 4].imagename == PlanesMt[VerL][Vercld + 3].imagename == PlanesMt[VerL][Vercld + 2].imagename:

                    PlanesMt[VerL][Vercld + 4].Changeimage('Empty.png')

                    Stream += 3

                if Vercld < 3 and PlanesMt[VerL][Vercld + 3].imagename == PlanesMt[VerL][Vercld + 2].imagename:

                    PlanesMt[VerL][Vercld + 3].Changeimage('Empty.png')

                    Stream += 3

                PlanesMt[VerL][Vercld].Changeimage('Empty.png')
                PlanesMt[VerL][Vercld + 1].Changeimage('Empty.png')
                PlanesMt[VerL][Vercld + 2].Changeimage('Empty.png')

                Stream += 3

    PlanesMt[VerL][Vercld].Points()

    for Verc in range(4):
        for Verld in range(6):
            if PlanesMt[Verc][Verld].imagename == PlanesMt[Verc + 1][Verld].imagename == PlanesMt[Verc + 2][Verld].imagename:
                if Verc < 2 and PlanesMt[Verc + 4][Verld].imagename == PlanesMt[Verc + 3][Verld].imagename == PlanesMt[Verc + 2][Verld].imagename:

                    PlanesMt[Verc + 4][Verld].Changeimage('Empty.png')

                    Stream += 3

                if Verc < 3 and PlanesMt[Verc + 3][Verld].imagename == PlanesMt[Verc + 2][Verld].imagename == PlanesMt[Verc + 1][Verld].imagename:

                    PlanesMt[Verc + 3][Verld].Changeimage('Empty.png')

                    Stream += 3

                PlanesMt[Verc][Verld].Changeimage('Empty.png')
                PlanesMt[Verc + 1][Verld ].Changeimage('Empty.png')
                PlanesMt[Verc + 2][Verld ].Changeimage('Empty.png')

                Stream += 3
                
    PlanesMt[Verc][Verld].Points()

    return Stream * PlanesMt[Verc][Verld].Getv()

#Este é o setor principal, contém o mainloop e as chamadas de outras funções:
def MainSector():

    pygame.init()

    Running = True

    #Enquanto o jogador não realizar um movimento válido os pontos não são contados para que o jogo se inicie realmente com 0 pontos
    Player_started = False
    
    ScreenDimensions = pygame.display.get_desktop_sizes()[0]

    Pontos = 0

    SectorScreen = pygame.display.set_mode(ScreenDimensions)

    gfont = pygame.font.SysFont('None', int(3 / 100 * ScreenDimensions[0]))

    #Referências de aviões disponíveis
    Planes = ['redplane.png', 'greenplane.png', 'yellowplane.png', 'blueplane.png', 'purpleplane.png', 'cyanplane.png']

    #Classe utilizada para os botões do mainloop
    class Botao:

            def __init__(self, x, y, imagem):

                self.imagename = imagem
                self.imagem = pygame.image.load(imagem)
                self.imagem = pygame.transform.scale(self.imagem, ((4/100 * ScreenDimensions[0]), (4/100 * ScreenDimensions[1])))
                self.rect = self.imagem.get_rect()
                self.rect.center = (x, y)
                self.BotaoPressionado = False

            def Selfdraw(self):

                Mouse_pos = pygame.mouse.get_pos()

                SectorScreen.blit(self.imagem, (self.rect.x, self.rect.y))

                if self.rect.collidepoint(Mouse_pos):

                    self.imagem = pygame.transform.scale(self.imagem, ((5/100 * ScreenDimensions[0]), (5/100 * ScreenDimensions[1])))

                    if pygame.mouse.get_pressed()[0] == 1:
                        self.BotaoPressionado = True
                else:
                    self.imagem = pygame.transform.scale(pygame.image.load(self.imagename), ((4/100 * ScreenDimensions[0]), (4/100 * ScreenDimensions[1])))

            def Status(self):
                return self.BotaoPressionado
            def Press(self, presser):
                self.BotaoPressionado = presser

    #Classe para criar e manipular os aviões
        #Os aviões são dimensionados de acordo com o tamanho da tela, assim como os botões
            #A classe tem muitos elementos por conta das verificações
    class plane:

        def __init__(self, x, y, imagem):

            self.imagename = imagem
            self.x = x
            self.y = y
            self.imagem = pygame.image.load(imagem)
            self.imagem = pygame.transform.scale(self.imagem, ((6/100 * ScreenDimensions[0]), (6/100 * ScreenDimensions[1])))
            self.rect = self.imagem.get_rect()
            self.rect.center = self.x, self.y
            self.selectable = True
            self.selected = False
            self.value = 0
            self.Hintable = False
            self.mudavelx = False
            self.mudavely = False
            self.mudavely2 = False
            self.mudavelxey = False
            self.mudavelxey2 = False
            self.mudavelxey3 = False
            self.mudavelxey4 = False
            self.mudavelxey5 = False
            self.mudavelxey6 = False
            self.mudavelxey7 = False
            self.mudavelxey8 = False
            self.mudavelxey9 = False
            self.mudavelxey10 = False
            self.mudavelxey11 = False
            self.mudavelxey12 = False


        def Selfdraw(self):

            Mouse_pos = pygame.mouse.get_pos()
                
            SectorScreen.blit(self.imagem, (self.rect.x, self.rect.y))

            if self.rect.collidepoint(Mouse_pos):
                self.imagem = pygame.transform.scale(self.imagem, ((8/100 * ScreenDimensions[0]), (8/100 * ScreenDimensions[1])))
    
                if pygame.mouse.get_pressed()[0] == 1 and self.selected == False:
                    self.selected = True
            else:
                self.imagem = pygame.transform.scale(pygame.image.load(self.imagename), ((6/100 * ScreenDimensions[0]), (6/100 * ScreenDimensions[1])))

        def Status(self):
            return self.selected   
        def Selectable(self):
            return self.selectable
        def SetSelectable(self):
            self.selectable = False           
        def SetChanged(self):
            self.selected = False  
        def Changeimage(self, newimg):
            self.imagename = newimg
        def Getv(self):
            return self.value
        def Points(self):
            if self.imagename == 'greenplane.png':
                self.value = 20
            elif self.imagename == 'yellowplane.png':
                self.value = 26
            elif self.imagename == 'blueplane.png':
                self.value = 32
            elif self.imagename == 'redplane.png':
                self.value = 38
            elif self.imagename == 'purpleplane.png':
                self.value = 44
            elif self.imagename == 'cyanplane.png':
                self.value = 50
        def GHintable(self):
            return self.Hintable
        def StHintable(self, Hintabler):
            self.Hintable = Hintabler

        def mudavelxs(self):
            return self.mudavelx
        def mudavelys(self):
            return self.mudavely 
        def mudavelys2(self):
            return self.mudavely2
        def mudavelyx(self):
            return self.mudavelxey
        def mudavelyx2(self):
            return self.mudavelxey2
        def mudavelyx3(self):
            return self.mudavelxey3
        def mudavelyx4(self):
            return self.mudavelxey4
        def mudavelyx5(self):
            return self.mudavelxey5
        def mudavelyx6(self):
            return self.mudavelxey6
        def mudavelyx7(self):
            return self.mudavelxey7
        def mudavelyx8(self):
            return self.mudavelxey8
        def mudavelyx9(self):
            return self.mudavelxey9
        def mudavelyx10(self):
            return self.mudavelxey10
        def mudavelyx11(self):
            return self.mudavelxey11
        def mudavelyx12(self):
            return self.mudavelxey12
        

        def setmudavelx(self, mutable):
            self.mudavelx = mutable
        def setmudavely(self, mutable):
            self.mudavely = mutable
        def setmudavely2(self, mutable):
            self.mudavely2 = mutable
        def setmudavelxy(self, mutable):
            self.mudavelxey = mutable
        def setmudavelxy2(self, mutable):
            self.mudavelxey2 = mutable
        def setmudavelxy3(self, mutable):
            self.mudavelxey3 = mutable
        def setmudavelxy4(self, mutable):
            self.mudavelxey4 = mutable
        def setmudavelxy5(self, mutable):
            self.mudavelxey5 = mutable
        def setmudavelxy6(self, mutable):
            self.mudavelxey6 = mutable
        def setmudavelxy7(self, mutable):
            self.mudavelxey7 = mutable
        def setmudavelxy8(self, mutable):
            self.mudavelxey8 = mutable
        def setmudavelxy9(self, mutable):
            self.mudavelxey9 = mutable
        def setmudavelxy10(self, mutable):
            self.mudavelxey10 = mutable
        def setmudavelxy11(self, mutable):
            self.mudavelxey11 = mutable
        def setmudavelxy12(self, mutable):
            self.mudavelxey12 = mutable

    #Criação da matriz com os aviões randomizados
    xadc = 45

    PlanesMt = list()

    for Line in range(6):

        yadc = 0
        planelist = list()

        for Column in range(6):

            Plane = plane((ScreenDimensions[0] - (91.6 / 100 * ScreenDimensions[0] - yadc)), (ScreenDimensions[1] - (90/100 * ScreenDimensions[1] - xadc)), random.choice(Planes))
            planelist.append(Plane)

            yadc += (10.2/100) * ScreenDimensions[0]
            
        PlanesMt.append(planelist)

        xadc += (14.2/100) * ScreenDimensions[1]

        SectorImage = pygame.image.load('Squares.png')
        SectorImage = pygame.transform.scale(SectorImage, (ScreenDimensions))

        Exitbutton = Botao((ScreenDimensions[0] - (3 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (97 / 100 * ScreenDimensions[1])), 'Exitbutton.png')
        HintButton = Botao((ScreenDimensions[0] - (50 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (70 / 100 * ScreenDimensions[1])), 'BotaoDica.png')

    #Estas listas fazem parte do sistema de mudança entre dois aviões
    Selection = []

    Loc1 = []
    loc2 = []

    #Quantidade de dicas por partida
    Hints = 4

    while Running:

        clock = pygame.time.Clock()
        clock.tick(60)

        SectorScreen.blit(SectorImage, (0, 0))

        #Se o nome do objeto for vazio randomiza-se um outro nome para o construtor
        for Line in range(6):
            for Column in range(6):
                if Line == 0 and PlanesMt[Line][Column].imagename == 'Empty.png':

                    PlanesMt[Line][Column].imagename = random.choice(Planes)

                elif Line > 0 and PlanesMt[Line][Column].imagename == 'Empty.png':

                    PlanesMt[Line][Column].imagename = PlanesMt[Line - 1][Column].imagename

                    PlanesMt[Line - 1][Column].imagename = 'Empty.png'

                PlanesMt[Line][Column].Selfdraw()

                #Se um objeto retornar status como verdadeiro significa que foi selecionado pelo usuário, sendo colocado na lista 'Selection' se passar na verificação a seguir
                if PlanesMt[Line][Column].Status() == True:
                    if len(Selection) == 0:
                        #Verifica-se a possibilidade de formação de uma cadeia para prosseguir, se o objeto selecionado não pode formar uma cadeia ele não continua para a seleção
                        if PlanesMt[Line][Column].mudavelxs() or PlanesMt[Line][Column].mudavelys() or PlanesMt[Line][Column].mudavelyx() or PlanesMt[Line][Column].mudavelyx2() or PlanesMt[Line][Column].mudavelyx3() or PlanesMt[Line][Column].mudavelyx4() or PlanesMt[Line][Column].mudavelyx5() or PlanesMt[Line][Column].mudavelyx6() or PlanesMt[Line][Column].mudavelyx7() or PlanesMt[Line][Column].mudavelyx8() or PlanesMt[Line][Column].mudavelyx9() or PlanesMt[Line][Column].mudavelyx10() or PlanesMt[Line][Column].mudavelyx11() or PlanesMt[Line][Column].mudavelyx12() or PlanesMt[Line][Column].mudavelys2():
                            Selection.append(PlanesMt[Line][Column])

                            Loc1.append(Line)
                            Loc1.append(Column)

                        else:
                             PlanesMt[Line][Column].StHintable(False)

                    elif len(Selection) == 1:
                        if PlanesMt[Line][Column] != Selection[0]:

                            Selection.append(PlanesMt[Line][Column])

                            loc2.append(Line)
                            loc2.append(Column)
                PlanesMt[Line][Column].SetChanged()

                if len(Selection) == 2:
                    if loc2[1] == Loc1[1] + 1 or loc2[1] == Loc1[1] - 1:
                        if loc2[0] == Loc1[0]:

                            image1 = PlanesMt[Loc1[0]][Loc1[1]].imagename
                            
                            image2 = PlanesMt[loc2[0]][loc2[1]].imagename

                            PlanesMt[Loc1[0]][Loc1[1]].Changeimage(image2)
                            PlanesMt[loc2[0]][loc2[1]].Changeimage(image1)

                            PlanesMt[Loc1[0]][Loc1[1]].SetChanged()
                            PlanesMt[loc2[0]][loc2[1]].SetChanged()

                            pygame.mouse.set_pos(((ScreenDimensions[0]/2), (ScreenDimensions[1]/2)))

                    elif loc2[0] == Loc1[0] + 1 or loc2[0] == Loc1[0] - 1:
                        if loc2[1] == Loc1[1]:

                            image1 = PlanesMt[Loc1[0]][Loc1[1]].imagename
                            
                            image2 = PlanesMt[loc2[0]][loc2[1]].imagename

                            PlanesMt[Loc1[0]][Loc1[1]].Changeimage(image2)
                            PlanesMt[loc2[0]][loc2[1]].Changeimage(image1)

                            PlanesMt[Loc1[0]][Loc1[1]].SetChanged()
                            PlanesMt[loc2[0]][loc2[1]].SetChanged()

                            pygame.mouse.set_pos(((ScreenDimensions[0]/2), (ScreenDimensions[1]/2)))

                    #Após o processo, as listas são limpas pois a operação de troca teve sucesso, os pontos agora podem ser contados porque o usuário manipulou as gemas formando um conjunto 
                    if HintButton.Status() and Hints != 0:
                        Hints -= 1
                    HintButton.Press(False)
                    Selection.clear()
                    Loc1.clear()
                    loc2.clear()
                    Player_started = True

                if len(Selection) > 0:

                    pygame.font.init()

                    text_ = gfont.render('Avião selecionado:', True, (50, 20, 180))

                    SectorScreen.blit(text_, ((ScreenDimensions[0] - (55 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (90 / 100 * ScreenDimensions[1]))))

                    Sell = Botao((ScreenDimensions[0] - (15 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (88 / 100 * ScreenDimensions[1])), Selection[-1].imagename)

                    Sell.Selfdraw()

        SeeAll(PlanesMt)

        #Se o botão de saida do mainloop for pressionado retorna-se ao menu
        Exitbutton.Selfdraw()
        if Exitbutton.Status():

            Running = False

            import PBL_2_Main
        
        HintButton.Selfdraw()
        if HintButton.Status():
            if Hints > 0:
                LocHt = []

                for hintl in range(6):
                    for  hintc in range(6):
                        if PlanesMt[hintl][hintc].mudavelxs() or PlanesMt[hintl][hintc].mudavelys() or PlanesMt[hintl][hintc].mudavelyx() or PlanesMt[hintl][hintc].mudavelyx2() or PlanesMt[hintl][hintc].mudavelyx3() or PlanesMt[hintl][hintc].mudavelyx4() or PlanesMt[hintl][hintc].mudavelyx5() or PlanesMt[hintl][hintc].mudavelyx6() or PlanesMt[hintl][hintc].mudavelyx7() or PlanesMt[hintl][hintc].mudavelyx8() or PlanesMt[hintl][hintc].mudavelyx9() or PlanesMt[hintl][hintc].mudavelyx10() or PlanesMt[hintl][hintc].mudavelyx11() or PlanesMt[hintl][hintc].mudavelyx12() or PlanesMt[hintl][hintc].mudavelys2():
                            PlanesMt[hintl][hintc].StHintable(True)
                        else:
                            PlanesMt[hintl][hintc].StHintable(False)
                for hintl in range(6):
                    for  hintc in range(6):
                        if PlanesMt[hintl][hintc].GHintable():
                            LocHt.append(hintl)
                            LocHt.append(hintc)
                            text1 = gfont.render(f'Linha: {LocHt[0]}', True, (50, 20, 180))
                            text2 = gfont.render(f'Coluna: {LocHt[1]}', True, (50, 20, 180))
                            SectorScreen.blit(text1, ((ScreenDimensions[0] - (55 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (50 / 100 * ScreenDimensions[1]))))
                            SectorScreen.blit(text2, ((ScreenDimensions[0] - (55 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (45 / 100 * ScreenDimensions[1]))))
                            Seeepn = Botao((ScreenDimensions[0] - (47 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (56 / 100 * ScreenDimensions[1])), PlanesMt[LocHt[0]][LocHt[1]].imagename)
                            Seeepn.Selfdraw()
                if len(LocHt) == 0:
                    
                    with open('Historico.txt', 'a') as file:
                        pass

                    with open('Historico.txt', 'r') as file:
                        primeira_linha = file.readline()
                        if primeira_linha == '':
                            primeira_linha = 0
                        pontos = int(primeira_linha)
                        segunda_linha = file.readline(1)
                        if segunda_linha == '':
                            segunda_linha = 0
                        vitorias = int(segunda_linha)
                        terceira_linha = file.readline(2)
                        if terceira_linha == '':
                            terceira_linha = 0
                        derrotas = int(terceira_linha)

                        pontos_passados = Pontos
                        novo_total_pts = pontos + pontos_passados
                        novo_total_vit = vitorias
                        novo_total_der = derrotas + 1

                        with open('Historico.txt', 'r+') as file:
                            file.seek(0)  
                            file.write(str(novo_total_pts) + '\n')  
                            file.write(str(novo_total_vit) + '\n') 
                            file.write(str(novo_total_der) + '\n') 
                        
                    GameOver()

                    Running = False

                LocHt.clear()
            
        if Player_started == True:
            Pontos += Match(PlanesMt)

        elif Player_started == False:
            Match(PlanesMt)

        text = gfont.render(f'Pontos: {Pontos}', True, (50, 20, 180))

        SectorScreen.blit(text, ((ScreenDimensions[0] - (55 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (85 / 100 * ScreenDimensions[1]))))

        texth = gfont.render(f'Dicas restantes: {Hints}', True, (50, 20, 180))

        SectorScreen.blit(texth, ((ScreenDimensions[0] - (55 / 100 * ScreenDimensions[1])), (ScreenDimensions[1] - (65 / 100 * ScreenDimensions[1]))))

        if EndState(Pontos):

            Running = False
    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

        pygame.display.update()

