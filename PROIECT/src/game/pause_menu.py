import pygame

from framework.events_manager import EventsManager
from framework.scene import Scene
from framework.button import Button
from framework.constants import *
import framework.app as app

import game.game_session as gs
import game.meniu as gm


class PauseMenu(Scene):
    def __init__(self, gameScene: 'gs.GameSession', displayState: pygame.Surface) -> None:
        super().__init__()
        self.gameScene = gameScene

        darkBgSurface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha()
        darkBgSurface.fill((0, 0, 0, 125))
        displayState.blit(darkBgSurface, (0, 0))
        self.ChangeBgImage(displayState)

        buttonW = 280
        buttonH = 60
        buttonX = DISPLAY_WIDTH / 2 - buttonW / 2
        yCenter = DISPLAY_HEIGHT / 2
        self.buttonResume = Button(buttonX, yCenter - buttonH - 7, buttonW, buttonH, 'Continuare joc', (255, 255, 255), RES_DIR + "font\Happy School.ttf", 35, RES_DIR + "img/ButtonBg.png", (216, 216, 216))
        self.AttachObject(self.buttonResume)
        self.buttonQuit = Button(buttonX, yCenter + 7, buttonW, buttonH, 'Iesire', (255, 255, 255), RES_DIR + "font\Happy School.ttf", 35, RES_DIR + "img/ButtonBg.png", (216, 216, 216))
        self.AttachObject(self.buttonQuit)
        
        muteButtonW = 50
        muteButtonH = 50
        muteButtonX = DISPLAY_WIDTH - muteButtonW - 10
        muteButtonY = 10
        self.buttonMute = Button(muteButtonX, muteButtonY, muteButtonW, muteButtonH)
        self.AttachObject(self.buttonMute)
        self.mutedIcon = pygame.transform.scale(pygame.image.load(RES_DIR + "no-sound.png"), (muteButtonW, muteButtonH))
        self.unmutedIcon = pygame.transform.scale(pygame.image.load(RES_DIR + "sound.png"), (muteButtonW, muteButtonH))
        if app.App.GetInstance().IsMuted():
            self.buttonMute.SetBgImage(self.mutedIcon)
        else:
            self.buttonMute.SetBgImage(self.unmutedIcon)


    def OnSceneEnter(self) -> None:
        manager = EventsManager.GetInstance()
        manager.AddListener(pygame.MOUSEBUTTONDOWN, self.OnButtonResume)
        manager.AddListener(pygame.MOUSEBUTTONDOWN, self.OnButtonMute)
        manager.AddListener(pygame.MOUSEBUTTONDOWN, self.OnButtonQuit)


    def OnButtonResume(self, event: pygame.event.Event) -> None:
        if self.buttonResume.CollidesWithPoint(event.pos):
            self.buttonResume.ClickedSound(app.App.GetInstance().IsMuted())
            app.App().GetInstance().PlayNewScene(self.gameScene)
    

    def OnButtonMute(self, event: pygame.event.Event) -> None:
        if self.buttonMute.CollidesWithPoint(event.pos):
            appInst = app.App.GetInstance()
            appInst.SwitchMuteOption()
            if(not appInst.IsMuted()):
                pygame.mixer.Sound(RES_DIR + "audio/Click.ogg").play()
            pygame.mixer.Channel(0).set_volume(0 if appInst.IsMuted() else 0.1)
            self.buttonMute.SetBgImage(self.mutedIcon if appInst.IsMuted() else self.unmutedIcon)
    

    def OnButtonQuit(self, event: pygame.event.Event) -> None:
        if self.buttonQuit.CollidesWithPoint(event.pos):
            self.buttonQuit.ClickedSound(app.App.GetInstance().IsMuted())
            mainMenu = gm.Meniu()
            pygame.mixer.Channel(0).stop()
            app.App().GetInstance().PlayNewScene(mainMenu)
