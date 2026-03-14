def count_vowels(string): 
    VOWELS = 'aioeuAIOEU'
    count = 0 
    for char in string: 
        if char in VOWELS: 
            count += 1 

    return count 
 
print(count_vowels('Hello, world'))
print(count_vowels('Python is a very powerful language'))


def count_vowels(string): 
    VOWELS = 'aioeyAIOEU'
    count = 0 
    for char in string: 
        if char in VOWELS:
            count += 1

    return count 

print(count_vowels('Hello, world'))
print(count_vowels('Python is a very powerful language'))