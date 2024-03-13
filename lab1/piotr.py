import json
data = json.load(
    open('simple_data.json')
)

def kwfunkca(ui):
    if ui in data.keys():
        return data[ui]
    else:
        return 'Podanego słownika {ui} nie ma słowniku'

word = input('Podaj wyraz:- ')
print(f'Podałes wyraz: {word}\n\n')
#print(f'data from simple json:\n{data}')
print(f'The value(s) for keyword: {word} is/are {kwfunkca[word]}')

print(f'RESULT:\n{kwfunkca[word]}')
#print(data.keys())