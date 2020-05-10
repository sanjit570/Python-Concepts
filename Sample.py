class Test():
    def __init__(self):
        self.first_name = "XYZ"


    def method(self):
        print(f"{self.first_name} is just a random word is taken for checking it's functionality.")

def main():
    obj = Test()
    obj.method()

if __name__ == "__main__":
    main()