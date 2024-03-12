import json
data = json.load(
    open('simple_data.json')
)

def kwfunkca(ui):
    if ui in data.keys():
        return data[ui]
    else:
        return 'Podanego słownika {ui} nie ma słowniku'

user_input = input('Podaj wyraz:- ')

print(f'data from simple json:\n{data}')
print(f'The value(s) for keyword: {user_input} is/are {kwfunkca[user_input]}')
print(f'RESULT:\n{kwfunkca[user_input]}')
print(data.keys())