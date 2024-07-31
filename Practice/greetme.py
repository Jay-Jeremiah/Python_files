def greetme():
    name = input("What is your name?\n")

    print("Hello", name)
    res = input("How are you?\n")
    if res == "I am fine":
        print("That is nice")
    elif res == "I am not fine":
        print("God loves you dear. Be strong in faith.")
    else:
        print("Error message.")
        print("Please type either 'I am fine' or 'I am not fine'")

    
    print("Just to  clarify the details above.")

    return f"Your name is {name} and your response is {res}\nWe wish you a lovely day"
    

print(greetme())