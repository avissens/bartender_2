import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#lists of names and adjectives for random drinks
drink_noun = ["Margo", "Ice", "Dog", "Bird", "Heart"]
drink_adjective = ["Fluffy", "Bloody", "Sunny", "Yellow", "Blue"]


def customers():
# storing customers names
    names = []
    name = input("What's your name? ")
    while True:
        try:
            len(name) > 0
            break
        except ValueError:
            name = input("I didn't get that... What's your name again? ")
    names.append(name)
    return names

def asking_questions(questions):
#asking questions and creating a new dictionary
    answers = {}
    for item in questions:
        while True:
            answer = input(questions[item] + "\nyes/no: ")
            if answer == "yes":
                answer = True
                break
            elif answer == "no":
                answer = False
                break
            else:
                print("Enter a valid answer, please...")
                continue
        answers[item] = answer
    print(answers)
    return answers

def mixing_drinks(answers):
#mixing a drink
    names = customers()
    drink = []
    preferences = {}
    for item in set(answers) & set(ingredients):
        if answers[item] == True:
            drink.append(random.choice(ingredients[item]))
            drink_name = random.choice(drink_adjective) + " " + random.choice(drink_noun)
            print("Ingredients:", ", ".join(drink))
            print(drink_name + " " + "it is!")
            for i in range(len(names)):
                preferences[names[i]] = drink_name
                print(preferences)
        if len(drink) == 0:
            print("You are not thirsty tonight!")
            break
    return drink
    
if __name__ == '__main__':
#    main()
    while True:
        customer = input("Would you like a drink?" + "\nyes/no: ")
        if customer == "yes":
            names = customers()
            if name in names:
                print("Here your drink")
            else:
                answers = asking_questions(questions)
                drink = mixing_drinks(answers)
        elif customer == "no":
            print("Enjoy yourself and see you soon!")
            break
        else:
            print("Pardon, I didn't get it...")
            continue