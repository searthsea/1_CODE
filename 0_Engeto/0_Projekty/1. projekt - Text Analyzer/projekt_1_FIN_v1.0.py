"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Schwarz
email: svarmartin@gmail.com
"""

from sys import exit

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
        f"Hello {username.title()}, welcome to the Text Analyzer. Select one of the texts for analysis."
    )
    selected_text = input(f"Type in a whole number between 1 and {len(texts)}: ")
    if not selected_text.isnumeric():
        print("The input is not a whole number! Try again.")
        exit()
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
        title_list = []
        upper_list = []
        lower_list = []
        numeric_list = []
        other_list = []
        number_0_9 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        alphabet_eng_capital = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]

        word_count = len(word_list_clean)

        for word in word_list_clean:
            if word.istitle() and word[0] not in number_0_9:
                title_counter += 1
                title_list.append(word)
            else:
                title_counter += 0
        for word in word_list_clean:
            if word.isupper() and word[0] not in number_0_9:
                upper_counter += 1
                upper_list.append(word)
            else:
                upper_counter += 0
            if word.islower():
                lower_counter += 1
                lower_list.append(word)
            else:
                lower_counter += 0
            if word.isnumeric():
                numeric_counter += 1
                numeric_list.append(word)
                num_sum_counter += int(word)
            else:
                numeric_counter += 0
        for word in word_list_clean:
            if (
                word not in title_list
                and word not in upper_list
                and word not in lower_list
                and word not in numeric_list
            ):
                other_list.append(word)
            else:
                continue
        for word in other_list:
            if word[0] in alphabet_eng_capital:
                title_list.append(word)
            else:
                continue

        # Word length stats:
        maxlen = ""
        for word in word_list_clean:
            if len(word) > len(maxlen):
                maxlen = word
            else:
                continue

        maxlen_counter = 0
        for string in maxlen:
            maxlen_counter += 1

        word_len_list = []
        for word in word_list_clean:
            word_len_list.append(len(word))

        word_len_dict = {}
        for number in range(1, maxlen_counter + 1):
            word_len_dict.setdefault(number, 0)

        for number in word_len_list:
            word_len_dict[number] += 1

        # VISUALIZATION & FINAL RESULTS PRINTS:
        print("\nRESULTS BELOW:")
        print("---------------------------------------------------")
        print(
            f"Total words: {word_count}\nTitlecase words: {title_counter} \
            \nUppercase words: {upper_counter}\nLowercase words: {lower_counter} \
            \nNumeric strings: {numeric_counter}\nSum of all numbers: {num_sum_counter}"
        )
        print("---------------------------------------------------")
        print(
            "How many times words of a specific length occured: \
            \nLEN| OCCURRENCES |N"
        )
        print("---------------------------------------------------")
        for n in range(1, maxlen_counter + 1):
            asterisk = word_len_dict[n] * "*"
            print(" {0} |{1} |{2}".format(n, asterisk, word_len_dict[n]))
    else:
        print(
            f"Number out of range! Selected text {selected_text} does not exist in the database. Try again."
        )
        exit()
else:
    print(
        f"\nusername: {username}\npassword: {password} \
        \nWrong username and/or password!\nTerminating program..."
    )
    exit()

# uncomment for testing purposes:
# print(
#     f"\nWORD LISTS:\nTitle: {title_list},\nUpper: {upper_list},\nLower: {lower_list},\nNumeric: {numeric_list}, \nSpecial cases:{other_list}"
# )
