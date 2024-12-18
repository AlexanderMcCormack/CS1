import random
Question_markings = ["who", "what", "when", "where", "which", "how", "will", "am", "is"]

while True:
    question = input("state your question")
    
    first_word = question.split()[0]
    if first_word in Question_markings:
        result = ["yes", "no", "maybe", "ask again later"]
        result =random.choice(result)
        print(result)
    else:
        print("no question asked")
    
