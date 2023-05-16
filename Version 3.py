#Version 3

def function():
    #Scoreboard
    score = 0
    score = int(score)
    iscore = 0
    iscore = int(iscore)
    
    #Start Quiz
    input("Press enter to start!")
    print("")
    
    #welcome the user
    print("Welcome to Version 2 of the quiz")
    
    #Question List
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
    questions4 = {
        "question4": "Which company owns the video game Counter Strike: Global Offense?",
        "choices4": ["A. Valve", "B. Activision", "C. Epic Games"],
        "answer4": "A"
    }
    
    questions5 = {
        "question5": "Which company owns the video game franchise Assassin's Creed?",
        "choices5": ["A. Rockstar Games", "B. Nintendo", "C. Ubisoft"],
        "answer5": "C"
        }

    #Print Question 1
    print(questions1["question1"])
    for choice in questions1["choices1"]:
        print(choice)
    
    #Ask user to answer question1
    user_answer1 = input("Enter your choice (A, B or C): ")
    
    #check answer 1 and give score
    if user_answer1 == questions1["answer1"]:
        print("That is Correct.")
        score = score + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")    
        print(" ")
    else:
        print("Sorry, Incorrect.")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("")
        
    #print question 2
    print(questions2["question2"])
    for choice in questions2["choices2"]:
        print(choice)
    
    #Ask user to answer quesiton 2
    user_answer2 = input("Enter your choice (A, B or C): ")
    
    #check answer 2 and give the score
    if user_answer2 == questions2["answer2"]:
        print("That is correct. ")
        score = score + 1
        print("you have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print(" ")
    else:
        print("Sorry, incorrect.")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print(" ")
    #print question 3
    print(questions3["question3"])
    for choice in questions3["choices3"]:
        print(choice)
              
    #ask user to answer question 3
    user_answer3 = input("Enter your choice (A, B or C): ")
    
    #check answer 3 and give the score
    if user_answer3 == questions3["answer3"]:
        print("That is correct. ")
        score = score + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("")
    else:
        print("Sorry, incorrect.")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print(" ")

    print(questions4["question4"])
    for choice in questions4["choices4"]:
        print(choice)
        
    #ask user to answer question 4
    user_answer4 = input("Enter your choice (A, B or C): ")
    
    #check answer 4 and give the score
    if user_answer4 == questions4["answer4"]:        
        score = score + 1
        print("That is correct ")
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("")
    else:
        print("Sorry, Incorrect. ")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("")
    
    print(questions5["question5"])
    for choice in questions5["choices5"]:
        print(choice)
        
    #ask user to answer question 5
    user_answer5 = input("Enter your choice (A, B or C): ")
    
    #check answer 5 and give the score
    if user_answer5 == questions5["answer5"]:           
        score = score + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("Quiz OVER!")
        print("You ended the quiz with", score, "Correct and", iscore, "Incorrect!")
        print("Would you like to restart the quiz?")
        restart = input(" ")
        if restart == "Yes":
            function()
        else:
            print("Thank you for your time")

    
    else:
        print("Sorry, Incorrect.")
        iscore = iscore + 1
        print("You have", score, "Correct")
        print("You have", iscore, "Incorrect")
        print("Quiz OVER!")
        print("You ended the quiz with", score, "Correct and", iscore, "Incorrect!")
        print("Would you like to restart the quiz?")
        restart = input(" ")
        if restart == "Yes":
            function()
        else:
            print("Thank you for your time")
        
        
    
function()