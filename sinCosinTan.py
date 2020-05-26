#This program prints a sine cosine and tangent table
import math
count = 0
while(count <= 3):
  print math.sin(count), "\t", math.cos(count), "\t", math.tan(count)
  count+=.1
