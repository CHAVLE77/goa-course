integer_list=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(integer_list)):
    print(integer_list[i] * integer_list[1])
    
    print(integer_list[i]+ integer_list[2])

    print(integer_list[i] / integer_list[3])
    
    print(integer_list[i] - integer_list[2])


letters=["a","b","c","d","e"]

for i in letters:
    print(i)

    letters[0]="f"
    print(letters)


num=[1,2,3,4,5,6,7,8,9]
index=int(input("please enter your value: "))
print(index)