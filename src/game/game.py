import sys
import pygame

from game.board import Board
from game.GUI import GUI

pygame.init()
class Game:
    def __init__(self, board_size:int=11):
        self.gui = GUI(board_size)
        self.board = Board(board_size)

        self.hex_hover = None
    
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_location = pygame.mouse.get_pos()
                self.move(mouse_location)
    
    def playGame(self):
        self.gui.drawBoard()
        self.hex_hover = self.gui.getHexagonHover()

        pygame.display.update()
        self.gui.clock.tick(30)
        self.handleEvents()

