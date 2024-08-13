class Animal:
    def __init__(self):
        self.name = "Animal"#deve ser criado primeiro o metodo com a função de print, e so no final 
        print("animal created")#que deveser printado, mas antes disso deve ser criado
                                #uma instancia da classe dog , como consta no final 
    def whoami(self):
        print("i am an animal")

    def eat(self):
        print("and i am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created")

    def whoami(self):
        print("iamdog, WOOF!")

    # Create an instance of the Dog class
mydog = Dog()

# Call the methods, apos isso tudo o metodo deve ser chamado como exemplo abaixo. 
mydog.whoami()
mydog.eat()