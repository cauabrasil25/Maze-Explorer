import sys
from src.Player import Player
from src.Display import Display
from src.Controller import Controller

controller = Controller()

while controller.running:
    controller.input(controller.getEstate())
    controller.update()
    controller.display.MainswitchDisplay(controller.getEstate(), controller.player)

controller.display.ShowEndScreen()