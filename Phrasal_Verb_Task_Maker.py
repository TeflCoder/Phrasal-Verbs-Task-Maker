import sys
import time
import spacy  
import io
import random
from spacy.matcher import Matcher
from spacy.util import filter_spans
from io import StringIO

sentence = 'For his whole life, Nick has never been able to get up early. When he was in elementary school, his mother would set the alarm clock for 6:00 AM, but it would not wake him up. When Nick was in high school, his alarm clock would go off, but he simply turned it off and went back to sleep. Every morning his father would shout, “Come on, Nick! You’re going to be late.” The shouting did not help, however. On a few days, Nick would show up two hours late! Nick knew that his school would not put up with this situation much longer. His parents were frustrated, but they could not give up. One day Nick’s mom came across a blog on the Internet where people were sharing their stories about oversleeping and different solutions they had come up with to solve their problems. After going over a few of these stories and realizing there could be an underlying health issue, Nick’s mother made'

nlp = spacy.load('en_core_web_sm') 


pattern = [{'POS': 'VERB','OP': '?'},
           {'POS': 'ADV','OP': '*'},
           {'POS': 'PRON','OP': '*'},
          {'POS': 'ADP','OP': '+'}]
           

# instantiate a Matcher instance
matcher = Matcher(nlp.vocab)
matcher.add("Verb phrase", [pattern])

doc = nlp(sentence) 
# call the matcher to find matches 
matches = matcher(doc)
spans = [doc[start:end] for _, start, end in matches]

myls = []
myls.append(filter_spans(spans))

#STEP ONE
stringer = str(myls)
string = stringer.replace('[', '2').replace(']', '2')

#STEP TWO
mystring = string.replace('22', '')

#STEP THREE
my_list = mystring.split(",")

#STEP FOUR
phrasal_list = [x.strip(' ') for x in my_list]


#STEP FIVE
listOfPrepositions = ['Aboard', 'About', 'Above', 'Across', 'After', 'Against', 'Along', 'Amid', 'Among', 'Around', 'As', 'At', 'Before', 'Behind', 'Below', 'Beneath', 'Beside', 'Besides', 'Between', 'Beyond', 'But', 'By', 'Down', 'For', 'From', 'In', 'Into', 'Of', 'Off', 'On', 'Onto', 'Over', 'Past', 'Round', 'Through', 'To', 'Toward', 'Towards', 'Under', 'Underneath', 'Up', 'Upon', 'With', 'Within', 'Without', 'aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among', 'around', 'as', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by', 'down', 'for', 'from', 'in', 'into', 'of', 'off', 'on', 'onto', 'over', 'past', 'round', 'through', 'to', 'toward', 'towards', 'under', 'underneath', 'up', 'upon', 'with', 'within', 'without']


#STEP SIX
for i in listOfPrepositions:
    if i in phrasal_list:
        phrasal_list.remove(i)



#Step Seven
mylist = []
for o in phrasal_list:
    index = sentence.find(o)
    mylist.append(index)


time.sleep(6)

mylist_2 = []
for i in phrasal_list:
    mylist_2.append(len(i))

new_list = [x+1 for x in mylist_2]

mylist_3=[x + y for x, y in zip(mylist, new_list)]

dictA = dict(zip(mylist, mylist_3))

old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout


for key in dictA:
    print('.replace(sentence[',key, ':', dictA[key],"], ' ____________ ')", end="")
    

sentenceVal = "sentence"

output = new_stdout.getvalue()
NewVal = sentenceVal+output

time.sleep(6)

sys.stdout = old_stdout

finalVar = eval(NewVal)

print("=> Phrasal Verbs key <=")
print("")
print(phrasal_list)
print("")
random.shuffle(phrasal_list)
print("A) Fill in the blanks with the appropriate phrasal verbs")
print("")
print(phrasal_list)
print("")
print("TEXT__________________________________________________________________________")
finalVar
