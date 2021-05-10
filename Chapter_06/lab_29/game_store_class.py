class GameStore:

    def __init__(self):
        self.list = []

    def __call__(self, items):
        for item in items:
            if not item in self.list:
                self.list.append(item)

