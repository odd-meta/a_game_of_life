#This is the part where i get tired of not having anything that does anything and do this jank cell-style



import pygame
from pygame.locals import *

import random

class Agent:
    pass


class Grid:

	def __init__(self, state = [], max_width = 20, max_height = 20):
		self.state = state
		self.max_width = max_width
		self.max_height = max_height
		if len(state) is 0:
			self.state = self.generate_state()

	def do_step(self):
		new_state = []

		for r in range(0,self.max_width):
			new_state.append([])
			for c in range(0,self.max_height):
				new_state[r].append(None)

		for row_index, row in enumerate(self.state):
			
			for cell_index, cell in enumerate(row):
				adjacent_cells = []
				#TODO: consolidate if statements
				#get top row
				top_left_y = None
				top_left_x = None
				top_y = None
				top_x = None
				top_right_y = None
				top_right_x = None

				#handle top left cell
				if cell_index - 1 < 0:
					top_left_y = self.max_height - 1
				else:
					top_left_y = cell_index - 1

				if row_index - 1 < 0:
					top_left_x = self.max_width -1
				else:
					top_left_x = row_index - 1

				#handle top cell
				top_y = cell_index
				if row_index - 1 < 0:
					top_x = self.max_width - 1
				else:
					top_x = row_index - 1

				#handle top right cell
				if cell_index + 1 >= self.max_height:
					top_right_y = 0
				else:
					top_right_y = cell_index + 1
				if row_index - 1 < 0:
					top_right_x = self.max_width -1
				else:
					top_right_x = row_index - 1


				#get sides

				left_side_y = None
				left_side_x = None
				right_side_y = None
				right_side_x = None

				#FUCKING FUCK TEDIOUS CODE FUCK HOW DID I EVER HAND TYPE THIS INTO A TI-89 GOOD GOD

				if cell_index - 1 < 0:
					left_side_y = self.max_height - 1
				else:
					left_side_y = cell_index - 1
				left_side_x = row_index

				if cell_index + 1 >= self.max_height:
					right_side_y = 0
				else:
					right_side_y = cell_index + 1
				right_side_x = row_index

				#get bottom row
				bottom_left_y = None
				bottom_left_x = None
				bottom_y = None
				bottom_x = None
				bottom_right_y = None
				bottom_right_x = None

				if cell_index - 1 < 0:
					bottom_left_y = self.max_height - 1
				else:
					bottom_left_y = cell_index - 1

				if row_index + 1 >= self.max_width:
					bottom_left_x = 0
				else:
					bottom_left_x = row_index + 1

				bottom_y = cell_index
				if row_index + 1 >= self.max_width:
					bottom_x = 0
				else:
					bottom_x = row_index + 1

				if cell_index + 1 >= self.max_height:
					bottom_right_y = 0
				else:
					bottom_right_y = cell_index + 1

				if row_index + 1 >= self.max_width:
					bottom_right_x = 0
				else:
					bottom_right_x = row_index + 1

				adjacent_cells = [	(top_left_x,top_left_y),
									(top_x,top_y),
									(top_right_x,top_right_y),
									(left_side_x,left_side_y),
									(right_side_x,right_side_y),
									(bottom_left_x,bottom_left_y),
									(bottom_x,bottom_y),
									(bottom_right_x,bottom_right_y)]
				#evaluate our next state based on rules

				#get number of adjacent alive cells
				our_state = int(self.state[row_index][cell_index])
				alive_cells = 0

				for cell in adjacent_cells:
					#if our_state is 1:
					#	print str(self.state[cell[0]][cell[1]])+" "+str( (cell[0],cell[1]) )
					alive_cells += int(self.state[cell[0]][cell[1]])

				
				our_new_state = None
				if our_state is 1:
					if alive_cells > 3:
						our_new_state = 0
					elif alive_cells < 2:
						our_new_state = 0
					elif alive_cells is 2 or alive_cells is 3:
						our_new_state = 1
					else:
						print "i cant even boolean logic"
				else:
					if alive_cells is 3:
						our_new_state = 1
					else:
						our_new_state = 0
				new_state[row_index][cell_index] = our_new_state
				#if our_state is 1:
				#	print alive_cells
				#	print (row_index,cell_index)
					




		#print "*****"
		self.state = new_state



		

	def generate_state(self):
		temp_state = []

		for x in range(0,self.max_height):
			temp_row = []
			for y in range(0,self.max_width):
				temp_row.append( random.randint(0,1) )
			temp_state.append(temp_row)
		return temp_state

	def __str__(self):
		the_string = ""
		for row in self.state:
			the_string += str(row) + "\n"
		return the_string







class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        #TODO: make this work with a non-square grid
        self.size = self.width, self.height = 900, 900
        self.bgcolor = 0, 0, 0
        self.DO_STEP_EVENT = pygame.USEREVENT+1
        self.IS_PAUSED = False
        self.STEP_SPEED = 100
        self.BOARD_DIMENSIONS = (self.width/20,self.height/20)
        self.CELL_SIZE = self.width / (self.width / 20)
 
    def on_init(self):
        pygame.init()
        icon_surface = pygame.image.load("icon.bmp")
        pygame.display.set_icon(icon_surface)
        pygame.display.set_caption("cellular automata makes krishna-jesus smile")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self._running = True

    def pre_loop(self):
        pass
 
    def on_event(self, event):
        
        if event.type == self.DO_STEP_EVENT:
	        self._display_surf.fill( self.bgcolor )
        	self.theGrid.do_step()
	        the_state = self.theGrid.state
	        for row_index, row in enumerate(the_state):
	        	for cell_index, cell in enumerate(row):
	        		if int(the_state[row_index][cell_index]) is 1:
	        			pygame.draw.circle(self._display_surf, (255,255,255), (row_index * self.CELL_SIZE + self.CELL_SIZE/2, cell_index * self.CELL_SIZE + self.CELL_SIZE/2), self.CELL_SIZE/2, self.CELL_SIZE/2/2)
        
        if event.type == pygame.QUIT:
            self._running = False
            
        elif event.type == pygame.MOUSEMOTION:

            pass


        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #print "mouse at (%d, %d)" % event.pos
            #self._display_surf.fill( self.bgcolor )
            #pygame.draw.circle(self._display_surf, (255,255,255), event.pos, 64, 0)
            if self.IS_PAUSED is False:
                self.IS_PAUSED = True
                pygame.time.set_timer(self.DO_STEP_EVENT, 0)
            else:
                pygame.time.set_timer(self.DO_STEP_EVENT, self.STEP_SPEED)
            #print "You released the left mouse button at (%d, %d)" % event.pos
            
    def on_loop(self):
    	pass


    
    def on_render(self):
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.theGrid = Grid(max_width=self.BOARD_DIMENSIONS[0],max_height=self.BOARD_DIMENSIONS[1])
        if self.on_init() == False:
            self._running = False

        pygame.time.set_timer(self.DO_STEP_EVENT, self.STEP_SPEED)
        
        while( self._running ):
            self.pre_loop()
            
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
 
if __name__ == "__main__" :

    theApp = App()
    theApp.on_execute()

