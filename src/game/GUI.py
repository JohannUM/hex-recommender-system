import pygame
from pygame import gfxdraw, time
from math import cos, sin, pi, radians


class GUI:
    def __init__(self, board_size:int):
        self.board_size = board_size

        self.clock = time.Clock()
        self.hex_radius = 20
        self.x_offset = 60
        self.y_offset = 60
        self.text_offset = 45

        self.screen = pygame.display.set_mode((
            self.x_offset + (2 * self.hex_radius) * self.board_size + self.hex_radius * self.board_size,
            round(self.y_offset + (1.75 * self.hex_radius) * self.board_size)
        ))

        # COLOURS
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.DARK_GRAY = (50, 50, 50)
        self.GOLD = (255, 215, 0)

        # PLAYERS
        self.RED_PLAYER = 1
        self.BLUE_PLAYER = 2

        self.screen.fill(self.BLACK)
        self.fonts = pygame.font.SysFont('Sans', 20)

        self.hex_lookup = {}
        self.rects = []
        self.colour = [self.WHITE] * (self.board_size ** 2)
        self.node = None
        self.clicked = None
    
    def update_board_colouring(self, states:list[int]):
        for index, state in enumerate(states):
            if state == 1:
                self.colour[index] = self.RED
            elif state == 2:
                self.colour[index] = self.BLUE

    
    def drawHexagon(self, canvas:object, colour:tuple, position:tuple, hexagon:int):
        sides = 6 # Hexagon has 6 sides
        x, y = position
        offset = 3

        self.hex_lookup[hexagon] = [(x + (self.hex_radius + offset) * cos(radians(90) + 2 * pi * i/sides),
                                  y + (self.hex_radius + offset) * sin(radians(90) + 2 * pi * i/sides))
                                  for i in range(sides)]
        
        gfxdraw.aapolygon(canvas, self.hex_lookup[hexagon], colour)

        gfxdraw.filled_polygon(canvas,
                               [(x + self.hex_radius * cos(radians(90) + 2 * pi * i/sides),
                                 y + self.hex_radius * sin(radians(90) + 2 * pi * i/sides))
                                for i in range(sides)], self.colour[hexagon])
        
        gfxdraw.aapolygon(canvas,
                          [(x + self.hex_radius * cos(radians(90) + 2 * pi * i/sides),
                            y + self.hex_radius * sin(radians(90) + 2 * pi * i/sides))
                            for i in range(sides)], self.BLACK)
        
        rect = pygame.draw.rect(canvas,
                                self.colour[hexagon],
                                pygame.Rect(x - self.hex_radius + offset, y - (self.hex_radius / 2),
                                            (self.hex_radius * 2) - (2 * offset), self.hex_radius))
        self.rects.append(rect)

        bounding_box_offset = [0, 3]

        # TOP
        if 0 < hexagon < self.board_size: # Checking if hexagon is in top row!
            points = ([self.hex_lookup[hexagon - 1][3][i] - bounding_box_offset[i] for i in range(2)],
                      [self.hex_lookup[hexagon - 1][4][i] - bounding_box_offset[i] for i in range(2)],
                      [self.hex_lookup[hexagon][3][i] - bounding_box_offset[i] for i in range(2)])
            gfxdraw.filled_polygon(canvas,
                                   points,
                                   self.RED)
            gfxdraw.aapolygon(canvas,
                              points,
                              self.RED)
        
        # BOTTOM
        if self.board_size ** 2 - self.board_size < hexagon < self.board_size ** 2:
            points = ([self.hex_lookup[hexagon - 1][0][i] + bounding_box_offset[i] for i in range(2)],
                      [self.hex_lookup[hexagon - 1][5][i] + bounding_box_offset[i] for i in range(2)],
                      [self.hex_lookup[hexagon][0][i] + bounding_box_offset[i] for i in range(2)])
            gfxdraw.filled_polygon(canvas,
                                   points,
                                   self.RED)
            gfxdraw.aapolygon(canvas,
                              points,
                              self.RED)
        
        bounding_box_offset = [3, -3]
        # LEFT
        if hexagon % self.board_size == 0:
            if hexagon >= self.board_size:
                points = ([self.hex_lookup[hexagon - self.board_size][1][i] - bounding_box_offset[i] for i in range(2)],
                          [self.hex_lookup[hexagon - self.board_size][0][i] - bounding_box_offset[i] for i in range(2)],
                          [self.hex_lookup[hexagon][1][i] - bounding_box_offset[i] for i in range(2)])
                gfxdraw.filled_polygon(canvas,
                                       points,
                                       self.BLUE)
                gfxdraw.aapolygon(canvas,
                                  points,
                                  self.BLUE)
        
        # RIGHT
        if (hexagon + 1) % self.board_size == 0:
            if hexagon > self.board_size:
                points = ([self.hex_lookup[hexagon - self.board_size][4][i] + bounding_box_offset[i] for i in range(2)],
                          [self.hex_lookup[hexagon - self.board_size][5][i] + bounding_box_offset[i] for i in range(2)],
                          [self.hex_lookup[hexagon][4][i] + bounding_box_offset[i] for i in range(2)])
                gfxdraw.filled_polygon(canvas,
                                       points,
                                       self.BLUE)
                gfxdraw.aapolygon(canvas,
                                  points,
                                  self.BLUE)
        
    def drawText(self):
        letters = list(map(chr, range(97, 123)))

        for i in range(self.board_size):
            # COLUMNS
            text_col = self.fonts.render(letters[i].upper(), True, self.WHITE, self.BLACK)
            text_col_rect = text_col.get_rect()
            text_col_rect.center = (
                self.x_offset + (2 * self.hex_radius) * i, self.text_offset/2
            )
            self.screen.blit(text_col, text_col_rect)

            # ROWS
            text_row = self.fonts.render(str(i+1), True, self.WHITE, self.BLACK)
            text_row_rect = text_row.get_rect()
            text_row_rect.center = (
                (self.text_offset/4 + self.hex_radius * i, self.y_offset + (1.75 * self.hex_radius) * i)
            )
            self.screen.blit(text_row, text_row_rect)
    
    def drawTurn(self, player:int):
        text = ''
        if player == 1:
            text = self.fonts.render('REDs TURN', True, self.RED, self.BLACK)
        else:
            text = self.fonts.render('BLUE TURN', True, self.BLUE, self.BLACK)
        
        text_rect = text.get_rect()
        text_rect.center = (620, 20)

        self.screen.blit(text, text_rect)
        
    def drawBoard(self, reccomended_move:tuple=None, show_reccomended_move:bool=False):
        hexagon_counter = 0
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.drawHexagon(self.screen, self.BLACK, self.getCoords(row, col), hexagon_counter)
                hexagon_counter += 1
        self.drawText()

        if show_reccomended_move:
            x, y = self.getCoords(reccomended_move[0], reccomended_move[1])
            gfxdraw.filled_polygon(self.screen,
                                   [(x + self.hex_radius * cos(radians(90) + 2 * pi * i/6),
                                    y + self.hex_radius * sin(radians(90) + 2 * pi * i/6))
                                    for i in range(6)], self.GOLD)
    
    def getCoords(self, row:int, col:int):
        x = self.x_offset + (2 * self.hex_radius) * col + self.hex_radius * row
        y = self.y_offset + (1.75 * self.hex_radius) * row
        return x, y
    
    def convert_mouse(self, mouse_location):
        for i, rect in enumerate(self.rects):
            if rect.collidepoint(mouse_location):
                self.clicked = i
                break
        row, col = -1, -1
        if self.clicked is not None:
            row, col = int(self.clicked / self.board_size), self.clicked % self.board_size
        
        return row, col
    
    def getHexagonHover(self):
        mouse_location = pygame.mouse.get_pos()
        for i, rect in enumerate(self.rects):
            if rect.collidepoint(mouse_location):
                self.node = i
                break
        
        if self.node is not None:
            row, col = int(self.node / self.board_size), self.node % self.board_size
            self.drawHexagon(self.screen, self.GREEN, self.getCoords(row, col), self.node)
    
    def get_colours(self):
        return self.colour

    def drawWinner(self, winner:int):
        self.screen.fill(self.BLACK)
        self.fonts = pygame.font.SysFont('Sans', 48)

        text = ''
        if winner == 1:
            text = self.fonts.render('RED HAS WON!', True, self.RED, self.BLACK)
        else:
            text = self.fonts.render('BLUE HAS WON', True, self.BLUE, self.BLACK)
        
        text_rect = text.get_rect()
        text_rect.center = (self.screen.get_width()//2, self.screen.get_height()//2)

        self.screen.blit(text, text_rect)
