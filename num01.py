
print("Welcome To My Quiz Game!")

playing = input("Do you want to play? ")

text = 'Hii IS great'
print(text.lower())
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Which letter is 5th to the right of the 20th letter from the right end?")
if answer.upper() == "15R" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Python type?")
if answer.lower() == "Interpreted" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Data type of 3.14?")
if answer.lower() == "float" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Keyword to define function?")
if answer.lower() == "def" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Loop type for fixed iterations?")
if answer.lower() == "for" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Loop type for condition-based?")
if answer.lower() == "while" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Keyword to handle errors?")
if answer.lower() == "try" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Anonymous function?")
if answer.lower() == "lambda" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Boolean false?")
if answer.lower() == "false" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Default argument keyword?")
if answer.lower() == "none" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Import module?")
if answer.lower() == "import" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Length of list?")
if answer.lower() == "len" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Add to list?")
if answer.lower() == "append" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Convert to string?")
if answer.lower() == "str" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Key-value structure?")
if answer.lower() == "dictionary" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Unique unordered collection?")
if answer.lower() == "set" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Immutable collection?")
if answer.lower() == "tuple" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Skip iteration?")
if answer.lower() == "continue" :
    print("Correct!")
else:
    print("Incorrect!")
    score +=1
answer = input("Mutable collection?")
if answer.lower() == "list" :
    print("Correct!")
else:
    print("Incorrect!")
score +=1

# ...existing code...

# Replace the final score counting section with:
total_questions = 19
correct_answers = total_questions - score  # Since score increases on incorrect answers
incorrect_answers = score

print(f"\nQuiz Results:")
print(f"Correct answers: {correct_answers}/{total_questions}")
print(f"Incorrect answers: {incorrect_answers}/{total_questions}")
percentage = (correct_answers / total_questions) * 100
print(f"Final score: {percentage:.2f}%")
