from pygame import *
from pygame.locals import *

class BaseObject():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.surface = Surface((60, 60))
        self.AABB = Rect(x, y, 60, 60)
        self.color = color
    def getAABB(self):
        return self.AABB
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

class Note(BaseObject):
    def __init__(self, x, y, color):
        BaseObject.__init__(x, y, color)
        self.isAlive = False
    def getAlive(self):
        return self.isAlive
    def setAlive(self, alive):
        self.isAlive = alive
    def setColor(self, color):
        self.color = color
    def update(self, dt):
        if self.isAlive:
            y -= 0.25 * dt

class NoteManager():
    def __init__(self):
        self.y = 0
        self.Notes = []
        for count in range(0, 13):
            self.Notes.append(Note(0, 0, Color(0, 0, 0)))
    def render(self, screen):
        for note in self.Notes:
            note.render(screen)
    def spawn(self, x, color):
        for note in self.Notes:
            if not note.getAlive():
                note.setX(x)
                note.setColor(color)
                note.setAlive(True)
                return None         
    def update(self, dt):
        for note in self.Notes:
            note.update(dt)           