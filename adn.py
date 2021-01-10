#Validation sequence fonction
def is_valid_(ADN):
    for i in range(len(ADN)):
        if ADN[i] == "a" or ADN[i] == "t" or ADN[i] == "c" or ADN[i] == "g":
            print(True)
        else:
            print(False)


#User sequence fonction
def get_valid_adn(prompt) :
    while True:
        sequence = input(prompt)
        try:
            val = int(sequence)
            print("The sequence can containe ONLY string, please try again!")
            continue
        except ValueError:
            break
    sequence = is_valid_(sequence)

adn = get_valid_adn("Enter your ADN sequence: ")