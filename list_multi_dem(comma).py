groups = [
["a","b","c","d"],
["e","f","g","h"],
["i","j","k","l"],
]

"""i=0
j=0
for word in group:
    for one in word:
        new = ', '.join(group[i][j])
        j += 1
        print (new)
    i += 1 """

#for group in groups:
#    print(", ".join(group), end = ", ")

print('\n')


for group in groups.copy():
    groups.remove(group)
    print(", ".join(group), end="")
    if groups != []:
        print(end = ", ")


print('\n')

#for group in groups:
#   print(", ".join(group))

print('Heeeeeeello')
