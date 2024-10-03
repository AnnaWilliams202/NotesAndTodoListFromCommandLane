from datetime import datetime

todo_items = []

while True:
    todo = input('Please enter To-Do or enter "done" to save and exit ')
    #todo_items.append(todo)
    if todo == 'done':
        break
    todo_items.append(todo)

content = '\n'.join(todo_items)
day = datetime.now().strftime('%A')
file_name = f'{day}.txt'

with open(file_name, 'w') as f:
    f.write(content)
print(f'Your todo list is saved as {file_name}')

