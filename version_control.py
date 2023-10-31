def menu():
    print("Menu")
    # simple menu loop
    print("-" * 13)
    print("1. Encode\n2. Decode\n3. Quit\n")


# Decodes encoded password by adding 7 to the existing digit, bringing the total addition to 10. Modulo by 10.
def decode(encoded_password):
    enc_pass_list = []
    for char in encoded_password:
        orig_digit = (int(char) + 7) % 10
        enc_pass_list.append(str(orig_digit))
    orig_password = ''.join(enc_pass_list)

    print(f"The encoded password is {encoded_password}, and the original password was {orig_password}.\n")


run_loop = True
while run_loop:
    menu()
    choice = input("Please enter a option: ")
    choice = int(choice)
    if choice == 1:
        usable_list = []
        to_encode = input("Please enter your password to encode:")
        for element in to_encode:
            usable_list.append(element)
        # turns the string into a list so i can actually mess with it
        n = 0
        for element in usable_list:
            usable_list[n] = int(usable_list[n])
            usable_list[n] = usable_list[n] + 3
            # shifts each number up 3
            n += 1
        n = 0
        for element in usable_list:
            # deals with any integer above 9 and shifts them down to where they should be
            if element >= 10:
                if element == 10:
                    usable_list[n] = 0
                elif element == 11:
                    usable_list[n] = 1
                elif element == 12:
                    usable_list[n] = 2
            n += 1
        n = 0
        for element in usable_list:
            usable_list[n] = str(usable_list[n])
            n += 1
        encoded = "".join(usable_list)
        # creates the encoded password and saves it as a string
        print("Your password has been encoded and stored!\n")
    elif choice == 2:
        decode(encoded)
    elif choice == 3:
        exit()
    else:
        print(":3")
        # in case something goes wrong also its funny to have it say that
