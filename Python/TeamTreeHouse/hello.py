import math

def split_check(total, number_of_people):
    cost_per_person = math.ceil(total /number_of_people)
    return cost_per_person

amount_due = split_check(84.97, 4)
print(amount_due)

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters //2)
    print(result)

# yell("You are doing great")
# yell("Don't forget to ask for help")
# yell("Don't Repeat Yourself.  Keep things DRY")


# print("Hello, World")

# praise = "You are doing great"
# praise = praise.upper()
# number_of_characters = len(praise)
# result = praise + "!" * (number_of_characters //2)
# print(result)

# advice = "Don't forget to ask for help"
# advice = advice.upper()
# number_of_characters = len(advice)
# result = advice + "!" * number_of_characters
# print(result)

# advice2 = "Don't Repeat Yourself.  Keep things DRY"
# advice2 = advice2.upper()
# number_of_characters = len(advice2)
# result = advice2 + "!" * number_of_characters
# print(result)