def factorial(num):
	# if num == 0:
	# 	return 1
	# else:
	# 	return num * factorial(num - 1)

	product = 1

	while num > 0:
		product *= num
		num -= 1
		
	return product

