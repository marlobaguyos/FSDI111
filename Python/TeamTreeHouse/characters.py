import random

class Thief:
    sneaky = True

    def pickpocket(self):
        print("Called by {}".format(self))
        return bool(random.randint(0,1))