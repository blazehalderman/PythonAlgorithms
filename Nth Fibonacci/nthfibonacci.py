  """
  The Fibonacci sequence is defined as follows: the first number of the sequence
  is 0, the second number is <span>1</span>, and the nth number is the sum of the (n - 1)th
  and (n - 2)th numbers. Write a function that takes in an integer
  n and returns the nth Fibonacci number.
  """

def getNthFib(n):
    tmp1 = 0
    tmp2 = 1
    if(n == 1):
    	return 0
    elif (n == 2):
    	return 1
    else:
    	n-=2
    while (n > 0):
    	tmp_sum = tmp1 + tmp2
    	tmp1 = tmp2
    	tmp2 = tmp_sum
    	n -= 1
    return (tmp_sum)
