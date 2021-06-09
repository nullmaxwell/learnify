import pandas as pd

class Helper:
    tracker = []
    actual = None    
    
    @classmethod
    def initialize(self):
        Helper.actual = pd.read_csv('data/liked.csv')
        Helper.actual['Label'] = None

        for x in range(0,10):
            Helper.actual = Helper.actual.sample(frac=1).reset_index(drop=True)

    @classmethod
    def something(self):
        for col in range(0, len(Helper.actual)):
            self.showInfo(col)
            label = self.getInput()

            if label == "b":
                self.showInfo(col-1)
                label = self.getInput()
                Helper.actual.at[col-1, 'Label'] = label

                self.showInfo(col)
                label = self.getInput()
                Helper.actual.at[col, 'Label'] = label

            Helper.actual.at[col, 'Label'] = label
        
        self.writeOut(Helper.actual)

    def getInput():
        while True:
            temp = str(input("Label: "))
            if temp not in ["0","1", "b"]:
                print("Invalid entry... try again.")
            else:
                if temp == "0":
                    return False
                if temp == "1":
                    return True
                if temp == "b":
                    return "b"

    def writeOut(self):
        Helper.actual.to_csv('data/liked_labeled.csv', index = True)

    @classmethod
    def showInfo(self, col):
        print()
        print()
        print(str(col+1) + "/" + str(len(Helper.actual)))
        print("Track: " + Helper.actual.at[col, 'Track Name'])
        print("Album: " + Helper.actual.at[col, 'Album Name'])
        print("Artist: " + Helper.actual.at[col, 'Artist Name(s)'])
        print("--------------------------------------------")