class Animal():
    def __init__(self, dog, cat):
        self.dog = dog 
        self.cat = cat 

    
    def doggo(self):
        return self.dog
    
    def kitty(self):
        return self.cat
    
    def owner_1(self, fname, lname):
        print(f"this is {fname} {lname} and owns one {self.cat} which is cat and one {self.dog} whch it a dog")


    def house(self):
        pass

class Human(Animal):
    def __init__(self, dog, cat):
        super().__init__(dog, cat)

        print(dog)
        print(cat)


owner = Animal("jack", "tim")
print(owner.doggo())
print(owner.kitty())
print(owner.owner_1(input("fname: "), input("lname: ")))

human = Human('jugro2q', "bkqwbfooqln")
print(human.doggo())

     