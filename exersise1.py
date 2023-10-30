""" 1. Write a python function called fizzbizz which will take a
       number n as input and print numbers i from 1 to n. 
        a. If i is divisible by 3, it will print fizz instead
           of i
        b. If i is divisible by 5, it will print bizz instead
           of i
        c. If i is divisible by 15, it will print fizzbizz
           instead i
        d. Otherwise, it will just print i """

# def fizzbizz(self):
#     n=int(input("enter a number"))
#     for i in range(1,n+1):
#         if i%15 == 0 : print("fizzbizz")
#         elif i%3 == 0 and i%15 !=0: print("fizz")
#         elif i%5 == 0 and i%15 !=0:print("bizz")
#         else:print(i," ")

# fizzbizz(" ")



"""Write a python function called palindrome that receives a string s as an
       argument. It will return True if s is a palindrome and False if
       not. A palindrome is a word that will read the same from left
       to right and right to left. e.g. "dad", "abba"""
  

# def palindrome(word):
#     reversedword=word[::-1]
#     if word == reversedword :print(True)
#     else: print(False) 
        



# palindrome("malayalam")
# palindrome("nivin")
# palindrome("sita")


"""Write a python function called panagram that receives a string s as an
       argument. It will return True if s is a panagram and False if
       not. A panagram is a sentence that contains all letters of the
       alphabet. e.g. "the quick brown fox jumps over the lazy dog" """


# def panagram(string):

#     stringList=list(string.lower())
#     stringSet=set(stringList)
#     panagramList=[]
    
#     for i in stringSet:
#         if  i in "abcdefghijklmnopqrstuvwxyz" :
#             panagramList.append(i)
    
#     if len(panagramList) == 26: print(True)
#     else: print(False)
        

        


# panagram("the quick brown fox @ jumps over the lazy dog")
    
""" Write a function freq that will take a string s as input and
       return a dictionary. The keys of the dictionary will be the
       characters in s and the values will the number of times each of
       the characters occurs in s. Implement this without using the
       .count method of strings. (ie. s.count()) """

def freq(string):

    
    

    frequencyDict = {}

    for i in string:
        if i not in frequencyDict.keys():
            frequencyDict[i] = 1
        else :
            frequencyDict[i] += 1
    print(frequencyDict)

    





freq("fjha gsfs vs##7EB")




    


