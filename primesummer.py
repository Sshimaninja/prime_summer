from random import choice
# import prime finding module
from sympy import isprime

# Make a class to initialize variables, hold the logic and get user input
class PrimeSummer:
	def __init__(self, minimum: int, maximum: int):
		self.emptycnt = 0
		# Create list of primes in the range
		self.primes = list(filter(isprime, range(minimum, maximum)))
		if len(self.primes) == 0:
			raise ValueError("No primes in provided range.")
		# Generate random prime numbers
		self.n = choice(self.primes)
		self.d = choice(self.primes)
		# Calculate sum
		self.r = self.n + self.d
		
	# Get user input
	def getInput(self, prompt):
		
		while True:
			# handle errors
			try:
				uinput = input(prompt)
				# handle numbers
				if uinput.isdigit():
					return round(int(uinput))
				# handle blank/null entries
				if uinput == "":
					self.emptycnt += 1
					# set defaults to specified parameters in the brief
					if self.emptycnt == 1:
						return 10000
					elif self.emptycnt == 2:
						return 20000
				# handle text
				else:
					byteSum = sum(ord(char) for char in uinput)
					return byteSum
				# handle any unexpected errors
			except Exception as e:
				print(f"Invalid input: {e}. Please input an ASCII value.")
			
	def output(self):
		# Create user-friendly output string
		string = (
		" 1st input number: "
		+ str(n0)
		+ "\n 2nd input number: "
		+ str(n1)
		+ "\n 1st random prime: "
		+ str(self.n)
		+ "\n 2nd random prime: "
		+ str(self.d)
		+ "\n Sum: "
		+ str(self.n)
		+ " + "
		+ str(self.d)
		+ " = "
		+ str(self.r)
		+ "\nNotes: \n All input rounded to nearest integer. \n All non-numerical characters translated to bytecode sums."
	)
		return string

print("Welcome to Prime Summer")

# Initiate default values. This is also reflected in blank value entry, but since a class needs to be initialized, I decided on these for default values
primesummer = PrimeSummer(10000, 20000)

# Createe a loop to get user input that breaks only when input is not identical
while True: 
	n0 = primesummer.getInput("Enter any number: ")
	n1 = primesummer.getInput("Enter any other number: ")
	if n0 != n1:
		break
	print("Input numbers must be different")

# Order the inputs in ascending order
minimum = min(n0, n1)
maximum = max(n0, n1)

# Reassign class variables to inputs, loop until a prime is found
while True: 
	try:
		primesummer = PrimeSummer(minimum, maximum)
		break
	# handle value error in which no primes are in the range
	except ValueError as e:
		#print(e)
		n1 = primesummer.getInput("Please input a new end-of-range: ")
		minimum = min(n0, n1)
		maximum = max(n0, n1)

print(primesummer.output())

