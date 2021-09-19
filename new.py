name = input("what's your name?: ")

age =input("how old are you?: " )

place = input( "where do you live?: " )

love = input( "what do you love?: ")

string = "you name is {},your age is {},you live in {} and you love {}"
output = string.format(name,age,place,love)
print(output)
