str1=input('enter ur first string: ')
str2=input('enter ur second string: ')
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print('anagram')
else:
    print('not anagram')

#two different word are said to be anagram if both will contain same letter

