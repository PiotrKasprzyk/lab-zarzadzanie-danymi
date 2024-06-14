import json
#rys.1
data = json.load(
    open('simple_data.json', "r", encoding="utf-8")
)
print(f'data from simple json:\n{data}')
#rys.2, rys.3
search_key = input("Podaj wyraz: ")

def print_key_value(key, json):
    if key in json:
        print(f"{json[key]}")
    else:
        print(f"Wyraz = {key} nie istnieje w pliku")

print_key_value(search_key, data)
#rys.4
print("Rys.4")
search_key = input("Podaj wyraz: ")

def to_lower_case(key):
    if type(key) is str:
        return key.lower()

print_key_value(to_lower_case(search_key), data)

# Rys.5 

print("Rys.5")
import difflib

print(difflib.SequenceMatcher(None, "stanowisko", "stano").ratio())

# Rys.6
# Rys.7
# Rys.7B
print("Rys.6, Rys.7, Rys.7B")

def find_matching_key(key, json):
    for k in json.keys():
        if difflib.SequenceMatcher(None, k, key).ratio() > 0.7:
            print(f"Czy chciałeś podać {k}? Podaj T lub N")
            answer = input()
            if answer == "T":
                return print_key_value(k, json)
            if answer == "N":
                print("ok... 0_0")

print(find_matching_key(search_key, data))
# Rys.8
print("Rys.8")
search_key = input("Podaj wyraz: ")

def print_array(array):
    for i in range(len(array)):
        print(f"{array[i]}")

def print_key_value_for_array(key, json):
    if key in json:
        if type(json[key]) is list:
            print_array(json[key])
        else:
            print(f"{json[key]}")
    else:
        print(f"Wyraz = {key} nie istnieje w pliku")

print_key_value_for_array(search_key, data)    

# Rys.9
print("Rys.9")
search_key = input("Podaj wyraz: ")

data_file = open("./data.json", "r", encoding="utf-8")
file = json.load(data_file)

print_key_value(search_key, file)

# Rys.10
print("Rys.10 ")
search_key = input("Podaj wyraz: ")

print_key_value(search_key, file)