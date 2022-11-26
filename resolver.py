class Resolver:
    def __init__(self):
        self.path = []

    def __str__(self):
        # string = "[ \n"
        # for line in self.content:
        #     string = string + str(line) + "," + "\n"
        # string = string + "]"
        # return string
        return self
    
    def getPltXY(self):
        self.path = [(2.0, 3.0), (3.0, 3.0), (4.0, 4.0), (5.0, 4.0), (6.0, 4.0), (7.0, 4.0), (8.0, 4.0), (9.0, 4.0), (10.0, 4.0)]
        xpath = [x - 0.5 for (x,y) in self.path]
        ypath = [y + 0.5 for (x,y) in self.path]
        return (xpath,ypath)
    
def main():
        
    resv = Resolver()
    resv.getPltXY()
    
if __name__ == "__main__":
    main()