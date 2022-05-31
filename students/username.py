import random

list_prefix = ["Creampie", "Mother", "Guru", "Fucker", "Super", "Hot", "Lil'", "Big", "Fat", "OG", "Crazy", "Cute",
               "Gangsta", "Dr.", "Slim", "Sexy",
               "BoomBap", "MF", "Dope", "Brother", "RichBoy", "Boombox", "TapeMaster", "Cigar", "Crocodile",
               "TankTop", "Bazooka",
               "SurferBoy", "Killer", "BadBoy", "Texas", "Chinese", "Tiger", "MC", "Queensbridge", "Lazy", "Flip",
               "Flex", "Zero",
               "Blueberry", "Broke", "Banana", "IceCream", "Sunny", "French", "Savage", "Vanilla", "Turbo", "Classy",
               "Tacco",
               "Revolver", "Bimbo", "Pimp", "General", "Hairy", "DopeBoy", "MoneyMaker", "Rockafella", "Iron", "Sir",
               "FanBoy",
               "Armani", "HomeOffice", "Single", "Trippy"]
list_main = ["Sucker", "Fucker", "Luke", "Lex", "Blex", "Kev", "Lover", "Joe", "Jones", "Jackson", "Gorilla",
             "Alexander", "Luther",
             "Brother", "J-Dog", "Sander", "Blender", "Fish", "Godfather", "Checker", "Flexer", "Dancer", "Chiller",
             "R2D2", "StonerRama", "Sexgod",
             "Rocker", "Shocker", "Manson", "Donald", "Dickham", "Dickinson", "Ericson", "Hairyson", "Madonna", ]
list_suffix = ["Jr", "TheThird", "TheGreat", "FromThaBlock", "FromTheBronx", "InPerson", "NotInPerson", "Himself",
               "FromThePast", "OutOfOffice", "NotInService", "NotServed", "OnTheFly", "OnTheRocks", "Official",
               "Inofficial", "VIP",
               "LMS", "MVP",
               "OF", "PH", "Snap", "FromTheSouth", "Black", "Serious", "TheSock"]
list_marks = ["!", "?", "*", "#", "_", "_", "_", "-", "", ""]


class UsernameGenerator:
    def generatePre(self):
        prefix = random.choice(list_prefix)
        return prefix

    def generateMain(self):
        main = random.choice(list_main)
        return main

    def generateSuf(self):
        suffix = random.choice(list_suffix)
        return suffix

    def generateMark(self):
        mark = random.choice(list_marks)
        return mark

    def generate(self):
        digit = random.randint(11, 99)
        return self.generatePre() + str(self.generateMark()) + self.generateMain() + "_" + str(digit)
