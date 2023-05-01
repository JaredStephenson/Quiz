#Version 1 - Programming Assessment - Quiz on any chosen subject

#Correct Score
score = 0
score = int(score)

#Incorrect Score
iscore = 0
iscore = int(iscore)

#Welcome
print("Welcome to Jared Stephenson's 3 question Quiz")
print("")
#Start Quiz
input("Press Enter to start ")
print("")
#Question list
questions1 = {
    "question1": "Which company owns the video game Minecraft?",
    "choices1": ["A. Microsoft", "B. Square Enix", "C. Bethesda"],
    "answer1": "A"
}

questions2 = {
    "question2": "Which company owns the video game Grand Theft Auto V?",
    "choices2": ["A. Rockstar Games", "B. Square Enix", "C. Activision"],
    "answer2": "A"
    }
questions3 = {
    "question3": "Which company owns the video game Rust?",
    "choices3": ["A. Activision", "B. Facepunch Studios", "C. Valve"],
    "answer3": "B"
    }
    
#print first question
print(questions1["question1"])
for choice in questions1["choices1"]:
    print(choice)
    
#Ask user to choose
user_answer1 = input("Enter your choice (A, B, or C): ")
    
#check answer
if user_answer1 == questions1["answer1"]:
    print("Correct.")
    score = score + 1
    print("You have", score, "Correct")
    print("You have", iscore, "Incorrect")    
else:
    print("Incorrect.")
    iscore = iscore + 1
    print("You have", score, "Correct")
    print("You have", iscore, "Incorrect")
    print("")
    
#Print Question 2
print(questions2["question2"])
for choice in questions2["choices2"]:
    print(choice)
    
#Ask user to choose
user_answer2 = input("Enter your choice (A, B, or C): ")
    
#check answer
if user_answer2 == questions2["answer2"]:
    print("Correct.")
    score = score + 1
    print("You have", score, "Correct")
    print("You have", iscore, "Incorrect")
    print("")
else:
        print("Incorrect.")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("")
    #Print Question 3
print(questions3["question3"])

#code isnt working how it should so im inserting the choices manually
print("A. Activision")
print("B. Facepunch Studios")
print("C. Valve")
    
#Ask user to choose
user_answer3 = input("Enter your choice (A, B, or C): ")
    
    #check answer
if user_answer3 == "B":
    print("Correct.")
    score = score + 1
    print("You have", score, "Correct")
    print("You have", iscore, "Incorrect")
    print("Quiz OVER!")
    print("You ended the quiz with", score, "Correct and", iscore, "Incorrect!")
    input("")    
    
else:
        print("Incorrect.")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
    
        print("Quiz OVER!")
        print("You ended the quiz with", score, "Correct and", iscore, "Incorrect!")
        input("")    
