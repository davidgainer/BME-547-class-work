def create_dictionary():
    x = {"day": "When the sun is out", 
         "night": "When the moon is out",
         "food": "something you eat"}
    return x

def add_to_dictionary(in_dictionary, new_word,
                      new_definition):
    in_dictionary[new_word] = new_definition
    

def output_dictionary(in_dictionary):
    print(type(in_dictionary))
    print(in_dictionary)
    add_to_dictionary(in_dictionary, "lunch", "mid-day meal")
    print(get_definition(in_dictionary,"lunch"))
    print(in_dictionary.keys())
    print(in_dictionary.values())

def get_definition(in_dictionary, word):
    another_way = in_dictionary.get(word)
    print(another_way)
    definition = in_dictionary[word]
    return definition


# .get will only return an error message of none. 
# square brackets will return a key error 
if __name__ == "__main__":
    my_dictionnary = create_dictionary()
    output_dictionary(my_dictionnary)