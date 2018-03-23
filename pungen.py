import sys
import random


class UsernameGenerator:
    def __init__(self):
        # command feedback for various arguments
        min_length, max_length = 0, 0  # quells PyCharm "might be referenced before assignment" warnings
        try:
            max_length = int(sys.argv[2])  # max_length equals the first argument
        except IndexError:  # if there is no second variable, flag length as a fixed number
            is_ranged = False
        else:
            is_ranged = True  # the length of usernames is ranged

        try:
            if sys.argv[1] == "help":  # if the first argument is "help"
                print("Usage: \n"  # print the usage instructions
                      "    pungen <username_length>\n"
                      "    pungen <username_length_min> <username_length_max>\n"
                      "Note: It is recommended to keep lengths under 20 for more realistic user names.")
                sys.exit()
            if is_ranged:
                min_length = int(sys.argv[1])  # min_length equals the first argument
            else:
                length = int(sys.argv[1])  # length equals the first argument
        except IndexError:  # if the user did not pass a length argument
            print("No length specified, using default of 7.")
            length = 7  # set length to default of 7

        # initialize tuples

        self.consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                           'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

        self.vowels = ('a', 'e', 'i', 'o', 'u')

        self.cons_weighted = (("t", "n"), ("r", "s", "h", "d"), ("l", "f", "c", "m"), ("g", "y", "p", "w", "b"),
                              ("v", "b", "j", "x", "q"), "z")
        self.vow_weighted = (("e", "a", "o"), ("i", "u"))
        self.double_cons = ("he", "re", "ti", "ti", "hi", "to", "ll", "tt", "nn", "pp", "th", "nd", "st", "qu")
        self.double_vow = ("ee", "oo", "ei", "ou", "ai", "ea", "an", "er", "in",
                           "on", "at", "es", "en", "of", "ed", "or", "as")

        # begin generating usernames
        for i in range(10):
            username, is_double, num_length = "", False, 0  # reset variables
            if random.randrange(10) > 0:
                is_consonant = True
            else:
                is_consonant = False

            if is_ranged:  # pick a random length for this username given the ranges
                length = random.randrange(min_length, max_length)

            if random.randrange(5) == 0:  # decide if there will be numbers after the name
                num_length = random.randrange(3) + 1
                if length - num_length < 2:  # we don't want the username to be too short
                    num_length = 0

            for j in range(length - num_length):  # we leave room for the numbers after the name here
                if len(username) > 0:
                    if username[-1] in self.consonants:
                        is_consonant = False
                    elif username[-1] in self.consonants:
                        is_consonant = True
                if not is_double:  # if the last character was a double, skip a letter
                    # 1 in 8 chance of doubling if username is still short enough
                    if random.randrange(8) == 0 and len(username) < int(length - num_length) - 1:
                        is_double = True  # this character will be doubled
                    if is_consonant:
                        username += self.get_consonant(is_double)  # add consonant to username
                    else:
                        username += self.get_vowel(is_double)  # add vowel to username
                    is_consonant = not is_consonant  # swap consonant/vowel value for next time
                else:
                    is_double = False  # reset double status so the next letter won't be skipped
            if random.randrange(2) == 0:
                # this was the best method I could find to only capitalize the first letter in Python 3
                username = username[:1].upper() + username[1:]
            if num_length > 0:
                for j in range(num_length):  # loop 1 - 3 times
                    username += str(random.randrange(10))  # append a random number, 0 - 9
            print(username)

    def get_consonant(self, is_double):
        if is_double:
            return random.choice(self.double_cons)  # add two consonants from our pre-defined tuple
        else:
            # we're just guessing at some good weights here. This is how more common letters get used more
            i = random.randrange(100)
            if i < 40:
                weight = 0
            elif 65 > i >= 40:
                weight = 1
            elif 80 > i >= 65:
                weight = 2
            elif 90 > i >= 80:
                weight = 3
            elif 97 > i >= 90:
                weight = 4
            else:
                # the last group is Z by itself. No point in going through extra code when we can finish it here
                return self.cons_weighted[5]
            # return a random consonant based on the weight
            return self.cons_weighted[weight][random.randrange(len(self.cons_weighted[weight]))]

    def get_vowel(self, is_double):
        if is_double:
            return random.choice(self.double_vow)  # add two vowels from our pre-defined tuple
        else:
            i = random.randrange(100)
            if i < 70:
                weight = 0
            else:
                weight = 1
            # return a random vowel based on the weight
            return self.vow_weighted[weight][random.randrange(len(self.vow_weighted[weight]))]

UsernameGenerator()  # run the class
