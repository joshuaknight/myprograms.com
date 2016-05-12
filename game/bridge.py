from random import randint
import passage 
class Bridge(object):
	def start(self):
		print "\n You Enter the Bridge in the Middle of the Night,"
		print "\n There is nobody accompaning You"
		print "\n A Huge person with a gun in his hand is blocking your way"
		print "\n He is Sure to shoot You,What do you do ?"
		print "\n Select a Choice"
		print "\n\t * 1.tackle"
		print "\t * 2.run"
		print "\t * 3.tell a joke"


	def input(self):
		get_input = raw_input(">")		
		i = 1 
		while (i):		
			if (get_input == '1'):
				print "You showed bravery and tried to tackle him he shoot at you and You are Dead"
				s = Bridge()
				return s.death()

			elif (get_input == '2'):
				print "You tried to run and he shoot you in the back and you are dead"			
				s = Bridge()
				return s.death()
			elif (get_input == '3'):
				print "You tell a Joke and he laughs and allows you to pass through"			
				mypassage = passage.Passage()
				return mypassage.start()
			else:
				print "Try again"	
				s = Bridge()
				return s.input()
			i = 0

	
	def death(self):
		print "Try Again !!!"
		print "=" * 50