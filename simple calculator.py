class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b

a = int(input('Enter First Number:'))
b = int(input("Enter Second Number:"))

obj = calculator(a,b)

while True:
    def menu():
        x = "1. Add \n2. Sub \n3. Multiply \n4. Divide"
        print(x)

    menu()
    choice = int(input("Please select one of the following: "))

    if choice == 1:
        print("Result: ", obj.add())
        break
    elif choice == 2:
        print("Result: ", obj.subtract())
        break
    elif choice == 3:
        print("Result: ", obj.multiply())
        break
    elif choice == 4:
        print("Result: ", obj.divide())
        break
    else:
        print("Invalid option")
        break
