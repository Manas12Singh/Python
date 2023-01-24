import numpy as np
import math

class Complex:
	def __init__(self,x=0,y=0):
		self.real = round(x,2)
		self.imag = round(y,2)
		self.__mod=round(((self.real)**2+(self.imag)**2)**0.5,2)

	def __repr__(self):
		if self.imag == 0:
			return "Complex number: " + str(self.real)
		elif self.real == 0:
			return "Complex number: " + str(self.imag) + ' i'
		elif self.imag < 0:
			return "Complex number: " + str(self.real) + ' - ' + str(self.imag*-1) + ' i'
		else:
			return "Complex number: " + str(self.real) + ' + ' + str(self.imag) + ' i'
	def modulus(self):
		return "Modulus: " + str(self.__mod)
	def polar(self):
		sf = math.degrees(math.asin(self.imag/self._Complex__mod))
		cf = math.degrees(math.acos(self.real/self._Complex__mod))
		return str(self._Complex__mod) + "(cos" + str(round(cf)) + " + isin" + str(round(sf)) + ")"
	def conjugate(self):
		if self.imag < 0:
			return "Conjugate: " + str(self.real) + ' + ' + str(self.imag*-1) + 'i'
		else:
			return "Conjugate: " + str(self.real) + ' - ' + str(self.imag) + 'i'

p = Complex(-10,10)

print(p.conjugate())