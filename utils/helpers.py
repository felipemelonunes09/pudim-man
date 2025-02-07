import enum
from typing import Iterator
from core.QuestionTrial import Question

def questionGenerator(questions: list[dict[str, str | list | int]]) -> Iterator[Question]:
    for question in questions:
        q = Question(question=question.get("question"), answers=question.get("answers"), rightIndex=question.get("rightIndex"))
        yield q

class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
