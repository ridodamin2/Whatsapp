from time import time
import pygame
pygame.init()


WINSIZE = (385,715)
WIN = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption("WhatsApp")
font18 = pygame.font.SysFont("",18)
font32 = pygame.font.SysFont("",32)
logo = pygame.image.load("res/logo.jpg")
DARK_COLOR = (21,28,36)
DARK_COLOR_TOP = (38,45,53)

class App:
    def __init__(self,win,fps=60):
        self.win = win
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.run = True

    def home(self):
        top_surf = pygame.surface.Surface((WINSIZE[0],WINSIZE[1]*0.16),DARK_COLOR_TOP)
        chat_surf = pygame.surface.Surface((WINSIZE[0],1000),DARK_COLOR_TOP)


    def splash(self):
        first = time()
        text1 = font18.render("from",1,(128,128,128))
        text2 = font32.render("RIDO",1,(248,248,248))
        self.win.fill(DARK_COLOR)
        self.win.blit(logo,((WINSIZE[0]-logo.get_width())/2,WINSIZE[1]*0.35))
        self.win.blit(text1,((WINSIZE[0]-text1.get_width())//2,WINSIZE[1]*0.9))
        self.win.blit(text2,((WINSIZE[0]-text2.get_width())//2,WINSIZE[1]*0.93))
        pygame.display.update()
        while self.run and time()-first<100:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run=False

    def start(self):
        self.splash()
        self.home()


if __name__ == "__main__":
    app = App(WIN)
    app.start()
    pygame.quit()
