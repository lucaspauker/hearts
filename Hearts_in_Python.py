#Uploaded January 18, 2015

import random
import time
import sys

deck=['2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h','14h',
      '2d','3d','4d','5d','6d','7d','8d','9d','10d','11d','12d','13d','14d',
      '2s','3s','4s','5s','6s','7s','8s','9s','10s','11s','12s','13s','14s',
      '2c','3c','4c','5c','6c','7c','8c','9c','10c','11c','12c','13c','14c']

newdeck=deck[:]    #the newdeck is the deck - cards already played (like a deck in a game)


class hand(object):
    def __init__(self):
        '''
        initialize a hand
        '''
        self.hand=[]

    def deck(self):
        return newdeck

    def removefromdeck(self,element):
        '''
        removes an element from deck
        '''
        #print element
        #print element in self.newdeck
        if element in newdeck:
            newdeck.remove(element)

    def removefromhand(self,card):
        '''
        removes one card from hand
        assumes card is in hand
        '''
        self.hand.remove(card)
        
    def addtohand(self,card):
        '''
        adds card to hand
        '''
        self.hand.append(card)
        count=2
        newhand=[]
        while count <14:
            for x in self.hand:
                if str(count)==x[:-1]:
                    newhand.append(x)
                    #print newhand
            count+=1
        hand=newhand
    
    def dealhand(self):
        '''
        deals a hand of 13 cards
        '''
        count=0
        while count<13:
            x=random.choice(newdeck)
            self.hand.append(x)
            self.removefromdeck(x)
            count+=1
##        count=2
##        newhand=[]
##        while count <14:
##            for x in self.hand:
##                if str(count)==x[:-1]:
##                    newhand.append(x)
##                    #print newhand
##            count+=1
##        hand=newhand

##    def getnumber(self, card):
##        return card[-1]

    def inhand(self,card):
        count=0
        #print len(self.hand)
        while count<len(self.hand):
            if card==self.hand[count]:
                return True
            count+=1
        return False

    def llength(self):
        return len(self.hand)

    def index(self, number):
        return self.hand[number]

    def __iter__(self):
        for x in self.hand:
            yield x

    def printhand(self):
        '''
        prints sorted hand
        '''
        print 'Hand contains: ',         ###Remove comma at the end of the hand
        count=2
        newhand=[]
        while count <=14:
            for x in self.hand:
                if str(count)==x[:-1]:
                    newhand.append(x)
                    #print newhand
            count+=1
        self.hand=newhand
        for x in self.hand:
            if x[-1]=='c':
                if x[:-1]>'10' and len(x[:-1])!=1:
                    if x[:-1]=='11':
                        print 'Jack of clubs, ',
                    if x[:-1]=='12':
                        print 'Queen of clubs, ',
                    if x[:-1]=='13':
                        print 'King of clubs, ',
                    if x[:-1]=='14':
                        print 'Ace of clubs, ',
                else:
                    print x[:-1],' of clubs, ',
        for x in self.hand:
            if x[-1]=='s':
                if x[:-1]>'10' and len(x[:-1])!=1:
                    if x[:-1]=='11':
                        print 'Jack of spades, ',
                    if x[:-1]=='12':
                        print 'Queen of spades, ',
                    if x[:-1]=='13':
                        print 'King of spades, ',
                    if x[:-1]=='14':
                        print 'Ace of spades, ',
                else:
                    print x[:-1],' of spades, ',
        for x in self.hand:
            if x[-1]=='d':
                if x[:-1]>'10' and len(x[:-1])!=1:
                    if x[:-1]=='11':
                        print 'Jack of diamonds, ',
                    if x[:-1]=='12':
                        print 'Queen of diamonds, ',
                    if x[:-1]=='13':
                        print 'King of diamonds, ',
                    if x[:-1]=='14':
                        print 'Ace of diamonds, ',
                else:
                    print x[:-1],' of diamonds, ',
        for x in self.hand:
            if x[-1]=='h':
                if x[:-1]>'10' and len(x[:-1])!=1:
                    if x[:-1]=='11':
                        print 'Jack of hearts, ',
                    if x[:-1]=='12':
                        print 'Queen of hearts, ',
                    if x[:-1]=='13':
                        print 'King of hearts, ', 
                    if x[:-1]=='14':
                        print 'Ace of hearts, ',
                else:
                    print x[:-1],' of hearts, ',
        print '\n'


class player(object):
    def __init__(self, hand, identification):
        '''
        initialize a player
        '''
        self.hand=hand
        self.identification=identification
        
    def passcards(self, card1, card2, card3):
        '''
        pass 3 cards
        input three cards in hand to pass

        will return 
        '''
        self.pass1=card1
        self.pass2=card2
        self.pass3=card3
        self.hand.removefromhand(card1)
        self.hand.removefromhand(card2)
        self.hand.removefromhand(card3)


    
    def getcards(self, otherplayer):
        '''
        takes the pass of another player
        '''
        self.hand.addtohand(otherplayer.pass1)
        self.hand.addtohand(otherplayer.pass2)
        self.hand.addtohand(otherplayer.pass3)
    
    def playcard(self, card):
        '''
        plays a card
        '''
        self.hand.removefromhand(card)
        return card

class computerplayer(player):
    def threeworstcards(self):
        '''
        picks three highest cards and (if in hand) the queen of spades
        then passes these three cards
        '''
        if self.hand.inhand('12s'):
            one='12s'
            two=self.hand.index(-1)
            three=self.hand.index(-2)
            #print one,two,three
##            self.hand.removefromhand(one)
##            self.hand.removefromhand(two)
##            self.hand.removefromhand(three)
##            return one,two,three
            self.passcards(one,two,three)
        else:
            one=self.hand.index(-1)
            two=self.hand.index(-2)
            three=self.hand.index(-3)
            #print one,two,three
##            self.hand.removefromhand(one)
##            self.hand.removefromhand(two)
##            self.hand.removefromhand(three)
##            return one,two,three
            self.passcards(one,two,three)
    def playcard(self, cardled):
        '''
        plays a card for the computer
        is the highest card in the original trick
        '''
        suit=cardled[-1]
        best='0d'
        for x in self.hand:
            #print x[:-1]
            if x[-1]==suit:
                if int(str(x)[:-1])>int(str(best)[:-1]):
                    best=x
        if best=='0d':
            best=self.hand.index(0)
        self.hand.removefromhand(best)
        return best


    

##h=hand()
##h.dealhand()
##h.printhand()
##p=computerplayer(h,1)
##h.printhand()
##p.threeworstcards()


class turnphase(object):
    def __init__(self, cardlead, card1, card2, card3):
        '''
        plays one turn phase
        '''
        self.cardlead=cardlead
        self.card1=card1
        self.card2=card2
        self.card3=card3

    def bestcard(self,cardled,cardtwo):
        '''
        returns which card has a higher number value and has the same suit as cardled
        '''
        #print cardled,cardtwo
        if cardled[-1]!=cardtwo[-1]:
            return cardled
        if int(cardled[:-1])>int(cardtwo[:-1]):
            return cardled
        return cardtwo
        
    def whowins(self):
        '''
        returns which card wins a hand
        '''
        best=self.bestcard(self.cardlead, self.card1)
        best=self.bestcard(best, self.card2)
        best=self.bestcard(best, self.card3)
        return best
    
    def getpoints(self):
        '''
        returns amount of points for single trick
        '''
        points=0
        for x in [self.cardlead, self.card1, self.card2, self.card3]:
            if x[-1]=='h':
                points+=1
            if x=='12s':
                points+=13
        return points




def start():
    m=raw_input('Press n to start a new game, press q to quit ')
    if m=='n':
        print '\n'
        playgame()
    elif m=='q':
        sys.exit()
    else:
        print 'Invalid command, please try again\n'
        start()

    
def playgame():
    print 'Welcome to hearts! To play a card write the number followed by the first letter in the suit with no spaces. Then press enter. For example, the Ace of hearts=14h, the Two of spades=2s, and the Queen of clubs=12c.\n'
    h=hand()
    p=player(h,1)           #real player
    h.dealhand()
    h.printhand()
    one=raw_input('First pass: ')
    while p.hand.inhand(one)==False:
        one=raw_input('Not in hand\nFirst pass: ')
    two=raw_input('Second pass: ')
    while p.hand.inhand(two)==False:
        two=raw_input('Not in hand\nSecond pass: ')
    three=raw_input('Third pass: ')
    while p.hand.inhand(three)==False:
        three=raw_input('Not in hand\nThird pass: ')
    p.passcards(one,two,three)
    
    i=hand()
    cpu1=computerplayer(i,2)
    i.dealhand()
    cpu1.threeworstcards()

    print 'You got passed: ',cpu1.pass1,cpu1.pass2,cpu1.pass3
    p.getcards(cpu1)
    cpu1.getcards(p)

    h.printhand()
    print '\nYou lead first'

            #do the passing stuff
    j=hand()
    cpu2=computerplayer(j,3)
    j.dealhand()

    k=hand()
    cpu3=computerplayer(k,4)
    k.dealhand()

    mypoints=0
    onepoints=0
    twopoints=0
    threepoints=0

    wholeads=1
    
    #print h.llength()
    while h.llength()!=0:

        if wholeads==1:
            boool=False
            while boool==False:
                m=raw_input('Play a card: ')
                boool=h.inhand(m)
                if boool==False:
                    print 'Not in hand'
            h.removefromhand(m)
            n=cpu1.playcard(m)
            print 'Computer 1 played: ', n
            o=cpu2.playcard(m)
            print 'Computer 2 played: ',o 
            q=cpu3.playcard(m)
            print 'Computer 3 played: ', q
            t=turnphase(m,n,o,q)
            
        if wholeads==2:
            n=cpu1.playcard(m)
            print '\nComputer 1 played: ', n
            o=cpu2.playcard(n)
            print 'Computer 2 played: ',o 
            q=cpu3.playcard(n)
            print 'Computer 3 played: ', q
            boool=False
            while boool==False:
                m=raw_input('Play a card: ')
                boool=h.inhand(m)
                if boool==False:
                    print 'Not in hand'
            h.removefromhand(m)
            t=turnphase(n,m,o,q)
            
        if wholeads==3:
            o=cpu2.playcard(m)
            print 'Computer 2 played: ',o 
            q=cpu3.playcard(o)
            print 'Computer 3 played: ', q
            boool=False
            while boool==False:
                m=raw_input('Play a card: ')
                boool=h.inhand(m)
                if boool==False:
                    print 'Not in hand'
            h.removefromhand(m)
            n=cpu1.playcard(o)
            print '\nComputer 1 played: ', n
            t=turnphase(o,n,m,q)

        if wholeads==4:
            q=cpu3.playcard(m)
            print 'Computer 3 played: ', q
            boool=False
            while boool==False:
                m=raw_input('Play a card: ')
                boool=h.inhand(m)
                if boool==False:
                    print 'Not in hand'
            h.removefromhand(m)
            n=cpu1.playcard(q)
            print '\nComputer 1 played: ', n
            o=cpu2.playcard(q)
            print 'Computer 2 played: ',o
            t=turnphase(q,n,o,m)


        #print m,n,o,p
        
        print '\n'
        h.printhand()
        r=t.whowins()
        points=t.getpoints()
        #print '\n',r,m,n,o,q
        if r==m:
            mypoints+=points
            print '\n\nYou won the trick. You gained ',points,' points. You now have ',mypoints,' points. You lead the next trick.\n'
            wholeads=1
        elif r==n:
            onepoints+=points
            print '\n\nComputer 1 won the trick. They gained ',points,' points. They now have ',onepoints,' points. Computer 1 leads the next trick.\n'
            wholeads=2
        elif r==o:
            twopoints+=points
            print '\n\nComputer 2 won the trick. They gained ',points,' points. They now have ',twopoints,' points. Computer 2 leads the next trick.\n'
            wholeads=3
        elif r==q:
            threepoints+=points
            print '\n\nComputer 3 won the trick. They gained ',points,' points. They now have ',threepoints,' points. Computer 3 leads the next trick.\n'
            wholeads=4
        print 'You have ',mypoints,' points. Computer 1 has ',onepoints,' points. Computer 2 has ',twopoints,' points. Computer 3 has ',threepoints,' points.\n'
        #print mypoints,onepoints,twopoints,threepoints

    if mypoints<=onepoints:
        if mypoints<=twopoints:
            if mypoints<=threepoints:
                print 'You Win!'
                start()
            else:
                print 'Computer 3 Wins.'
                start()
        else:
            if twopoints<threepoints:
                print 'Computer 2 Wins.'
                start()
            else:
                print 'Computer 3 Wins.'
                start()
    else:
        if onepoints<twopoints:
            if onepoints<threepoints:
                print 'Computer 1 Wins.'
                start()
            else:
                print 'Computer 3 Wins.'
                start()
        else:
            if twopoints<threepoints:
                print 'Computer 2 Wins.'
                start()
            else:
                print 'Computer 3 Wins.'
                start()    

start()



            
        
        
