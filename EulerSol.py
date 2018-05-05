# Solution to the archived problems of Project Euler

# Libraries imported
from math import sqrt
import fractions
import time

# Problem 1 : Multiples of 3 and 5 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def mul_3_5_sum(arr):
	start = time.time()
	total = 0
	for i in arr:
		if (i % 3 == 0) and (i % 5 == 0):
			total += i
		elif (i % 3 == 0):
			total += i
		elif (i % 5 == 0):
			total += i
		else:
			pass

	return total, time.time() - start 

p = 1
result, total_time = mul_3_5_sum(range(0,1000))
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))

# Problem 2 : Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def even_fibonacci(arr):
	start = time.time()
	x = arr
	i = total = 0
	while (x[len(x)-1] < 4000000):
		x.append(x[i]+x[i+1])
		i += 1
	x.pop()

	for j in x:
		if j % 2 == 0:
			total += j
		else:
			pass

	return total, time.time() - start

p += 1
result, total_time = even_fibonacci([1,2])
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))

# Problem 3: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_factor(num):
	start = time.time()
	factors = []
	if num % 2 == 0:
		factors.append(2)

	for i in range(3, int(sqrt(num))):
		flg = 0
		if num % i == 0:
			for prime in factors:
				if i % prime == 0:
					flg = 1 
			
			if flg == 0:
				factors.append(i)
		i += 2

	return max(factors), time.time() - start

p += 1
result, total_time = prime_factor(600851475143)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))

# Problem 4: Largest Palinrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome(n):
	start = time.time()
	upper_limit = 0
	for i in range(0, n):
		upper_limit *= 10
		upper_limit += 9

	lower_limit = 1 + upper_limit//10
	
	max_product = 0
	for i in range(upper_limit, lower_limit-1, -1):
		for j in range(i, lower_limit-1, -1):
			product = i*j
			if product < max_product:
				break

			number = product
			reverse = 0

			while number != 0:
				reverse = number % 10 + reverse*10
				number = number//10

			if reverse == product and product > max_product:
				max_product = product
				
	return max_product, time.time() - start				

p += 1
result, total_time = largest_palindrome(3)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))


# Problem 5: Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(nums, technique):
	start = time.time()
	if technique == "normal":
		multiple = 2
		while True:
			multiple += 1
			for x in nums:
				if multiple % x != 0:
					break
				else:
					multiple *= x
					if x == max(nums):
						return multiple
	elif technique == "gcd":
		multiple = 2
		for i in nums:
			multiple = (multiple*i)/fractions.gcd(multiple, i)

		return int(multiple), time.time() - start

p += 1
result, total_time = smallest_multiple(list(range(2,21)), "gcd")
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))


# Problem 6: Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_sq_diff(nums):
	start = time.time()
	sum_sq = sq_sum = 0
	for i in nums:
		sum_sq += i**2
		sq_sum += i

	return (sq_sum**2 - sum_sq, time.time() - start)

p += 1
result, total_time = sum_sq_diff(list(range(1,101)))
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))


# Problem 7: 10001st Prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def _10001prime(n):
	start = time.time()
	while True:
		prime_list = [True for i in range(n+1)]
		p = 2
		prime_l = []
		while (p*p < n):
			if (prime_list[p] == True):
				for i in range(p*2, n+1, p):
					prime_list[i] = False
			p += 1

		for prime in range(2, n+1):
			if prime_list[prime]:
				prime_l.append(prime)

		if len(prime_l) >= 10001:
			break
		else:
			n *= 10
	
	return prime_l[10000], time.time() - start

p += 1
result, total_time = _10001prime(10000)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))


# Problem 8: Largest product in a series
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def _13adj_prod(n, seq):
	start = time.time()
	n_len = len(n)
	max_prod = 0

	for i in range(1, n_len - seq + 1):
		prod = 1
		for j in range(i, i + seq):
			prod *= int(n[j])

		if prod > max_prod:
			max_prod = prod

	return max_prod, time.time() - start

n = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

p += 1
result, total_time = _13adj_prod(n, 13)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))


# Problem 9: Special Pythagorean Triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pyth_triplet(num):
	start = time.time()
	for a in range(1, num):
		for b in range(a, num - a):
			c = num - b - a
			if a*a + b*b == c*c:
				return a*b*c, time.time() - start

p += 1
result, total_time = pyth_triplet(1000)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))


# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sum_primes(n):
	start = time.time()
	prime_list = [True for i in range(n+1)]
	p = 2
	prime_l = []
	while p*p < n:
		if prime_list[p] == True:
			for i in range(p*2, n+1, p):
				prime_list[i] = False
		p += 1

	for i in range(2, n):
		if prime_list[i]:
			prime_l.append(i)

	return sum(prime_l), time.time() - start

p += 1
result, total_time = sum_primes(2000000)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))

# Problem 11: Largest product in a grid
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def prod_grid(arr):
	start = time.time()
	product = 1

	horizontal_max = max(arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3] for i in range(20) for j in range(17))

	vertical_max = max(arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j] for i in range(17) for j in range(20))

	diagonal1_max = max(arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3] for i in range(17) for j in range(17))

	diagonal2_max = max(arr[i][j]*arr[i-1][j+1]*arr[i-2][j+2]*arr[i-3][j+3] for i in range(3,20) for j in range(17))

	product = max(horizontal_max, vertical_max, diagonal1_max, diagonal2_max)

	return product, time.time() - start

grid = [	[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
			[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
			[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
			[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
			[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
			[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
			[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
			[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
			[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
			[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
			[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
			[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
			[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
			[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
			[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
			[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
			[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
			[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
			[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
			[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
		]

p += 1
result, total_time = prod_grid(grid)
print ("Solution to Problem {} is {}, solved in {:.5f} seconds".format(p, result, total_time))