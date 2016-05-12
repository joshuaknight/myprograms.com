import forest 
class Passage(object):
	def start(self):
		print "\nAfter,Which you enter a dark passage and near a bush you find a shotgun"
		print "\nYou Take the shotgun,and go along the passage"
		print "\nYou are tired from walking and see a shelter"
		print "\nYou Go and take rest in the Shelter,Where you meet a Oldman"
		print "\nWho advices you to go along the journey and not take rest and threatens to kill you"		
		print "\n What do you do ?"
		print "\n Select a Choice"
		print "\n\t * 1.be rude and stay"
		print "\t * 2.be calm and leave"
		print "\t * 3.shoot him with shotgun"
		s = Passage()
		return s.input()

	def input(self):	
		get_input = raw_input(">")		

		if (get_input == '1'):
			print "\nthe old man shoots you from behind now you are dead "
			mypass = Passage()
			return mypass.death()
			
		elif (get_input == '2'):
			print "\nyou leave the shelter and pass out in the road and eaten by a tiger"			
			mypass = Passage()
			return mypass.death()

		elif (get_input == '3'):
			print "\nyou shoot him and take rest in the shelter"			
			myforest = forest.Forest()
			myforest.start()

		else:
			print "Try again"
			mypass = Passage()
			return mypass.input()
	
	def death(self):
		print "Try Again !!!"
		print "=" * 50			


