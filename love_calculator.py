
//Bishal Kumar
print(" !! Welcome to the Love Calculator !!")
name1 = input("Enter your name: \n")
name2 = input("Enter his/her name: \n")
combine_name = name1 + name2
f1 = combine_name.lower()

t = f1.count("t")
r = f1.count("r")
u = f1.count("u")
e = f1.count("e")
sum1 = t + r + u + e

l = f1.count("l")
v = f1.count("v")
o = f1.count("o")
e = f1.count("e")
sum2 = l + o + v + e

love_score = str(sum1) + str(sum2)
print(f"Your Love Score is {love_score}")
