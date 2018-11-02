longest_word = ''
my_people = ['ben', 'lauren', 'estelle', 'shiba']
for name in my_people:
    if len(name) > len(longest_word):
        longest_word = name
print(longest_word)
