
import random

print('Welcome to Magic 8-Ball')

while True:

    print('enter your Question')
    question = input('> ')


    print("you're question is...",question)
    answers = [
        'YES.',
        'NO.',
        'could happen.',
        'possibly.',
        'lets find out.',
        'I will be waiting.',
        'Best not to know.',
        'oh,s*** no!.',
        'you bet.',
        'shut up',
        'back off.',
    ]

    answer = random.choice(answers)
    print(answer)
