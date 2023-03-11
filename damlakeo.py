from random import randint 

print('		--DAM LA KEO--		')
print('NHAP LUA CHON CUA BAN')
player = input()
computer =  randint(0,2)

if computer == 0:
	computer = 'DAM'
if computer == 1:
	computer = 'KEO'
if computer == 2:
	computer = 'LA'
print('MAY TINH CHON ' + str(computer))

print('KET QUA')

if player == computer:
	print('DRAW')
else:
	if player == 'DAM':
		if computer == 'KEO':
			print('WIN')
		else:
			print('LOSE')	

	elif player == 'LA':
		if computer == 'DAM':
			print('WIN')
		else:
			print('LOSE')

	elif player == 'KEO':
		if computer == 'DAM':
			print('LOSE')
		else:
			print('WIN')
	else:
		print('--------	')
		print('NHAP LAI')	
