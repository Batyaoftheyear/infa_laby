class Animal:
    __age = 0
    __name = ""
    def __init__(self,age,name):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
       
    def __str__(self):
        return self.get_str()
   
class Zebra(Animal):
    def get_str(self):
        return "Zebra Name:" + self.get_name() + " Age:" + str(self.get_age())

class Dolphin(Animal):
    def get_str(self):
        return "Dolphin Name:" + self.get_name() + " Age:" + str(self.get_age())

print(Zebra(15,"Zoya").__str__())
print(Dolphin(19, "Denis"))

