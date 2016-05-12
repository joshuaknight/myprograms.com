import cave 
class Forest(object):
	def start(self):
		print "\nYou wake up and walk the path you now enter a Jungle"
		print "\nas you enter the jungle you break a wood stick from a tree"
		print "\nand make fire to it to keep the animals away "		
		print "\na roaring sound is heard and a tiger is headed your way"
		print "\nthere's a dark cave ahead,"
		print "\nWhat do you do?"
		print "\n Select a Choice"
		print "\n\t * 1.enter the cave "
		print "\t * 2.confront the tiger"
		print "\t * 3.run back to the passage"
		s = Forest()
		return s.input()

	def input(self):	
		get_input = raw_input(">")		

		if (get_input == '1'):
			print "\nYou Now enter the cave and escape from the tiger "
			s = cave.Cave()	
			return s.start()
		elif (get_input == '2'):
			print "\nYou being corageous try to shoot the tiger,but the tiger is too strong attacks you with his paws and you are dead"
			s = Forest()
			return s.death
		elif (get_input == '3'):
			print "\nWhile you are running you fall into a pit hole and you are dead "			
			s = Forest()
			return s.death
		else:
			print "Try again"	
			s = Forest()
			return s.input()			

	def death(self):
		print "Try Again !!!"
		print "=" * 50		

	