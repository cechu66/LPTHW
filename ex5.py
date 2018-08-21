# -- coding: utf-8 -- 
name = 'Zed a. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
in_centi = height / 0.39370
in_kilos = weight / 2.2046


print "Lets talk about %r." % name
print " Hes %d inches tall." % height
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy"
print "He's got %r eyes and %r hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

#this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d i get %d." % (age, height, weight, age + height + weight)
print "in centimet is .%2F" % in_centi
print "in kilos is %.2F" % in_kilos