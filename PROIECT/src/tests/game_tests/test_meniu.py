import unittest
import pygame

from game.meniu import Meniu
from game.game_session import GameSession
from framework.app import App


class TestMeniu(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('\nTesting Meniu...\n')
    
    @staticmethod
    def Init() -> bool:
        pygame.init()
        return pygame.get_init()


    @staticmethod
    def Quit() -> bool:
        pygame.quit()
        return not pygame.get_init()
    
    def test_ButtonStart(self):
        pygame.init()
        appInstance = App.GetInstance()
        appInstance.currentScene = Meniu()
        buton = appInstance.currentScene.butonStart.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))
        self.assertIsInstance(appInstance.currentScene, GameSession)

    def test_ButtonExit(self):
        pygame.init()
        appInstance = App.GetInstance()
        appInstance.currentScene = Meniu()
        buton = appInstance.currentScene.butonExit.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))
        lastEvent = pygame.event.get()[-1]
        self.assertTrue(lastEvent.type == pygame.QUIT)
    
    def test_ButtonHighScores(self):
        pygame.init()
        appInstance = App.GetInstance()
        appInstance.currentScene = Meniu()
        buton = appInstance.currentScene.butonHighScores.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))

        logo = appInstance.currentScene.logo
        butonStart = appInstance.currentScene.butonStart
        butonHighScores = appInstance.currentScene.butonHighScores
        butonInstructiuni = appInstance.currentScene.butonInstructiuni
        butonExit = appInstance.currentScene.butonExit
        highScoreBox = appInstance.currentScene.scoreBoard
        highScoreBoxActive = appInstance.currentScene.scoreBoardActive
        instructionBox = appInstance.currentScene.instructionBox
        instructionBoxActive = appInstance.currentScene.instructionBoxActive
        butonMute = appInstance.currentScene.buttonMute
        childrenList= appInstance.currentScene._children

        self.assertTrue(butonStart not in childrenList and butonHighScores not in childrenList and butonInstructiuni 
        not in childrenList and butonExit not in childrenList and highScoreBox in childrenList and highScoreBoxActive
        and instructionBox not in childrenList and not instructionBoxActive and butonMute in childrenList and logo not in childrenList)
    
    def test_ButtonInstructiuni(self):
        pygame.init()
        appInstance = App.GetInstance()
        appInstance.currentScene = Meniu()
        buton = appInstance.currentScene.butonInstructiuni.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))

        logo = appInstance.currentScene.logo
        butonStart = appInstance.currentScene.butonStart
        butonHighScores = appInstance.currentScene.butonHighScores
        butonInstructiuni = appInstance.currentScene.butonInstructiuni
        butonExit = appInstance.currentScene.butonExit
        highScoreBox = appInstance.currentScene.scoreBoard
        highScoreBoxActive = appInstance.currentScene.scoreBoardActive
        instructionBox = appInstance.currentScene.instructionBox
        instructionBoxActive = appInstance.currentScene.instructionBoxActive
        butonMute = appInstance.currentScene.buttonMute
        childrenList= appInstance.currentScene._children

        self.assertTrue(butonStart not in childrenList and butonHighScores not in childrenList and butonInstructiuni 
        not in childrenList and butonExit not in childrenList and highScoreBox not in childrenList and not highScoreBoxActive
        and instructionBox in childrenList and instructionBoxActive and butonMute in childrenList and logo not in childrenList)
    
    def test_ExitHighScores(self):
        pygame.init()
        appInstance = App.GetInstance()
        appInstance.currentScene = Meniu()
        buton = appInstance.currentScene.butonHighScores.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))
        buton = appInstance.currentScene.hsExitButton.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))

        logo = appInstance.currentScene.logo
        butonStart = appInstance.currentScene.butonStart
        butonHighScores = appInstance.currentScene.butonHighScores
        butonInstructiuni = appInstance.currentScene.butonInstructiuni
        butonExit = appInstance.currentScene.butonExit
        highScoreBox = appInstance.currentScene.scoreBoard
        highScoreBoxActive = appInstance.currentScene.scoreBoardActive
        instructionBox = appInstance.currentScene.instructionBox
        instructionBoxActive = appInstance.currentScene.instructionBoxActive
        butonMute = appInstance.currentScene.buttonMute
        childrenList= appInstance.currentScene._children

        # appInstance.currentScene.DetachObject(logo)
        # appInstance.currentScene.DetachObject(butonStart)
        # appInstance.currentScene.DetachObject(butonHighScores)
        # appInstance.currentScene.DetachObject(butonInstructiuni)
        # appInstance.currentScene.DetachObject(butonExit)
        # appInstance.currentScene.AttachObject(highScoreBox)
        # appInstance.currentScene.scoreBoardActive = True

        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))

        self.assertTrue(butonStart in childrenList and butonHighScores in childrenList and butonInstructiuni 
        in childrenList and butonExit in childrenList and highScoreBox not in childrenList and not highScoreBoxActive
        and instructionBox not in childrenList and not instructionBoxActive and butonMute in childrenList and logo in childrenList)
    
    def test_ExitInstructionBox(self):
        pygame.init()
        appInstance = App.GetInstance()
        appInstance.currentScene = Meniu()
        buton = appInstance.currentScene.butonInstructiuni.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))
        buton = appInstance.currentScene.inExitButton.GetRect()
        appInstance.currentScene.OnMouseDown(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=buton.center))

        logo = appInstance.currentScene.logo
        butonStart = appInstance.currentScene.butonStart
        butonHighScores = appInstance.currentScene.butonHighScores
        butonInstructiuni = appInstance.currentScene.butonInstructiuni
        butonExit = appInstance.currentScene.butonExit
        highScoreBox = appInstance.currentScene.scoreBoard
        highScoreBoxActive = appInstance.currentScene.scoreBoardActive
        instructionBox = appInstance.currentScene.instructionBox
        instructionBoxActive = appInstance.currentScene.instructionBoxActive
        butonMute = appInstance.currentScene.buttonMute
        childrenList= appInstance.currentScene._children

        # appInstance.currentScene.DetachObject(logo)
        # appInstance.currentScene.DetachObject(butonStart)
        # appInstance.currentScene.DetachObject(butonHighScores)
        # appInstance.currentScene.DetachObject(butonInstructiuni)
        # appInstance.currentScene.DetachObject(butonExit)
        # appInstance.currentScene.AttachObject(instructionBox)
        # appInstance.currentScene.instructionBoxActive = True

        self.assertTrue(butonStart in childrenList and butonHighScores in childrenList and butonInstructiuni 
        in childrenList and butonExit in childrenList and highScoreBox not in childrenList and not highScoreBoxActive
        and instructionBox not in childrenList and not instructionBoxActive and butonMute in childrenList and logo in childrenList)

