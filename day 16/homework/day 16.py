def initial_chars(fullname):
    splited_fullname = fullname.split(" ")
    
    firstname = splited_fullname[0]
    lastname = splited_fullname[1]
    
    result = firstname[0] + "." + lastname[0]
    
    print(result)
   

initial_chars("Nika Chavleishvili")



def average_arithmetic(number_list):
    jami = sum(number_list)
    result = jami // len(number_list)
    print(result)

average_arithmetic([1,2,3])




def palindrom(word):
    reversed_word = ''
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]
    
    print(reversed_word == word)


palindrom("nika")



def remove_spaces(word):
    word_without_space = ''
    
    for i in word:
        if i != " ":
            word_without_space = word_without_space + i
    
    print(word_without_space)

remove_spaces("Nika Chavleishvili")




def num(number_list):
    num1=0
    num2=0
    
    for i in number_list:
        if i >= 0:
            num1= num1 + i
        else:
            num2 = num2 + 1
    
    print(num1,num2)

num([1,2,3,-4,-5,-6])