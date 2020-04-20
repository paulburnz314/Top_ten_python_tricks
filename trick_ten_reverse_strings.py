
#Trick 10: reversing a string

# lengthy but easiest to understand
word = 'murder'
backword = ''
x = len(word)  # length of the string
while x > 0:  # short version is just 'while x:'
    x = x - 1
    backword = backword + word[x]  #each time you add a letter python is making a new string so slow
    
print(f'The word {word} spelled backward is {backword}')


#letter by letter populate a list
word = 'murder'
backword_list = []
x = len(word)
while x > 0:
    x = x - 1
    backword_list.append(word[x])
"""below join returns a string concatenated with the elements
	of an iterable object such as a list"""

backword = ''.join(backword_list) 

print(f'The word {word} spelled backward is {backword}')


#Play around with the values start, stop and step
word = 'murder' * 3		#neat how you can multiply a string
length = len(word)
start = length - 0  # where do you want to start slicing
stop = None			# if you want to go through to the end put None, otherwise try 0,1 or more
step = -1			# negative means you step backwords, while 1 means no skipping
reverse_slice = slice(start, stop, step)
reverse = word[reverse_slice]

print(reverse)


#similar to above but not readable or easy to understand
word = 'rikkitikkitavi'
backword = word[::-1]

print(backword)

#Sourced from: Arron Hall, https://stackoverflow.com/questions/931092/reverse-a-string-in-python