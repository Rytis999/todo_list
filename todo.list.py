print('Welcome to Todo_list')

to_do = []

while True:
    # Įrašyti iki 5 užduočių
    count = len(to_do)  # Nuskaičiuojame kiek jau yra užduočių
    while count < 5:
        user_input = input('Enter your todo list: ')
        to_do.append(user_input)
        count += 1

        print(f'Your todo list is: {to_do}')
        for idx,  task in enumerate(to_do, start=1):
            print(f'{idx}. {task}')
            
        

    # Paklausti, ar vartotojas nori pašalinti užduotį
    question = input('Do you want to delete a task? (y/n): ').strip().lower()
    if question == 'y':
        delete_task = input('Enter a task you have completed: ')
        if delete_task in to_do:
            to_do.remove(delete_task)
            print(f'Task "{delete_task}" removed.')
        else:
            print(f'Task "{delete_task}" not found in your list.')

    # Paklausti, ar vartotojas nori pridėti dar ką nors
    question2 = input('Maybe you want to add something? (y/n): ').strip().lower()
    if question2 == 'y':
        user_input1 = input('Enter a task to add: ')
        to_do.append(user_input1)

    # Jei vartotojas nenori nei pridėti, nei ištrinti, baigti programą
    continue_program = input('Do you want to continue managing your tasks? (y/n): ').strip().lower()
    if continue_program != 'y':
        break

print(f'Your final todo list is: {to_do}')

