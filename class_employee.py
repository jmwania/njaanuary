class Human:
    def __init__(self, n, o):
        self.name = n 
        self.occupation = o
    
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")

        elif self.occupation == "actor":
            print(self.name, "shoots film")
    def speaks(self):
        print(self.name, "says how are you")

mwania = Human("mwania josphat", "actor")
mwania.do_work()
mwania.speaks()

cliff = Human("Cliff Katiku", "Tennis player")
cliff.speaks()
cliff.do_work()