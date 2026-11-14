import random

choices = ['r','p','s']

choice_menaning = {
    'r' : 'Rock' ,
    'p' : 'paper',
    's' : 'scissors'
}

user_score = 0
ai_score = 0
final_number = 5

while True:
        
    user_choice = input('Select from Rock , Paper , Scissors: (r,p,s): ')

    ai_choices = random.choice(choices)

    if user_choice in choices:
        print(f'your choice is {choice_menaning[user_choice]}. AI choice is {choice_menaning[ai_choices]}')
        # r > s , p > r , s > p
        if user_choice == ai_choices:
            print('tie')
        elif user_choice == 'r' and ai_choices== 's' :
            print('user+1!')
            user_score +=1
        elif user_choice == 'p' and ai_choices == 'r':
            print ('user+1!')
            user_score +=1
        elif user_choice == 's' and ai_choices == 'p':
            print ('user+1!')
            user_score +=1
        else :
            print('Ai+1')
            ai_score += 1
    else:
        print('Invalid input')
        
    print(f'User score: {user_score} / AI score: {ai_score}')
    
    if user_score == final_number or ai_score == final_number :
        break
    
    print('\n', '-'*15 , '\n')
    
if user_score == final_number:
    print(f'User won with score: {user_score}')
else:
    print(f'AI won with score: {ai_score}')
    
    