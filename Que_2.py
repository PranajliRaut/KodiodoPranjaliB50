
string=input("enter the string")
vowel=["A","E","I","O","U","a","e","i","o","u"]
a=0
for i in (string):
    if i in vowel:
        a+=1
print('number of vowel :-',a)
