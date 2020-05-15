def binary(n, num_digits):
	ans = bin(n)[2:] # get the binary nums, without the initial 0b
	num_zeros = num_digits - len(ans) # to make them 'num_digits' digits long
	return ('0' * num_zeros) + ans

def give_lst(num_of_cards):
	num1 = (2 ** num_of_cards)
	lst = []
	for i in range(1, num1):
		lst.append(binary(i, num_of_cards))
	return lst

def check_ans(num_cards, key):
	lst = give_lst(num_cards)
	correct = '0' * num_cards
	for func in key:
		lst = func(lst)
		if correct in lst:
			lst.remove(correct)
			reply = True
		else:
			reply =  False
			exit
	return reply

def find_options(num_cards):
	options = []
	lst = give_lst(num_cards)
	for i in range(num_cards):
		def func(lst = lst, i = i):
			ans_lst = []
			for position in lst:
				if position[i] == '1':
					result = position[:i] + '0' + position[i + 1:]
				else:
					result = position[:i] + '1' + position[i + 1:]
				ans_lst.append(result)
			return ans_lst
		options.append(func)
	return options

def find_ans(num_cards):
	ans_lst = []
	options = find_options(num_cards)
	lst = give_lst(num_cards)
	correct = '0' * num_cards
	for n in range(len(lst)):
		for i in options:
			if correct in i(lst):
				lst = i(lst)
				lst.remove(correct)
				ans_lst.append(i)
	return ans_lst

def find_options_num(num_cards):
	options = {}
	lst = give_lst(num_cards)
	count = 0
	for i in range(num_cards):
		def func(lst = lst, i = i):
			ans_lst = []
			for position in lst:
				if position[i] == '1':
					result = position[:i] + '0' + position[i + 1:]
				else:
					result = position[:i] + '1' + position[i + 1:]
				ans_lst.append(result)
			return ans_lst
		options.update({count : func})
		count += 1
	return options

def find_ans_num(num_cards):
	ans_lst = []
	options = find_options_num(num_cards)
	lst = give_lst(num_cards)
	correct = '0' * num_cards
	for n in range(len(lst)):
		for count, i in options.items():
			if correct in i(lst):
				lst = i(lst)
				lst.remove(correct)
				ans_lst.append(count)
				count += 1
	return ans_lst