"""
Q Squared Solutions Technical Assessment Task 1
Kyle Pickford

The function 'Qcount' below completes the required calculations.
It takes in a single string which it expects to be valid data. 
An empty string is acceptable. Python limits max string length by 
system data.
It classifies whitespace characters as 'other'.'

Below it is 'Qresult' which prints the results in an easy to read output.

Further below that is a main which uses the previous two functions in console for testing.
Note: main function requires use of quotations in terminal.
"""

def Qcount(instring=""):
	#The below variables track the number of A's, C's G's T's and other characters
	As, Cs, Gs, Ts, others, = 0, 0, 0, 0, 0
	
	#The below variables track the highest consecutive number of the given letter
	consecutiveA, consecutiveC, consecutiveG, consecutiveT = 0, 0, 0, 0
	
	#consecutiveFlag tracks the preceding character's value for consecutive tracking
	#Uses an integer instead of 4 boolean flags
	#1 = preceding A, 2 = preceding C, 3 = preceding G, 4 = preceding T, 0 = other
	consecutiveFlag = 0
	
	#The program passes through the string once for O(n) complexity
	#It goes character, branching off depending on value
	for char in instring:
		if char == 'a' or char == 'A':				#Once a character is matched
			As += 1									#its count is incremented.
			if consecutiveFlag == 1:				#If it matches the last character,
				tempA += 1							#the consecutive tracker is incremented.
			else:
				consecutiveFlag = 1					#Otherwise the flag is updated
				tempA = 1							#and consecutive tracking begins.
			if tempA > consecutiveA:				#If the current consecutive tracker
				consecutiveA = tempA				#exceeds the previous max, it replaces it
		elif char == 'c' or char == 'C':
			Cs += 1
			if consecutiveFlag == 2:
				tempC += 1
			else:
				consecutiveFlag = 2
				tempC = 1
			if tempC > consecutiveC:
				consecutiveC = tempC
		elif char == 'g' or char == 'G':
			Gs += 1
			if consecutiveFlag == 3:
				tempG += 1
			else:
				consecutiveFlag = 3
				tempG = 1
			if tempG > consecutiveG:
				consecutiveG = tempG
		elif char == 't' or char == 'T':
			Ts += 1
			if consecutiveFlag == 4:
				tempT += 1
			else:
				consecutiveFlag = 4
				tempT = 1
			if tempT > consecutiveT:
				consecutiveT = tempT
		else:
			others += 1
			consecutiveFlag = 0
			
	#Percentages of total are calculated
	sumAll = As + Cs + Gs + Ts + others
	sumAll = max(1, float(sumAll))
	percentA = As / sumAll * 100
	percentC = Cs / sumAll * 100
	percentG = Gs / sumAll * 100
	percentT = Ts / sumAll * 100
	percentO = others / sumAll * 100
	
	return([As, Cs, Gs, Ts, others, percentA, percentC, percentG, percentT, 
		percentO, consecutiveA, consecutiveC, consecutiveG, consecutiveT])
	
def Qresult(results=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
	print("The number of A's (upper or lower case): {}".format(results[0]))
	print("The number of C's (upper or lower case): {}".format(results[1]))
	print("The number of G's (upper or lower case): {}".format(results[2]))
	print("The number of T's (upper or lower case): {}".format(results[3]))
	print("The number of other characters: {}".format(results[4]))
	print("Percentage A's (upper or lower case): {} %".format(results[5]))
	print("Percentage C's (upper or lower case): {} %".format(results[6]))
	print("Percentage G's (upper or lower case): {} %".format(results[7]))
	print("Percentage T's (upper or lower case): {} %".format(results[8]))
	print("Percentage other characters: {}".format(results[9]))
	print("The greatest number of consecutive A's (upper or lower case): {}".format(results[10]))
	print("The greatest number of consecutive C's (upper or lower case): {}".format(results[11]))
	print("The greatest number of consecutive G's (upper or lower case): {}".format(results[12]))
	print("The greatest number of consecutive T's (upper or lower case): {}".format(results[13]))
	
def main():
	testIn = input("Please enter your test string: ")
	testResults = Qcount(testIn)
	Qresult(testResults)

if __name__ == "__main__":
	main()
