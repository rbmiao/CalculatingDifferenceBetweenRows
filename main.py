from bitsight_module import *

def main(inputfile):
	textfile = inputfile                  	# read in files which is processed..
	count = 1                               # count is current line
	failure = 0                             # how many numbers are NOT satisfy within [100,500]
	bufferLines = {}                        # save all lines 
	result_pass = []                        # numbers that are satisfied are put here
	result_fail = []                        # numbers that are not satisfied are put here

	with open(textfile, 'r') as fp:

		for line in fp.readlines():
			tmp = line.split(' ')   

			if(isOutScope(int(tmp[1]))):    # failed numbers are put in an array
				result_fail.append((int(tmp[0]), int(tmp[1]), "Number is not in (100,500) -- FAIL"))
				failure = failure + 1
			else:
				result_pass.append((int(tmp[0]), int(tmp[1]), "Pass"))

		
			if failure > 0:                 # If there is a failed number, exit immediately
				print("\nSome numbers is out of range, existing...")
				exit(0)
			
		
			else:                           # Otherwise trying to calculating them
				bufferLines[count] = line
				number = line.split(' ')
			
		   
				if count == 1:              # No action on first line, just print it.
					print("%4d\t%4d" % (count, int(number[1])))
				

				# Calculation starts from second line
				# 
				if count > 1:               # number in current line(bufferLines[count]) substract
											# number in previous line (bufferLines[count-1])
					number1 = bufferLines[count-1].split(' ')
					number2 = bufferLines[count].split(' ')

					## define result's positive or negative 
					if number1[1] < number2[1]:
						result = "POSITIVE"
					else:
						result = "negative"

					print("%4d\t%4d\t%.2f%%\t (%s %% difference between %4d ->%4d)" % (count, int(number2[1]), (int(number2[1])-int(number1[1]))/int(number1[1])*100.0, result, int(number1[1]), int(number2[1]) ))

				# Move to next line
				count = count + 1
