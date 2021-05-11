from cake.no_duplicate_class import NoDuplicates

class Cake:
    
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
        """
            create new Cake object has overloaded += operator
            
            methods:
                show_info()
                add_additives(obj, additives)
                add_extra_additives(obj, additives)

            property:
                full_name()
        """
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    
    def __iadd__(self, other):
        if type(other) == list:
            self.additives.extend(other)
            return self
        elif type(other) == str:
            self.additives.append(other)
            return self
        else:
            raise Exception(str.format("{} is correct type !", other))


    def __str__(self):
        return str.format("kind: {}\nname: {}\nadditives: {}", self.kind, self.name, self.additives)
    

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
    

    def add_additives(self, additives):
        self.additives.extend(additives)

    @property
    def full_name(self):
        """show Cake properties: name and kind"""
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

# #! There is no member Cake class 
# @NoDuplicates
# def add_extra_additives(cake, additives):
#     cake.add_additives(additives)
    
    #? Alternative version without Decorator -> method is member Cake class
    def add_extra_additives(self, additives):
        for additive in additives:
            if not additive in self.additives:
                self.additives.extend(additives)

    