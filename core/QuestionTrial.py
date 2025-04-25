import pygame
from config import globals
from typing import List


class Question():
    def __init__(self, question: str, answers: list[str], rightIndex: int):
        self.__question = question
        self.__answers = answers
        self.__rightIndex = rightIndex

    def getRightAnswerIndex(self) -> int:
        return self.__rightIndex

    def getQuestion(self) -> str:
        return self.__question
    
    def getAwnsers(self) -> list[str]:
        return self.__answers
    
    def getAwnsersLen(self) -> int:
        return len(self.__answers)

    def getAwnser(self, index: int):
        return self.__answers[index]
    
## this class handle logic and visual (it shoud divided into two other classes QuestionTrial and QuestionDisplay)
class QuestionTrial():
    def __init__(self, font: str, size: int, *groups):
        super().__init__(*groups)
        self.margin     = 50
        self.index      = 0
        self.count      = 0
        self.refresh    = 8
        self.fontName   = font
        self.size       = size
        self.completed  = False
        self.correct    = False
        self.color  = (*globals.SCREEN_COLOR, 230)
        
        self.__question: Question = None
        self.__createSurface()

    def draw(self, surface: pygame.Surface):
        self.image.blit(self.__questionText, self.__questionTextRect)
        for i in range(self.__question.getAwnsersLen()):
             self.image.blit(self.__awnsersText[i], self.__awnsersTextRect[i])
        surface.blit(self.image, (self.margin, self.margin))

    def update(self):
        keys = pygame.key.get_pressed()
        if self.count > 0:
            self.count -= 1
        else:
            if keys[pygame.K_UP]:
                self.index = (self.index - 1) % self.__question.getAwnsersLen()
                self.__updateText()
            elif keys[pygame.K_DOWN]:
                self.index = (self.index + 1) % self.__question.getAwnsersLen()
                self.__updateText()
            elif keys[pygame.K_RETURN]:
                self.completed = True
            self.count = self.refresh

    def setQuestion(self, question: Question) -> None:
        self.__question = question
        self.index = 0
        self.completed = False
        self.correct = False
        self.__createSurface()
        self.__updateText()

    def testCompletion(self) -> tuple[bool, bool]:
        self.correct = self.__testCompletion()
        return (self.completed, self.correct)
    
    def __createSurface(self) -> None:
        self.image  = pygame.Surface((globals.SCREEN_SIZE[0] - self.margin*2, globals.SCREEN_SIZE[1] - self.margin*2), pygame.SRCALPHA)
        self.font   = pygame.font.SysFont(self.fontName, self.size)
        self.rect   = self.image.get_rect(topleft=(self.margin, self.margin))
        self.image.fill(self.color)

    def __updateText(self):
        self.__questionText = self.font.render(self.__question.getQuestion(), True, globals.TEXT_COLOR)
        self.__questionTextRect = self.__questionText.get_rect(topleft=(self.margin, self.margin))
        self.__awnsersText      = [self.font.render(self.__question.getAwnser(index), True, globals.SELECTED_TEXT_COLOR if index == self.index else globals.TEXT_COLOR)  for index, awnsers in enumerate(self.__question.getAwnsers())]
        self.__awnsersTextRect  = [awnswerText.get_rect(topleft=(self.margin, self.margin*index + self.margin*2)) for index, awnswerText in enumerate(self.__awnsersText)]
    
    def __testCompletion(self) -> bool:
        rightIndex = self.__question.getRightAnswerIndex()
        return rightIndex == self.index
