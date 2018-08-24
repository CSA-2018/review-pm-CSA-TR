class Person:
    def __init__(self, username, age, city, number):
        self.username=username
        self.age=age
        self.city=city
        self.number=number
        
    def start():
        u=input("Username: ")
        a=input('Age: ')
        c=input('What city do you live in?')
        p1=Person(u, a, c, p)
        print(p1)
        
    def phone():
        while True:
            try:
                p=int(input('Age:'))
                return p
            except ValueError:
                print('Please enter a number')
