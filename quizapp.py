print("Welcome to my Quiz")

playing = input("Are you ready to play (yes/no)? : ").lower()

if playing == "yes":
    print("Let's play")
elif playing == "no":
    print("Thank you")
else:
    print("please enter valid statment")
    quit()

correct_answers = 0

answer = input("Python uses __________ to indicate blocks of code.").lower()
if answer == "indentation":
    print("Correct answer")
    correct_answers += 1
else:
    print("Wrong answer")
answer = input("The function used to get user input in Python is __________. ").lower()
if answer == "input":
    print("Correct answer")
    correct_answers += 1
else:
    print("Wrong answer")
answer = input("In Python, a single-line comment is created using the symbol __________. ").lower()
if answer == "#":
    print("Correct answer")
    correct_answers += 1
else:
    print("Wrong answer")
answer = input("To declare a variable in Python, you simply provide a name and use the __________ operator. ").lower()
if answer == "=":
    print("Correct answer")
    correct_answers += 1
else:
    print("Wrong answer")
answer = input("The built-in function to find the length of a list in Python is __________. ").lower()
if answer == "len()":
    print("Correct answer")
    correct_answers += 1
else:
    print("Wrong answer")

print("You got", correct_answers ,"answers correct")
