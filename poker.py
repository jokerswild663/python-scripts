#!/usr/bin/python

class card:
	'this is a card with suit and rank'
	
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def get_suit(self):
		return self.suit
	
	def get_rank(self):
		return self.rank

def matches(ranks, match_num):
	for i in ranks:
		if ranks.count(i) == match_num:
			return True	

#********************************************************************************************
def two_pair(ranks, match_num):
	'determines if there are 2 pairs in the hand'
	pair_count = 0
	for i in ranks:						#iterates through the hand and counts the number of times a card shows up twice
		if ranks.count(i) == match_num:
			pair_count += 1
	
	if pair_count == 4:		#Since pairs will be counted twice, we need to check for pair_count = 4
		return True
	
	else:	
		return False
#******************************************************************************************

def arith_sum(ranks):
	'Takes an arithmetic sum of the ranks of the hand'
	n = len(ranks)
	s = n*(ranks[0] + ranks[4])/2
	return s
#*************************************************************************************************

def sequence(ranks):
	'determines if there is a sequence formed using arithmetic sums'
	smallest = min(ranks)
	largest = max(ranks)
	Sum = 0
	a_sum = arith_sum(ranks)

	for i in ranks:		#this for loop takes the sum of the card ranks
		Sum += i	

	if Sum == a_sum:		#if the sum of the cards in the is equal to the arithmetic sum, it is a match
		return True
	else:
		return False
#*****************************************************************************************************

def sequence2(ranks):
	'determines if there is a sequence.  However, with less overhead than above'
	if max(ranks) - min(ranks) == 4:	#It is not possible for it to be in sequence and not be equal to 4 
		return True
	else:
		return False			

#*****************************************************************************
def same_suit(suits):
	'This determines if the hand has the same suit or not'
	if suits.count(min(suits)) == 5:	
		return True		

#********************************************************************************
def royal(ranks):
	'This determines if the hand is a royal flush or not'
	if min(ranks) + max(ranks) == 24:
		return True
	else:
		return False
#********************************************************************************

def singles(ranks):
	'determines if every card is different'
	for i in ranks:
		if ranks.count(i) > 1:
			return False

	return True

#********************************************************************************
def hand_type(hand):
	'This is the main function that determines the type of hand'
	
	ranks = list()	#the hand is split up into 2 parts to more easily work with
	suits = list()
	
	for cards in hand:
		ranks.append(cards.get_rank())
		suits.append(cards.get_suit())		
	ranks.sort()

#***************************************************************The flushes / straights*********
	if singles(ranks):
		if same_suit(suits):
			if sequence2(ranks):
				if royal(ranks):
					return "royal flush"
				else:
					return "straight flush"				

			else:
				return "flush"
		else:
			if sequence2(ranks):
				return "straight"
			else:
				return "high card"

#********************************The common cards************************************************
	elif matches(ranks,4):
		return "4 of a kind"	

	elif matches(ranks,3):
		if matches(ranks,2):
			return "full house"
		else:
			return "3 of a kind"			

	elif matches(ranks,2):
		if two_pair(ranks,2):
			return "2 pair"
		else:
			return "1 pair"
	
#***********************************************************************************************	

#This is where you can manipulate the hand
hand = [card(2,"diamonds"), card(2,"clubs"), card(3,"diamonds"), card(3,"clubs"), card(3,"diamonds")]


result = hand_type(hand)

print result
