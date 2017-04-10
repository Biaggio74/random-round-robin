from random import randint
from datetime import datetime, date, time

#Competitors
competitors = ["Gro Lovli", "Hilde L. Thorkildsen", "Geir Gjersdal", "Thomas Ohrbom", "Stefan Dokken", "Balazs Kisfali", "Bezawit Jemberu Telila", "Leif Monnich Strom", "Martin Larssen", "Arnstein", "Lars Stromme", "Leif Bottolfs", "Knut Fredrik Asker", "Thomas Karlsen", "Martin Larssen", "Nina V Five", "Stein Sundbye", "Odd Bjornsen", "Terje Kulseng", "petter firing", "Herleik Wahl", "Steinar Tveito", "Carl Erik Auke Borgen", "Geir Birkenes"]
 
#["A", "B", "C", "D", "E", "F", "G", "H"]
length = len(competitors)
#print ", ".join(competitors)
print "The number of the competitors: " + str(length)
print " "

def comp(comp):
    for i in range(0, len(comp)):
        print str(i+1) + ") " + comp[i]

comp(competitors)    

#Number of competitors within one group
group_size = 6
#Create a random list of competitors
def rounding(competitors):
    length = len(competitors)
    rand_list = []
    for i in range(0, length):
        ind = randint(0, length-1)
        rand_comp = competitors[ind]
        rand_list.append(rand_comp)
        competitors.remove(rand_comp)
        length -= 1
    return rand_list

randomlist = rounding(competitors)
print " "   
     
#Group the competitors into couples
def couples(list, group):
    couples = []
    for n in range(0, len(list)  / 2):
        couples.append(list[n] + " vs. " + list[len(list)/2 + n ])
    return couples           

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def grouping():
    i=0
    for group in chunker(randomlist, 6):
        print " "
        print "Group: " + str(i+1)
        i += 1
        for n in group:
            print n
        
print grouping()     
    
print "Random grouping was run at: " + datetime.now().strftime("%Y-%m-%d %H:%M")    