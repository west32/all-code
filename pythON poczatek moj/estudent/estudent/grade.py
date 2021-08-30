from dataclasses import dataclass
from estudent.subject import Subject
from typing import ClassVar

@dataclass
class Grade:
    value:int
    FAILING_GRADE: ClassVar = 1

    def is_passing(self):
        return self.value > Grade.FAILING_GRADE

    def __repr__(self):
        return  str(self.value)
@dataclass()
class FinalGrade(Grade):
    subject: Subject

    def __repr__(self):
        return f"{self.subject}: {self.value}"