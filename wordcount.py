"""Count words in file."""

def dict_words(filename):

    data = open(filename)
    my_dict = {}

    for line in data:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            if word not in my_dict:
                my_dict[word] = 1
            else: 
                my_dict[word] += 1

    return my_dict
    
print(dict_words("test.txt"))
# print(dict_words("twain.txt"))


#further study 
#  for character in word:
        #punctuation = ",.?|"
#       if character in punctuation:
#       #character.remove(punctuation) 

