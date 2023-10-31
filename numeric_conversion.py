
def hex_char_decode(digit):
    # checks each possible hexcode digit and converts to decimal
    if str(digit) == "A":
        new_dig = 10
    elif str(digit) == "a":
        new_dig = 10
    elif str(digit) == "B":
        new_dig = 11
    elif str(digit) == "b":
        new_dig = 11
    elif str(digit) == "C":
        new_dig = 12
    elif str(digit) == "c":
        new_dig = 12
    elif str(digit) == "d":
        new_dig = 13
    elif str(digit) == "D":
        new_dig = 13
    elif str(digit) == "E":
        new_dig = 14
    elif str(digit) == "e":
        new_dig = 14
    elif str(digit) == "F":
        new_dig = 15
    elif str(digit) == "f":
        new_dig = 15
    elif 0 <= int(digit) <= 9:
        new_dig = int(digit)
    return new_dig
    # really simple since it is one digit

def hex_string_decode(string):
    new_list = []
    # turns string into list to work with easier
    for element in string:
        new_list.append(element)
    # removed 0x
    if "0x" in string:
        new_list.pop(0)
        new_list.pop(0)
    decimal_value = 0
    # useful variables I tried and they worked, basically grows to make the exponent right
    idea = 1
    for element in new_list:
        # this math definetly looks odd but I could not figure a better way to do this
        decimal_value += int((hex_char_decode(element))) * (16 ** (int(len(new_list)) - int(idea)))
        # this for some reason was multiplied be an extra factor of 16 so i just divided again
        idea += 1
    return decimal_value


def binary_string_decode(binstring):
    true_num = 0
    true_list = []
    for element in binstring:
        true_list.append(element)
    # the previous creates a list which is easier to work with
    idea2 = 0
    # as you can see, very similar conversion as my previous work
    for element in true_list:
        if element == "1":
            # this makes sure the number is actually a number, cause multiplying by the element is a string
            true_num += int((1 * (2 ** (len(true_list) - idea2 -1))))
            idea2 += 1
        else:
            true_num += 0
            idea2 += 1
            # for zeros but keep the exponents right
    return true_num


def binary_to_hex(string):
    decimal = binary_string_decode(string)
    # creates decimal value
    hexstring = ""
    while decimal > 1:
        num = decimal % 16
        if num == 10:
            dig = "A"
        elif num == 11:
            dig = "B"
        elif num == 12:
            dig = "C"
        elif num == 13:
            dig = "D"
        elif num == 14:
            dig = "E"
        elif num == 15:
            dig = "F"
        else:
            dig = num
        hexstring += f"{dig}"
        # okay so this checks for if the modulo is A-F, if not just uses the digit, adds to string
        # then it divides by 16 to get to the next factor working with
        decimal = int(decimal / 16)
    true_numeral = hexstring[::-1]
    # the string is created backwards so it has to be reversed
    return true_numeral


def main():
    # simple menu loop function
    run_menu = True
    while run_menu:
        print("Decoding Menu")
        print("-" * 13)
        # creates menu
        print("1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit")
        choice = input('Please enter an option: ')
        if choice == "1":
            decimal = input("Please enter the numeric string to convert: ")
            print("Result:", f"{hex_string_decode(decimal)}")
        elif choice == "2":
            # every choice uses essentially the same code except for its function, could probably
            # simplify, just dont see how
            decimal = input("Please enter the numeric string to convert: ")
            print("Result:", f"{binary_string_decode(decimal)}")
        elif choice == "3":
            decimal = input("Please enter the numeric string to convert: ")
            print("Result:", f"{binary_to_hex(decimal)}")
        else:
            print("Goodbye!")
            run_menu = False
if __name__ == "__main__":
    main()