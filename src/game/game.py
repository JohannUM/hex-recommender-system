import sys
import pygame

from game.board import Board
from game.GUI import GUI
from agent.agent import Agent

pygame.init()
class Game:
    def __init__(self, board_size:int=11, agent_type='hybrid'):
        self.gui = GUI(board_size)
        self.board = Board(board_size)
        self.agent = Agent(agent_type)
        
    
    def playGame(self):
        run = True
        player = 1
        self.gui.drawTurn(player)
        next_move = (0, 0)
        show_hint = False
        while run:
            self.gui.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP: # When clicked to the following
                    show_hint = False
                    mouse_location = pygame.mouse.get_pos()
                    row, col = self.gui.convert_mouse(mouse_location)

                    if not self.board.contains_location((row, col)):
                        print('HERE NOT ON BOARD')
                        continue

                    if not self.board.check_position_state((row, col)) == 0:
                        print('HERE OCCUPIED')
                        continue

                    self.board.update_position_state((row, col), player)
                    self.gui.update_board_colouring(self.board.get_board_states())

                    winner = self.board.check_winner()
                    if not winner == 0:
                        run = False
                        continue
                    
                    player = 3-player
                    self.gui.drawTurn(player)
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    next_move = self.agent.find_move(player, self.board)
                    show_hint = True


            
            self.gui.drawBoard(reccomended_move=next_move, show_reccomended_move=show_hint) # Add the MCTS predicted move here!
            self.gui.getHexagonHover()
            pygame.display.update()
