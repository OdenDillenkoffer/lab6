def menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode\n2. Decode\n3. Quit")

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
        n = 0
        for element in usable_list:
            usable_list[n] = int(usable_list[n])
            usable_list[n] = usable_list[n] + 3
            n += 1
        n = 0
        for element in usable_list:
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
        print("Your password has been encoded and stored!")
    elif choice == 2:
        print(f"The encoded password is {encoded}, and the original password was {to_encode}.")
    elif choice == 3:
        exit()
    else:
        print("WRONG")