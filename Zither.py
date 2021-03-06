import Input
from BaseObject import BaseObject
from pygame import *
from pygame.locals import *

class StringButton(BaseObject):
    def __init__(self, x, y, button, color):
        BaseObject.__init__(self, x, y, color)
        self.button = button
        self.isDown = False
    def setDown(self, state):
        self.isDown = state
    def getDown(self):
        return self.isDown
    def update(self, dt, input_):
        if (input_.getKeyPressed(self.button)):
            self.isDown = True
            self.surface.fill(Color(255, 255, 255))
        else:
            self.isDown = False
            self.surface.fill(self.color)

class Zither():
    def __init__(self):
        self.smallButtonGroup = []
        self.bigButtonGroup = []
        self.inputBind = [K_z, K_x, K_c, K_v, K_b, K_n, K_m]
        self.numpadBind = [K_COMMA, K_PERIOD, K_SLASH]
        self.colorBind = [Color(255, 0, 0), Color(255, 165, 0), Color(255, 255, 0), Color(0, 255, 0), Color(0, 0, 255), Color(75, 0, 130), Color(238, 130, 238)]
        self.greyBind = [Color(192, 192, 192), Color(169, 169, 169), Color(128, 128, 128), Color(105, 105, 105)]
        for count in range(0, 7):
            self.bigButtonGroup.append(StringButton(((count+1) * 60), 500, self.inputBind[count], self.colorBind[count]))
        self.smallButtonGroup.append(StringButton((9 * 60), 500, self.numpadBind[0], self.greyBind[0]))
        self.smallButtonGroup.append(StringButton((10 * 60), 500, self.numpadBind[1], self.greyBind[1]))
        self.smallButtonGroup.append(StringButton((11 * 60), 500, self.numpadBind[2], self.greyBind[2]))
    def getBigButton(self, index):
        return self.bigButtonGroup[index]
    def getSmallButton(self, index):
        return self.smallButtonGroup[index - 9]
    def getButton(self, index):
        if (index >= 7):
            return self.getSmallButton(index)
        else:
            return self.getBigButton(index)
    def update(self, dt, input_):
        for count in range(0, 7):
            self.bigButtonGroup[count].update(dt, input_)
        for count in range(0, 3):
            self.smallButtonGroup[count].update(dt, input_)
    def render(self, screen):
        for count in range(0, 7):
            self.bigButtonGroup[count].render(screen)
        for count in range(0, 3):
            self.smallButtonGroup[count].render(screen)                       
