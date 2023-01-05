class Letter:

    def __init__(self,lettersender,letterreceiver):
        self.lettersender = lettersender
        self.letterreceiver = letterreceiver
        self.draft = ""

    def addline(self,draft):
        self.draft = self.draft + draft + "\n"

    def getText(self):
        text = " Dear " + self.letterreceiver + ":\n\n" + self.draft + "\n" + "Sincerely,\n" + self.lettersender
        print(text)

# output

myLetter = Letter ("Mary","John")
myLetter .addline(" I am sorry we must part")
myLetter .addline(" I wish you all the best")

myLetter.getText()
