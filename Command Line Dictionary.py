import json
from difflib import get_close_matches

data = json.load(open("data.json"))

#If the word you enter is in the dictionary this will return the definition
def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
#If the word you enter is close to a word in the dictionary this will ask you if a similar word is what you meant
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s?" % get_close_matches(word, data.keys())[0])
        if yn.lower() == "yes" or yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "no" or yn.lower() == "n":
            return "Please check your spelling.  Otherwise I don't know that word."
        elif len(yn.lower()) == 0:
            return "You did not type anything."
        else:
            return "Sorry, I don't understand."
    elif len(word) == 0:
        return "You didn't write anything."

    else:
        return "The word doesn't exist, please check your spelling."

word = input("What word do you want to know?")

print(lookup(word))
