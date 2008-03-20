import pygame
from pygame.locals import *

class KeyboardRemember():
    """ Simple class to provide more responsive keyboard input.
    This allows you to hold down a key and then press another one. When you release
    the second key, the first will still be held down.
    """
    def __init__(self, applicable):
        self.keysdown = []*len(applicable)
        self.applicable = applicable

    def update(self, event):
        """ We need the pygame.event to update ourself with. """
        if event.type is KEYDOWN:
            if self._isDirection(event.key):
                self._add(event.key)
        elif event.type is KEYUP:
            if self._isDirection(event.key):
                self._remove(event.key)

    def _isDirection(self, key):
        """ Is it a key direction? """
        return key in self.applicable

    def _add(self, key):
        """ Add to our list of keys. """
        assert len(self.keysdown) < len(self.applicable)   ## we shouldn't have more than all
        self.keysdown.append(key)       ##  directions when we're adding

    def _remove(self, key):
        """ Remove from the list of directions. """
        try:
            self.keysdown.remove(key)
        except:
            print "Strange, the %i key wasn't there." % key

    def getCurrent(self):
        """ Get the current key pressed. If no direction key pressed, then None"""
        try:
            last = len(self.keysdown)-1
            return self.keysdown[last]   # return the last element
        except:
            # this will happen if no key is pressed
            return None
