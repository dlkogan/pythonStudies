#This program takes three strings and returns in dictionary Order

print("Hello! Your 3 strings will be returned in dictionary order")
str1 = raw_input("Enter string One:")
str2 = raw_input("Enter string Two:")
str3 = raw_input("Enter string Three:")
unsortedList = [str1, str2, str3]
unsortedList.sort()
#if str1 is less than str2, swap
#if str1 is less than str3, swap

print("These strings in dictionary order are...")
for i in unsortedList:
  print(i)

