# progam to count the frequencies of every word in list
sonnet1 = ['from', 'fairest', 'creatures', 'we', 'desire',
'increase','that', 'thereby', 'beauty','rose', 'might','never',
'die','but','as', 'the','riper', 'should', 'by', 'time', 'decease',
'his', 'tender', 'heir', 'might','bear', 'his', 'memory','but','thou',
'contracted', 'to', 'thine', 'own', 'bright','eyes','feed','thy','light',  'flame', 'with',
'self-substantial','fuel','making','a','famine','where', 'abundance','lies','thyself',
'thy','foe' , 'to', 'thy', 'sweet', 'self', 'too', 'cruel']
# dictionary help to initialize every word with their frequency
dictionary = {}
for i in sonnet1:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

print(dictionary)  # dictionary call