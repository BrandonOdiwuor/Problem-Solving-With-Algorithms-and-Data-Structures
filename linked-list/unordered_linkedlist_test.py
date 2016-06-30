import unordered_linkedlist

def main():
	my_linkedlist = unordered_linkedlist.UnorderedLinkedList()
	test(len(my_linkedlist), 0)
	test(my_linkedlist.is_empty(), True)
	my_linkedlist.add(31)
	test(len(my_linkedlist), 1)
	my_linkedlist.add(77)
	my_linkedlist.add(17)
	my_linkedlist.add(93)
	my_linkedlist.add(26)
	my_linkedlist.add(54)
	test(len(my_linkedlist), 6)
	test(my_linkedlist.search(93), True)
	test(my_linkedlist.search(9), False)
	test(my_linkedlist.remove(93), 93)
	test(len(my_linkedlist), 5)
	test(my_linkedlist.search(9), False)
	test(my_linkedlist.remove(9), False)
	my_linkedlist.append(100)
	test(len(my_linkedlist), 6)
	my_linkedlist.append('Last')

	#Printing the linked list
	print(my_linkedlist)



# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



#Runs the main function
if __name__ == '__main__':
	main()
