import pygame
from pygame.locals import *
"""
Game of Life

Using the Agent, Environment, Rules model

Each cell will be defined in an environment matrix

Each live cell will be defined as an Agent


Every agent is visited in the list of agents and told to run against the defined rules based on it's environment

The changes are buffered until all changes are collected from all agents, then all changes are applied in the sequence they were collected

Changes are a result from the agents interacting with the rules

RULES:
based off of the definitions in "Growing Artificial Societies"

agent-agent

environment-environment


environment-agent


TODO






"""

class Agent:
    pass


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1440, 900
        self.bgcolor = 0, 0, 0
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self._running = True

    def pre_loop(self):
        pass
 
    def on_event(self, event):
        
        
        if event.type == pygame.QUIT:
            self._running = False
            

        elif event.type == pygame.MOUSEMOTION:
            print "mouse at (%d, %d)" % event.pos
            self._display_surf.fill( self.bgcolor )
            pygame.draw.circle(self._display_surf, (255,255,255), event.pos, 64, 0)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print "You released the left mouse button at (%d, %d)" % event.pos
            
    def on_loop(self):
        pass
    
    def on_render(self):
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        
        if self.on_init() == False:
            self._running = False
 
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
