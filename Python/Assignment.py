# submit the questions 4,5,6,7,10 and 9 (without using files,) from the practical list.
# For Q10 store the data in a string and perform the operations given in the question.

# 4. Write a program that accepts a character and performs the following:
#   a. print whether the character is a letter or numeric digit or a special character.
#   b. if the character is a letter, print whether the letter is uppercase or lowercase
#   c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)
s=input("Enter char :")
d={"1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE","6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE"}
isup={True:"Upper",False:"Lower"}
if len(s)==1:
    if s.isdigit():
        print(f"Digit\n{d[s]}")
    elif s.isalpha():
        print(f"Letter\n{isup[s.isupper()]}")
    else:print("Special char")
else:print(f"{s}::is not a character its a string")


# 5. Write a program to perform the following operations on a string
# a. Find the frequency of a character in a string.
# b. Replace a character by another character in a string.
# c. Remove the first occurrence of a character from a string.
# d. Remove all occurrences of a character from a string.

s=input("Enter string :")
ch=input("frequency of a character in a string:")
print(s.count(ch))
oc=input("Replace a character by another character in a string\nchar to be replaced:")
nc=input("char that you want there:")
s=s.replace(oc,nc)
print(s)
wrc=input("Remove the first occurrence of a character from a string\nchar to be removed:")
s=list(tuple(s))
notfound=True
i=0
while notfound and i<=len(s)-1:
    if s[i]==wrc:
        del s[i]
        notfound=False
    i+=1
ts=""
for i in s:
    ts+=i
s=ts
print(s)
wsrc=input("Remove the first occurrence of a character from a string\nchar to be removed:")
s=s.replace(wsrc,"")
print(s)



# 6. Write a program to swap the first n characters of two strings.







# 7. Write a function that accepts two strings and returns the indices of all the occurrences of the
# second string in the first string as a list. If the second string is not present in the first string
# then it should return -1.



# 9. Write a program to read a file and
# a. Print the total number of characters, words and lines in the file.
# b. Calculate the frequency of each character in the file. Use a variable of dictionary type
# to maintain the count.
# c. Print the words in reverse order.
# d. Copy even lines of the file to a file named ‘File1’ and odd lines to another file named
# ‘File2’.



# 10. Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the
# values are cubes of the keys.