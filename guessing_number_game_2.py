def respond():
    """
    Function provides hints from the user.
    :return: Too big!, Too small! or You win!
    """
    answears = ["1", "2", "3"]
    while True:
        print("1 = Too big!")
        print("2 = Too small!")
        print("3 = You win!")
        answear = input("Choose one of the above options: ")
        if answear in answears:
            break
        print("Please select number from 1 to 3!")
    return answear


def computer_guess():
    """
    Function in 10 tries guesses unknown user number from 1 to 1000.
    :return: Computer guess
    """
    print("Imagine number between 1 to 1000 and I will figure it out in maximum of 10 tries!")
    print("Press 'Enter' when You are ready :)")
    input()
    min_number = 0
    max_number = 1000
    user_answear = ""
    i = 1
    while user_answear != "3":
        if i <= 10:
            i += 1
            guess = int(((max_number - min_number) / 2) + min_number)
            print(f"My guess is: {guess}")
            user_answear = respond()
            if user_answear == "1":
                max_number = guess
            elif user_answear == "2":
                min_number = guess
            elif user_answear == "3":
                print(f"I figured it out in {i - 1} tries!")
        else:
            print("Don't cheat!")
            break


computer_guess()
