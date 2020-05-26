#this function takes three numbers and tells you if they are a pythagorean triple

a,b,c = input("Enter three numbers separated by commas.I'll lyk if they're a triple:")
if(a*a + b*b == c*c):
  print "Yay a triple!"
else:
  print a,b,"and",c, "do not form a triple."
