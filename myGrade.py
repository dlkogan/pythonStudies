#this program will tell you how good your grade is!

totalPoints = input("How many points did the test have?")
yourPoints = input("And how many did you get?")
yourScore = (yourPoints * 100)/totalPoints
if(yourScore >= 90.0):
  print "You are incredible! A!!"
elif(yourScore >= 80.0):
  print "Pretty cool! B!!"
else:
  print "whatever"
