from datetime import datetime

notes = []

while True:
    note = input('Please enter your note. Hit "enter" for next line or hit "exit" to save your notes: ')
    if note == 'exit':
        break
    notes.append(note)

content = '\n'.join(notes)
day = datetime.now().strftime("%y-%m-%d")
file_name = f'{day}.txt'

with open(file_name, 'w') as f:
    f.write(content)

print(f'Notes was saved in diary as {file_name}')

