"""
  Write a function that takes in a non-empty string and returns its run-length
  encoding.


  From Wikipedia, "run-length encoding is a form of lossless data compression in
  which runs of data are stored as a single data value and count, rather than as
  the original run." For this problem, a run of data is any sequence of
  consecutive, identical characters.
"""

def runLengthEncoding(string):
	count = 1
	new_string = ""
	print(str(len(string)))
	for i in range(1, len(string)):
		char = string[i - 1]
		if(string[i] != char or count % 9 == 0):
			new_string += str(count) + char
			count = 0
		count += 1
	new_string += str(count) + string[len(string) - 1]
	return(new_string)
