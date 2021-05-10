from cake.cake_class import Cake

class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling,
                 occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print("Occasion:        {}".format(self.occasion))
        print("Shape:           {}".format(self.shape))
        print("Ornaments:       {}".format(self.ornaments))
        print("Text:            {}".format(self.text))

