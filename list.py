# creating an empty list:
list=[]

# number of element as input
n=int(input("enter number of elements:"))


# iterating till the range
for i in range(0,n):
    ele=int(input())
    #adding the element
    list.append(ele)
print(list)
for i in range(len(list)):
          if list[i]>100:
             list[i]="over"
print(list)
