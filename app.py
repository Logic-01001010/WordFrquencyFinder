print("WordFrequencyFinder v1.0")

f = open('keywords.txt')

li = []
dic = {}


while True:
	word = f.readline()
	
	if not word:
		break
	print( word )
	
	for i in range( len(word) ):
		w = word[i]
		if w.isupper():
			w = w.lower()
		
		if w not in li and w != '\n':
			li.append(w)
			
		if w != '\n':
			if w not in dic:
				dic[w] = 1
			else:
				dic[w] += 1
		
			
li.sort()

print( "\n문자들의 개수:", len(li) )

dic = sorted( dic.items(), key=lambda x : x[1], reverse=True )

print("\n제일 많이 나온 문자: ", dic[0][0],":",dic[0][1],"개")
print("\n제일 적게 나온 문자: ", dic[-1][0],":",dic[-1][1],"개")

print("\n\n각 문자들의 빈도수를 전부 확인하시겠습니까? (Y/N)\n")
choice = input("choice > ")

if(choice == 'Y' or choice == 'y'):

	print("\n각 문자들의 빈도수:")
	for val in dic:
		print( val[0], ":", val[1] )

print()

for i in li:
	print( i, end='' )
