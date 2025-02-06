
welcome = 'Guten Tag'
answer_bot = 'Dummyantwort'
quit = 'stop'
question = 'Und weiter?'
answer =''
print(welcome)
while answer.lower() != quit: 
    answer = input(question)
    print(answer_bot)
