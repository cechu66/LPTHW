def number_range(max,step):
	i = 0
	list = []
	while i < max:
		print "At the top i is %d" % i
		list.append(i)

		i = i + step
	print list

def number_range_using_for(max,step):
	elements = range(1,max,step)
	for item in elements:
		print "Item: %d " % item
	print elements

number_range(10,2)
number_range_using_for(20,2)

