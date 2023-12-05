list=[-1,2,-3,4,-5,6]
positive_number=[num for num in list if num>0]
print("positive",positive_number)

N=5
squares=[i**2 for i in range(1,N+1)]
print("squares up to N",squares)

word='HELLO WORLD'
vowels=[char for char in word if char]
print("vowels",vowels)

word='HELLO WORLD'
ordinal_values=[ord(char)for char word]
print("ordinal values",ordinal_values)