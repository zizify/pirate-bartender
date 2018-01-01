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

def ask(questions):
    """Asks the user to answer questions about their preferred drink."""
    answers = {}
    
    for k, v in questions.items():
        userInput = input(v + ' ')
        if userInput in ['y', 'yes']:
            answers[k] = True
        else:
            answers[k] = False
            
    makedrinks(answers, ingredients)
    
def makedrinks(responses, ingredients):
    drink = ''
    
    for k, v in responses.items():
        if v == True:
            drink += ' ' + random.choice(ingredients[k])
    
    print(drink)
    
if __name__ == '__main__':
    ask(questions)