import intro

class Main(object):
	"\n\n\t\tThis is A Game Meant To Be Played"
	def get(self):
		dict1 = {
		'get_intro' : 'intro.Intro()',
		'get_start' : 'bridge.Bridge()',
		'get_passage' :'passage.Passage()',
		'myforest' : 'forest.Forest()',
		'mycave' : 'cave.Cave()'}	
		get_intro = intro.Intro()
		get_intro.hello()				
		#get_start.start()
		#get_passage.passage()
		#myforest.start()
		#mycave.cave()	




print Main.__doc__
mymain = Main()
mymain.get()