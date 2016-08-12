


class Cat():
	def __init__ (self, furcolor, name, eyecolor):
		self.furcolor = furcolor
		self.name = name
		self.eyecolor = eyecolor

	def meow(self):
		print("Meow!")

	def returnfur_color(self):
		return self.furcolor

	def eating(self):
		print("Yum!")

	def joke(self):
		print("Knock Knock!")
		input()
		print("Boo.")
		input()
		print("It's just a joke why are you crying? :)")

	def joke2(self):
		print("Why did the chicken cross the road?")
		input()
		print("To get to the idiot's house.")
		print("Knock Knock")
		input()
		print("The chicken.")
		print("Gonna need some ointment for that burn broooo!")
	def joke3(self):
		print
	def joke4(self):
		print("Knock Knock")
		input()
	def returneye_color(self):
		return self.eyecolor

	def return_name(self):
		return self.name
	def laughing(self):
		print("HAHAHA I'M SOOO FUNNY!")
	def entertain(self):
		answer = input("Do you wanna hear another joke?") 
		if answer == "Yes":
			self.joke2()
		answer = input("Do you wanna hear another joke?") 
		if answer == "Yes":
			self.joke3()
		answer = input("Do you wanna hear another joke?") 
		if answer == "Yes":
			self.joke4()
Tom = Cat("gray", "Tom", "green")
Tom.meow()
Tom.eating()
Tom.joke()
Tom.laughing()
Tom.entertain()