import enum
from typing import Iterator, List, Dict, Union  # necessário para Python 3.8
from core.QuestionTrial import Question

def questionGenerator(questions: List[Dict[str, Union[str, List, int]]]) -> Iterator[Question]:
    for question in questions:
        q = Question(
            question=question.get("question"),
            answers=question.get("answers"),
            rightIndex=question.get("rightIndex")
        )
        yield q

class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
