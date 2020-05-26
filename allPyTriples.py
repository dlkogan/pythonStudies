#All Pythagorean Triples of positive numbers less than or equal to 20

for i in (0,20):
  for j in (i, 20):
    for k in (j,20):
      if((i*i) + (j*j) == k*k):
        print i, j, "and", k, "are a pythagorean triple"
