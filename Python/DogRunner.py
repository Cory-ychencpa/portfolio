class Dog: #class to create object dog
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

#code begins here
print("This is the Dog Runner!")
print("would you like to create a dog?(y/n)")
create = input().lower()
if create == "y":
    print("Name your dog:")
    dogName = input().capitalize()
    print("Dog's age: ")
    dogAge = int(input())
    d1 = Dog(dogName, dogAge)
    print("Change Dog's name: ")
    d1.name = input()
    print("Name set to: "+str(d1.getName()))
