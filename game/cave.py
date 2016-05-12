from random import randint 
class Cave(object):
	def start(self):
		print "\nThe cave is dark and too silent you go along a cracked path"
		print "\nYou use the lighted stick to move along the path"		
		print "\nYou hear a roaring whispiring sound "
		print "\nYou try not to make a sound"
		print "\nbut the cracks on the floor makes a screeching noise"
		print "\nwhich wakes the Lion,Who finds you"
		print "\nthere is a 10meter gap between you and the lion"
		print "\nthe lion on seeing you jumps towards you"
		print "\nthere is a lock on the door with a lockcode of 5digit"
		print "\nthere is also a cracked sealing,which is about to fall"
		print "\nWhat do you do?"
		print "\nSelect Choice"
		print "\n\t * 1.shoot the lion in the head"
		print "\t * 2.shoot the lock on the door"
		print "\t * 3.shoot yourself"
		print "\t * 4.try to run back"
		print "\t * 5.shoot the celing"
		print "\t * 6.shut your eyes and kneel to pray"
		print "\t * 7.shove the lion with a stick of flame and shoot"
		s = Cave()
		return s.input()


	def input(self):		
		get_input = raw_input(">")
		if (get_input == '1'):
			print "You shoot the tiger in the head but still survives and attacks you and you are dead "
			s = Cave()
			return s.death()	

		elif(get_input == '2'):
			print "You shoot the lock on the door but the lion is too quick and ponuces on you and you are dead"			
			s = Cave()
			return s.death()

		elif (get_input == '3'):
			print "You shoot yourself and you are dead"
			s = Cave()
			return s.death()

		elif (get_input == '4'):
			print "You try to run back but the lion is too quick and ponuces on you and you are dead"			
			s = Cave()
			return s.death()

		elif (get_input == '5'):
			print "You Shoot the celing and both you and the lion die"
			s = Cave()
			return s.death()

		elif (get_input == '6'):
			print "The lion on seeing you kneel down leaves you in peace and goes back to sleep"
			s = Cave()
			return s.finished()

		elif (get_input == '7'):
			print "The lion being afraid roars you being courageous shoot the lion in the head and the lion is dead,but the celing falls on the roaring thunder of the lion and you too die"											
			s = Cave()
			return s.finished()

		else:
			print "Try again"
			s = Cave()
			return s.input()
			

	def death(self):
		print "Try Again !!!"
		print "=" * 50		

	def finished(self):
		print "You Have Survived and Won the Game Congragulations !!!" 