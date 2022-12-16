import pygame


class App:
    def __init__(self):
        pygame.init()
        size = self.width, self.height = 701, 701  # screen size
        self.screen = pygame.display.set_mode(size)  # creating screen
        self.clock = pygame.time.Clock()  # creating clock
        self.fps = 60  # setting fps
        self.all_sprites = pygame.sprite.Group()  # adding all sprites to one group
        self.running = True  # allowing program to run

    def main(self):
        while self.running:  # main running cycle
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # shutting down program if we close main window
                    self.running = False  # shutting program down

            self.screen.fill((0, 0, 0))  # filling screen with black
            self.all_sprites.draw(self.screen)  # drawing all sprites on the screen
            self.all_sprites.update()  # updating all sprites
            pygame.display.flip()  # flipping screen
            self.clock.tick(self.fps)  # setting clock tick to fps value


if __name__ == '__main__':
    app = App()
    app.main()
