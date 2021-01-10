#Validation sequence fonction
def is_valid_(x):
    for i in range(len(x)):
        if x[i] == "a" or x[i] == "t" or x[i] == "c" or x[i] == "g":
            print(True)
        else:
            print(False)


#User sequence fonction
def get_valid_adn() :
    while True:
        sequence = input("Enter your ADN sequence: ")
        try:
            val = int(sequence)
            print("The sequence can containe ONLY string, please try again!")
            continue
        except ValueError:
            break

    sequence = is_valid_(sequence)
    return sequence

adn = get_valid_adn()
print(adn)
