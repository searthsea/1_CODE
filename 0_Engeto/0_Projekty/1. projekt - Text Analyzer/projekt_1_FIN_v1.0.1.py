"""
projekt_1_FIN_v1.0.1.py: první projekt do Engeto Online Python Akademie

author: Martin Schwarz
email: svarmartin@gmail.com

verze č. 2
"""

import sys

texts = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""",
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]
user_data = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

username = input("Enter your username:")
password = input("Enter your password:")

if username in user_data.keys() and password == user_data[username]:
    print(
        f"Hello {username.title()}, welcome to the Text Analyzer. \
        \nSelect one of the texts for analysis."
    )
    selected_text = input(f"Type a whole number between 1 and {len(texts)}: ")
    if not selected_text.isnumeric():
        sys.exit(
            "The input is not a whole number! \
            \nTerminating program..."
        )
    elif int(selected_text) >= 1 and int(selected_text) <= (len(texts)):
        print("Analyzing text...")
        analyzed = texts[int(selected_text) - 1]
        words_separated = analyzed.split()
        word_list_clean = []
        for word in words_separated:
            word_strip = word.strip(".,:;!?()")
            word_list_clean.append(word_strip)

        # STATS ENGINE:
        title_counter = 0
        upper_counter = 0
        lower_counter = 0
        numeric_counter = 0
        num_sum_counter = 0

        word_count = len(word_list_clean)

        for word in word_list_clean:
            # Title_counter: Exclude 1 char capital letter strings, e.g. "A"
            # these are counted as Uppercase words.
            # Exclude strings where 1st char is numeric , e.g. "30N"
            if len(word) >= 2 and word.istitle() and word[0].isalpha():
                title_counter += 1
            if word.isupper() and word.isalpha():
                upper_counter += 1
            if word.islower() and word[0].isalpha():
                lower_counter += 1
            if word.isnumeric():
                numeric_counter += 1
                num_sum_counter += int(word)

        # WORD LENGTH STATS:
        maxlen_word = ""
        word_len_dict = {}

        for word in word_list_clean:
            if len(word) > len(maxlen_word):
                maxlen_word = word

            word_length = len(word)
            if word_length in word_len_dict:
                word_len_dict[word_length] += 1
            else:
                word_len_dict[word_length] = 1

        maxlen = len(maxlen_word)

        # VISUALIZATION & FINAL RESULTS PRINTS:
        print("\nRESULTS BELOW:")
        print("---------------------------------------------------")
        print(
            f"Total words: {word_count} \
            \nTitlecase words: {title_counter} \
            \nUppercase words: {upper_counter} \
            \nLowercase words: {lower_counter} \
            \nNumeric strings: {numeric_counter} \
            \nSum of all numbers: {num_sum_counter}"
        )
        print("---------------------------------------------------")
        print(
            "How many times words of a specific length occured: \
            \nLEN| OCCURRENCES |N"
        )
        print("---------------------------------------------------")
        for n in range(1, maxlen + 1):
            asterisk = word_len_dict.get(n, 0) * "*"
            print(" {0} |{1} |{2}".format(n, asterisk, word_len_dict.get(n, 0)))
    else:
        print(
            f"Number out of range! \
            \nSelected text {selected_text} does not exist in the database."
        )
        sys.exit("Terminating program...")
else:
    print(
        f"\nusername: {username}\npassword: {password} \
       \nWrong username and/or password!"
    )
    sys.exit("Terminating program...")
