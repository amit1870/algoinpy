class SimpleStack(object):
	def __init__(self):
		self.stack = []

	def stack_push(self,item):
		self.stack.append(item)

	def stack_pop(self):
		return self.stack.pop()

	def stack_top(self):
		return self.stack[-1]


def main():
	st = SimpleStack()

	string = "abcXcba"
	i = 0
	while string[i] != 'X':
		st.stack_push(string[i])
		i += 1


	i += 1
	while i < len(string) :
		if st.stack == [] or string[i] != st.stack_pop():
			print "Not Pallindrome"
			return None
		i += 1

	print "Pallindrome"
	

def pallindrom_by_reverse(number):
	# there is a recusive way in recursion.py 
	temp = number
	rev_num = 0
	while temp > 0 :
		rev_num = rev_num * 10 + temp % 10 
		temp /= 10

	if number == rev_num:
		return "Pallindrome"
	else:
		return "Not Pallindrome"

def str_pallindrome(string):
	len_s = len(string)

	for i in range(0,len_s/2):
		if string[i] != string[-i-1]:
			return False
	return True


print str_pallindrome("madaam")

def str_reverse(string):
	len_s = len(string)
	i = len_s-1
	rev = ""
	while i >= 0:
		rev += string[i]
		i -= 1
	return rev

print str_reverse("amitpatel")



# print pallindrom_by_reverse(10000)

if __name__ == "__main__":
	# main()
	pass