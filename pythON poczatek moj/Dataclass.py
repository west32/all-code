from dataclasses import dataclass

@dataclass
class Subject:
    identifier: int
    name: str
    is_obligatory: bool

def run_example():
    math = Subject(identifier=1, name="Matematyka",is_obligatory=True)

    print(math)

if __name__=="__main__":
    run_example()