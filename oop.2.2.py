class Mother:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.get_str()        
    def get_str(self):
            return self.name    



class Dauther(Mother):
    def get_str(self):
            return "dauther " + self.name    

print(Mother("Sveta"))
print(Dauther('Anya'))