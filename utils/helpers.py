import enum
from typing import Generator, Iterator
from core.QuestionDisplay import Question

def questionGenerator(questions: list[dict[str, str | list | int]]) -> Iterator[Question]:
    for question in questions:
        q = Question(question=question.get("question"), awnsers=question.get("answers"), rightIndex=question.get("rightIndex"))
        yield q

class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3