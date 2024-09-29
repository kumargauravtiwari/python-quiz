quiz = {
    "question1":{
        "question":"what is the capital of India?",
        "answer":"Delhi"
    },
     "question2":{
        "question":"what is the capital of France?",
        "answer":"paris"
    },
     "question3":{
        "question":"what is the capital of Germany?",
        "answer":"berlin"
    },
     "question4":{
        "question":"what is the capital of Italy?",
        "answer":"Rome"
    },
     "question5":{
        "question":"what is the capital of Spain?",
        "answer":"Madrid"
    },
     "question6":{
        "question":"what is the capital of Portugal?",
        "answer":"Libson"
    },
     "question7":{
        "question":"what is the capital of Afganistan?",
        "answer":"Kabul"
    },
     "question8":{
        "question":"what is the capital of Switzerland?",
        "answer":"Bern"
    },
     "question9":{
        "question":"what is the capital of Pakistan?",
        "answer":"Karachi"
    },
     "question10":{
        "question":"what is the capital of Bangladesh?",
        "answer":"Dhaka"
    },
}
score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower()==value['answer'].lower():
        print("correct")
        score +=1
        print("your score is: "+ str(score))
        print("")
        print("")
    else:
        print("wrong!")
        print("The answer is :"+ value['answer'])
        print("your score is: "+ str(score))
        print("")
        print("")

print("you got " + str(score)+"out of 10 question correctly")

print("your percentage is " + str(int(score/10 *100))+"%")


