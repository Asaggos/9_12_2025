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


# #Askhsh 2

# def wordScore(s):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     mry = {'m','r','y'}
#     score = 0
#     for i in s:
#         if (i in vowels):
#             score += 2
#         elif i in mry:
#             score += 3
#         else:
#             score += 1
#     return score 

# x = wordScore(input("Dwse akolouthia xarakthrwn: "))
# print ("Score= ",x)

#Askhsh 3 

# def numWars(n1,n2):
#     numbers = []
#     for i in range (2, min(n1,n2) + 1): 
#         if n1 % i == 0 and n2 % i == 0:
#             numbers.append(i)
#     if len(numbers) >= 2:
#         return "Friends", numbers
#     else:
#         return "Enemies", numbers
    
# a = int(input("Dwse to n1: "))
# b = int(input("Dwse to n2: "))

# apotelesma, nums = numWars(a,b)
# print(apotelesma, "Arithmoi: ",nums)