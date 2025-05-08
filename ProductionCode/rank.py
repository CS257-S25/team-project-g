class Rank:
    def __init__(self, name: str, tally: int):
        self.name = name
        self.tally = tally

    def __str__(self) -> str:
        return f"{self.name}: {self.tally}"
