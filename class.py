class Computer:
    name = "Hp"


    # special method inbuilt
    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor

    # methods
    def info(self, brand):
        print(f"This is {brand} -- {self.ram}) -----> {self.processor}")

    #classmethod
    @classmethod
    def compare(cls):
        print(cls.name)


comp1 = Computer("8gb", "i7")
comp2 = Computer("4gb", "i5")
# print(comp1.name)
comp1.info("probook")
comp2.info()

computer.detail()




