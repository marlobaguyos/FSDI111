import random

class Thief:
    sneaky = True

    def pickpocket(self):
        return bool(random.randint(0,1))