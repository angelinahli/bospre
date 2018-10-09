import sys

def read():
	try:
		result = raw_input().rstrip("\n")
	except EOFError:
		result = None
	finally:
		return result

def get_padded(string, length, padded_elt):
	return (padded_elt * (length - len(string))) + string

while True:
	num1 = read()
	if num1 == None:
		break
	num2 = read()
	maxlen = max(len(num1), len(num2))
	add_num1 = get_padded(num1, maxlen + 1, "0")
	add_num2 = get_padded(num2, maxlen + 1, "0")
	carry = [" " for _ in xrange(maxlen + 1)]
	total = ["0" for _ in xrange(maxlen + 1)]
	for i in range(1, maxlen + 1)[::-1]:
		current_carry = 1 if carry[i] != " " else 0
		total_sum = int(add_num1[i]) + int(add_num2[i]) + current_carry
		new_carry = 1 if total_sum > 1 else " "
		new_sum = 1 if total_sum % 2 == 1 else 0
		carry[i - 1] = str(new_carry)
		total[i] = str(new_sum)
	if carry[0] != " ":
		total[0] = carry[0]
	
	print("BINARY SUM:")
	print("".join(carry))
	print(get_padded(num1, maxlen + 1, " "))
	print(get_padded(num2, maxlen + 1, " "))
	print("-" * (maxlen + 1))
	print("".join(total))
