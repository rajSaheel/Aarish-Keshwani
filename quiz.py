def start_quiz():
    score=0
    test=[
        {
            "question":"Who is the president of the United States?",
            "options":["Obama","Bush","Trump","Biden"],
            "answer":"Trump",
            "number":"1"
        },       
        {
            "question":"What is 12*6?",
            "options":["60","72","108","84"],
            "answer":"72",
            "number":"2"
        },
        {
            "question":"What year was the Declaration of Independence signed?",
            "options":["1780","2000","1776","1820"],
            "answer":"1776",
            "number":"3"
        }
    ]
    for quiz in test:
        print(quiz["number"],quiz["question"])
        for option in quiz["options"]:
            print(option)
        response=input("Your response: ")
        if response.lower()==quiz["answer"].lower():
            print("Correct answer.")
            score=score+33.33
        else:
            print("Wrong answer.")
    print("You have scored", score)   
print("Welcome to the quiz.")
username="quizuser123"
password="quiz123"
user=input("Enter the username: ")
if user==username:
    pwd=input("Enter the password: ")
    if pwd==password:
        start_quiz()
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")
