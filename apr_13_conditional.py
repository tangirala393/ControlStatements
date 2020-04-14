'''
# check if string is palindram or not
k = input("enter the string to check:")

if k == k[::-1]:
    print("Palindram")
else:
    print("Not palindram")

#Percentage of marks

marks = int(input("enter the marks of student:"))


#if marks > 0 and marks<100:
 #   print("Valid marks")
    
if marks == 100:
    print("Grade A")
elif marks >= 90 and marks <=99:
    print("Grade B")
elif marks >= 80 and marks <=89:
    print("Grade C")
elif marks >= 70 and marks <=79:
    print("Grade D")
elif marks >= 50 and marks <=69:
    print("Grade E")
elif marks >= 0 and marks <=49:
    print("Grade F")
else:
    print("invalid")
    
##check whether first char, middle char, last char of a string is same or different

k = input("enter string:")
if k[0] == k[len(k)//2] == k[-1]:

    print("first,middle and last letters are same")
else:
    print("Not same")
    '''
