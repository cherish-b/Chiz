#task 1
def rocks():
	print("girls who code rocks!")

# for i in range(77):
# 	rocks()

#task 2
def custom_message(answer):
	answer = input("What do you want to say?")
	print(answer)
# custom_message(input)

#task 3
def adding():
	c = (a+b)
	return c
def subtracting(a,b):
	c = (a-b)
	return c
def multiplying(a,b):
	c = (a*b)
	return c
def dividing(a,b):
	c = (a/b)
	return c
# print(adding(int(input("Enter a number.")), subtracting(int(input("Enter a number.")))
# a = int(input("Enter a number."))
# b = int(input("Enter a number."))
# c = int(input("Another number."))

# print(adding())
# print(multiplying(a,b))
a = []
number = int(input("How many numbers would you like to add?"))
for i in range(number):
	answer = int(input("Give me a number."))
	a.append(answer)
# [0,1,2,3,4,5,6,7,8,9]
b = sum(a)
print(b)