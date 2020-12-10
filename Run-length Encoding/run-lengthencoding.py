"""
  Write a function that takes in a non-empty string and returns its run-length
  encoding.


  From Wikipedia, "run-length encoding is a form of lossless data compression in
  which runs of data are stored as a single data value and count, rather than as
  the original run." For this problem, a run of data is any sequence of
  consecutive, identical characters.
"""

def runLengthEncoding(string):
    # Write your code here.
	char = None
	count_values = []
	count = 1
	i = 1
	new_string = ""
	char = string[0]
	print(str(len(string)))
	while(i < len(string)):
		#if hit a same character continue
		if(string[i] == char):
			count += 1
			if(count % 9 == 0):
				new_string += str(count) + char
				count = 0
		if(i == len(string) - 1 or string[i] != char):
			count_values.append(count)
			new_string += str(count) + char
			char = string[i]
			count = 1
		i += 1 
	return(new_string)
