from googlesearch import search
import os
from colorama import Fore
import time
import random

def clear():
	os.system('clear')
colors=["RED","BLUE","GREEN","YELLOW","CYAN","MAGENTA","WHITE"]
color = random.choice(colors)
def printt(string,printsearch):
	global color
	if printsearch:
		delay = 0.01
	else:
		delay = 0.03
	for i in str(string):
		whatcolor="Fore"+"."+color
		whatcolor=eval(whatcolor)
		print(whatcolor + i, end="", flush = True)
		time.sleep(delay)
	print('')
def searchgoogle(query,results):
	clear()
	printt("\n\nPlease Stand By\n\nLoading...\n\n",False)
	pauseval = results/2
	count = 0
	for i in search(query, tld='co.in', lang='en', num=results, start=0, stop=results, pause=pauseval):
		if count == 0:
			clear()
			printt(query,True)
			printt("\n\n",True)
		printt("\n",False)
		print(i)
		printt("\n",False)
		count+=1
	printt("\n\nHit Enter To Continue",False)
	input()


while True:
	clear()
	printt("Welcome To The  DubSearch Engine That Doesn't Track You!",False)
	printt("Please Enter What You Want To Search\n\n",False)
	query = input()
	printt("\n\nPlease Enter How Many Results You Would Like (The Larger Amount Of Results Requested, More Time You Will Have To Wait). Recommended is 0 - 20\n\n",False)
	results = input()
	try:
		results = int(results)
		notint = False
	except:
		notint = True
	while notint:
		printt("\n\nPlease Enter A Number!\n\n",False)
		results = input()
		try:
			results = int(results)
			notint = False
		except:
			notint = True
	searchgoogle(query,results)
