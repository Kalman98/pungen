import sys
import random
import string


class UsernameGenerator:
    def __init__(self):
        # command feedback for various arguments
        min_length, max_length = 0, 0  # quells PyCharm "might be referenced before assignment" warnings
        try:
            max_length = int(sys.argv[2])  # max_length equals the first argument
        except IndexError:
            is_ranged = False
        else:
            is_ranged = True  # the length of usernames is ranged

        try:
            if sys.argv[1] == "help":  # if the first argument is "help"
                print("Usage: \n"  # print the usage instructions
                      "    pungen <username_length>\n"
                      "    pungen <username_length_min> <username_length_max>\n"
                      "Note: It is recommended to keep lengths under 20 for more realistic names.")
                sys.exit()
            if 2 > int(sys.argv[1]) > 20:  # if the given length is outside the 2 - 20 character range
                print("Please input a number greater than 2 and less than 20.")
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

        # decide if the first letter is a consonant
        if random.randrange(2) == 1:
            is_consonant = True
        else:
            is_consonant = False
        # begin generating usernames
        for i in range(10):
            username, is_double = "", False  # reset variables
            if is_ranged:
                length = random.randrange(min_length, max_length)
            for j in range(length):
                if not is_double:  # if the last character was a double, skip a letter
                    # 1 in 8 chance if username is shorter than the length
                    if random.randrange(8) == 0 and len(username) < int(length) - 1:
                        is_double = True  # this character will be doubled
                    if is_consonant:
                        username += self.add_consonant(is_double)  # add consonant to username
                    else:
                        username += self.add_vowel(is_double)  # add vowel to username
                    is_consonant = not is_consonant  # swap consonant/vowel value for next time
                else:
                    is_double = False  # reset double status so the next letter won't be skipped
            if random.randrange(2) == 0:
                username = string.capwords(username)  # capitalize the first letter
            if random.randrange(5) == 0:
                for j in range(random.randrange(3) + 1):  # loop 1 - 3 times
                    username += str(random.randrange(10))  # append a random number, 1 - 9
            print(username)

    def add_consonant(self, is_double):
        if is_double:
            return random.choice(self.consonants) * 2  # add two of the consonant
        else:
            return random.choice(self.consonants)  # add the consonant

    def add_vowel(self, is_double):
        if is_double:
            return random.choice(self.vowels) * 2  # add two of the vowel
        else:
            return random.choice(self.vowels)  # add the vowel

UsernameGenerator()  # run the class
