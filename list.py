# Given A list of letters, output a new list that only contains a single copy of each letter.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

Alist = ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
Blist = []
for letter in Alist:
    if letter in Blist:
       continue 
    else:
        Blist.append(letter)
print(Blist)
            