import pygame
from typing import List, Tuple  # necessário para Python 3.8
from config import globals

class Question:
    def __init__(self, question: str, answers: List[str], rightIndex: int):
        self.__question = question
        self.__answers = answers
        self.__rightIndex = rightIndex

    def getRightAnswerIndex(self) -> int:
        return self.__rightIndex

    def getQuestion(self) -> str:
        return self.__question
    
    def getAwnsers(self) -> List[str]:
        return self.__answers
    
    def getAwnsersLen(self) -> int:
        return len(self.__answers)

    def getAwnser(self, index: int) -> str:
        return self.__answers[index]

# esta classe gerencia lógica e visual (deveria ser dividida em duas: QuestionTrial e QuestionDisplay)
class QuestionTrial:
    def __init__(self, font: str, size: int, *groups):
        super().__init__(*groups)
        self.margin     = 50
        self.index      = 0
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

    def update(self, pos: Tuple[int, int]):
        local_pos = (pos[0] - self.margin, pos[1] - self.margin)
        print("[QuestionTrial] Update: ", local_pos)
        for txtRect in self.__awnsersTextRect:
            if txtRect.collidepoint(local_pos) and not self.completed:
                idx = self.__awnsersTextRect.index(txtRect)
                if idx == len(self.__awnserList) - 1:
                    self.completed = True
                else:
                    self.index = idx
                    self.__updateText()


    def setQuestion(self, question: Question) -> None:
        self.__question = question
        self.index = 0
        self.completed = False
        self.correct = False
        self.__awnserList = question.getAwnsers()
        self.__awnserList.append("Responder!!")
        self.__createSurface()
        self.__updateText()

    def testCompletion(self) -> Tuple[bool, bool]:
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
        self.__awnsersText = [
            self.font.render(
                self.__question.getAwnser(index) + "                             ",
                True,
                globals.SELECTED_TEXT_COLOR if index == self.index else globals.TEXT_COLOR
            ) for index, _ in enumerate(self.__awnserList)
        ]

        self.__awnsersTextRect = [
            awnswerText.get_rect(topleft=(self.margin, self.margin * index + self.margin * 2))
            for index, awnswerText in enumerate(self.__awnsersText)
        ]
    
    def __testCompletion(self) -> bool:
        rightIndex = self.__question.getRightAnswerIndex()
        return rightIndex == self.index
