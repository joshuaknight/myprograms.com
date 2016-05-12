#from sys import argv
import bridge
from sys import exit 

class Intro(object):
	def hello(self):
		#script ,first ,second = argv
		print "\nHello There ! Enter Your name : "
		get_name = raw_input(">")
		print "\nEnter Your Age :"
		get_age = int(input(">"))
		if (get_age < 18):
			try:
				raise NameError()
			except NameError:
				print "Invalid Age Restricted"
				exit(1)

		print "\nHello There %s Welcome to this furious game"%get_name 
		print "lets see if you can survive in this wild Game" 
		print "These Four Parts of Passage've to be passed to Survive"
		print "\n"
		
		items = ('bridge passage forest cave')
		
		for i in items:
			stuff_items = items.split(' ')

		print "\t * ",stuff_items[0]
		print "\t * ",stuff_items[1]
		print "\t * ",stuff_items[2]
		print "\t * ",stuff_items[3]
		
		if (i > 5):
			mybridge = bridge.Bridge()
			mybridge.start()
			mybridge.input()


					
