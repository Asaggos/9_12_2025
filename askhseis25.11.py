# #Askhsh 1

# def whatVowels(s):
#     vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
#     s1 = []
#     for i in s.lower():
#         if i in vowels:
#             s1.append(i)
#     return s1

# leksh = whatVowels(input("Dwse leksh: "))
# print ("".join(leksh))


#Askhsh 2

def wordScore(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    mry = {'m','r','y'}
    score = 0
    for i in s:
        if (i in vowels):
            score += 2
        elif i in mry:
            score += 3
        else:
            score += 1
    return score 

x = wordScore(input("Dwse akolouthia xarakthrwn: "))
print ("Score= ",x)