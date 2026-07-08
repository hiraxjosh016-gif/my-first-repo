print('              HIRAX\'S MASTER PIECE.       ')
print('''Type......
         Done......if you are finished
         NB Enter atleast 6 characters''')
numlist = list()
while True :
	inp = input('Enter whatever you want here :',)
	if inp == 'Done' : break
	numlist.append(inp)
print('we are set to go..')
print('Here are your items...')
print(numlist)
print('Now damn many mosquitoes here, uhmm now here is a dictionary of them...')
dictionary = dict()
try:
	for item in numlist :
		if item not in dictionary :
			dictionary[item] = 1
		else :
			dictionary[item] = dictionary[item] + 1
			print(dictionary)
except:
	print('Make sure you entered words only not figures:')
	
#now on a file.
print('Create a text file no numbers and save as e.g. sample.txt. after the one i Have sent. Make sure it is not in any folder rather in the home storage location')
fnam = input('Enter file name:',)
try:
	fname = open(fnam)
except:
	print('Error!')
	print('Laba endongo ku pig,')
	print('I said enter a file name u dumbass,like sample.txt exactly')
	print('Atte....hurry')
	print('Now try again')
	quit()
for i in fname :
	print('Here is your file...:',i)
print('done')
newinp = input('Do you wish to see ur title source statement?')
if newinp == 'Yes' :
	print(i)
elif newinp == 'No' :
	print('Thanks for ur tym!@@')
else:
	print('its either Yes or No,unchanged')
print('Now create your own file or use an existing.')
file = input('Enter new File name :',)
try:
	ffile = open(file)
except:
		print('''Error!
		Please,get another file in internal storage
		Not in any folder and try again''')
for ff in ffile :
		print(ff)
print('All done.')
		


	
