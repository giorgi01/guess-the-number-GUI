from tkinter import *
from random import randrange

index = 0


def checker(rand_num = randrange(1,26)):
	global index
	global num
	index += 1 
	if index >= 3 and index < 5:
		if rand_num - 5 < 0:
			print(f'რიცხვი მდებარეობს {rand_num+randrange(3,6)}-სა და 0-ს შორის')
		else:
			print(f'რიცხვი მდებარეობს {rand_num+randrange(3,6)}-სა და {rand_num-randrange(3,6)}-ს შორის')
	elif index >= 5:
		if rand_num - 3 < 0:
			print(f'რიცხვი მდებარეობს {rand_num+randrange(2,4)}-სა და 0-ს შორის')
		else:
			print(f'რიცხვი მდებარეობს {rand_num+randrange(2,4)}-სა და {rand_num-randrange(2,4)}-ს შორის')
	if int(num.get()) == rand_num:
		print('პასუხი სწორია')
	else:
		print('პასუხი არასწორია, კიდევ სცადეთ :)')

root = Tk()
root.title('გამოცნობანა')
root.geometry('300x115')
Label(root, text='შეიყვანეთ რიცხვი 1-25 შუალედში', height=2, width=40).grid(row=0)
num=Entry(root, width=15)
num.grid(row=1)
check_button = Button(root,text='Check!', width=5, command=checker)
check_button.place(x=123, y=75)
mainloop()