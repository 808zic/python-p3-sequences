#!/usr/bin/env python3

def print_fibonacci(length):
    

	fib_seq = []
	if length > 0:
		fib_seq.append(0)
	if length >= 2:
		fib_seq.append(1)
		for i in range(2, length):
			fib_seq.append(fib_seq[-1] + fib_seq[-2])
	print(fib_seq)
	
    #Common Sequence Operations 
	'''
	For a sequence s:

    x in s returns True if x is equal to at least one element of s.

    s + s2 returns a single sequence of the elements of s followed by the elements of s2.

    s * n returns a single sequence of s repeated n times.

    s[i]returns the ith element of s (starting at 0).

	'''
	#NOTE: Python also supports negative indices. -1 represents the last element in a sequence.
	'''
	

    s[i:j] returns a slice of s from index i up to (but not including!) index j.

    s[i:j:k] returns a slice of s from i to j with steps of k in between.

    len(s) returns the number of elements in s.

    min(s) and max(s) return the minimum and maximum values in s, respectively. >
	  NOTE: this requires the elements of s to be of the same data type, either str or numerical.

    s.index(x) returns the index of the first x in s.

    s.count(x) returns the number of instances of x in s.


	
	'''
	#Lists
	#Sorting Lists
	#there are 2 types
	'''
	1: list.sort ()
	list.sort() rearranges the elements of a list so that they are in order
	#NOTE The key parameter allows us to pass in a function
	eg 
	my_list.sort(key = len)
    print(my_list)
    # => ['z', 'Word', 'This is a long sentence']
	2: sorted()
	The sorted() function returns a sorted copy of the original list
	This function should be used when you want to preserve the integrity of your original list,
	  but you need a sorted version for a separate task
	  We can pass the key and reverse parameters into sorted() like we did for the sort method:

my_list = ['Loquacious', 'Chatty', 'Talkative']
sorted_list = sorted(my_list, key=len, reverse=True)
# => ['Loquacious', 'Talkative', 'Chatty']

	'''
	#Adding to list
	'''
	we have 2 ways
	1: list.append()
	appends its parameter to the list.
	it appends only at the end
	2: list.insert()
	can insert at any index.
	 takes two arguments: an index and a value.
	 
	 my_list = ['a', 'b', 'c', 'd', 'f']
         my_list.insert(4, 'e')
     print(my_list)
     # => ['a', 'b', 'c', 'd', 'e', 'f']
    '''
    #Removing from list
    '''
	we have 4 methods for clearing an element in a list
	
    1:The del() function.
	del() removes elements from a list, specified by an index or range of indices.
	
    2:The list.pop() method.
	list.pop() removes and returns the element at the index passed in as an argument. 
	When used without any arguments, it removes and returns the last element of the list.
	
    3:The list.remove() method.
	list.remove() removes the element passed in as an argument. 
	This is one of the few list methods that searches by value instead of index!
	
    4:The list.clear() method.
	list.clear() erases all of the values of a list. This is usually not a very useful tool, 
	but it's a fast way to free up memory on your device 
	if you're working with a particularly large list in the Python shell.

	'''
#Tuples

#Tuples do not have any special exclusive methods like lists do. This is because tuples are immutable. 

#Ranges
'''
Ranges are a very simple type of sequence that is most commonly used in for loops
You can build a range using the range() constructor 
The range constructor only requires one argument: the end of the range.and this last value is not
included in the range.
There are two optional arguments that you can include when creating a range: a start value and a step size.
step size like in slicing above

'''

# Strings
# Changing Case
'''
Strings can be formatted for case using three methods:

    str.upper() returns an uppercase version of the original string.
    str.lower() returns a lowercase version of the original string.
    str.title() returns the original string in titlecase (with the first letter of each new word capitalized.)

'''
#Instructions
