#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(n):

	return 0 if n == 0 else 1 if n == 1 else get_fibonacci_number(n-1) + get_fibonacci_number(n-2)

	pass

def get_fibonacci_sequence(l):

	return [0] if l == 1 else [0,1] if l == 2 else get_fibonacci_sequence(l-1) + [sum(get_fibonacci_sequence(l-1)[-2:])]

	pass

def get_sorted_dict_by_decimals(dic):

	return dict(sorted(dic.items(), key = lambda x: x[1] % 1))

	pass

def fibonacci_numbers(length):

	ls = [0,1]

	for i in ls:

		yield i

	ls = deque(ls)

	for i in range(2, length):

		ls.append(ls[-1] + ls[-2])
		ls.popleft()
		yield ls[-1]

	pass

def build_recursive_sequence_generator(seq, f):

	def fibonacci_numbers(length):

		ls = seq

		for i in ls:

			yield i

		ls = deque(ls)

		for i in range(len(seq), length):

			ls.append(ls[-1] + ls[-2])
			ls.popleft()
			yield ls[-1]

	return fibonacci_numbers

	pass


if __name__ == "__main__":

	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
