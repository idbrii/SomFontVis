#! /usr/bin/env python
import pygame
from pygame import locals

class SomVisualizer():
    def __init__(self, som):
        self.som = som
        self.val = 0

    def draw(self, screen):
        self.val += 1
        screen.set_at( (self.val,self.val), (0,0,255) )

class Som():
    def __init__(self):
        pass

    def update(self):
        pass


def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
