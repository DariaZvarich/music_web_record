class Artist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"Artist{self.name}, {self.genre}"