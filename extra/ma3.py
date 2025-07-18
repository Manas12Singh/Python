a = input("Enter a number (upto ten billion) : ")

l = len(a)

l1 = [ 'twenty' , 'thirty' , 'forty' , 'fifty' , 'sixty' , 'seventy' , 'eighty' , 'ninety' ]

l2 = [ 'one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine' , 'ten' , 'eleven' , 'twelve' , 'thirteen' , 'forteen' , 'fifteen' , 'sixteen' , 'seventeen' , 'eighteen' , 'nineteen' ]

a = ( '0' * ( 10 - l ) ) + a

b = '\033[1;32m'

if a[0] != '0' :
	b = b + l2[int(a[0]) - 1] + ' billion '

b += '\033[1;33m'

if a[1:4] != '000' :
	if a[1] != '0' :
		b = b + l2[int(a[1]) - 1] + ' hundred '

	if a[2:4] != '00' :
		if int(a[2:4]) < 20 :
			b += l2[int(a[2:4]) - 1]
		else :
			if a[3] != '0' :
				b = b + l1[int(a[2]) - 2] + '-' + l2[int(a[3]) - 1]
			else :
				b = b + l1[int(a[2]) - 2]
	b += ' million '

b += '\033[1;34m'

if a[4:7] != '000' :
	if a[4] != '0' :
		b = b + l2[int(a[4]) - 1] + ' hundred '

	if a[5:7] != '00' :
		if int(a[5:7]) < 20 :
			b += l2[int(a[5:7]) - 1]
		else :
			if a[6] != '0' :
				b = b + l1[int(a[5]) - 2] + '-' + l2[int(a[6]) - 1]
			else :
				b = b + l1[int(a[5]) - 2]
	b += ' thousand '

b += '\033[1;37m'

if a[7:10] != '000' :
	if a[7] != '0' :
		b = b + l2[int(a[7]) - 1] + ' hundred '

	if a[8:10] != '00' :
		if int(a[8:10]) < 20 :
			b += l2[int(a[8:10]) - 1]
		else :
			if a[9] != '0':
				b = b + l1[int(a[8]) - 2] + '-' + l2[int(a[9]) - 1]
			else:
				b = b + l1[int(a[8]) - 2]

print(b)