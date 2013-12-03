 # -*- coding: utf-8 -*-
 # coding: utf-8
import MySQLdb
import time
import random
import sys
import string

q1=("Зачем " ,"Почему ", "Когда ","Как ")
q2=("Петя ", "Вася ", "Коля ", "Саша ", "Дима ", "Максим ")
q3=("ест " , "ломает " , "чинит ", "смотрит на ", "читает ")
q4=("яблоко?" , "дом?" , "газету?","колбасу?","машину?")


s2="Действительно???"

def gen_quest_title():
	s1=q1[random.randint(0,2)] + q2[random.randint(0,5)] + q3[random.randint(0,4)] + q4[random.randint(0,3)]
	return s1

def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)



def id_generator(size=20, chars=string.ascii_lowercase ):
	size = random.randint(5, 20)
	return ''.join(random.choice(chars) for x in range(size))


user = []
dates = {}

def gen_text():
	s = "";
	for x in xrange(1,random.randint(5,30)):
		s = s+" "+id_generator()
	return s
	pass



def gen_user(dates):
	f = open('/tmp/users.txt', 'w')	
	for x in xrange(2,1000):

		dates[x] = randomDate("1/1/2008 1:30 PM", "1/1/2013 4:50 AM", random.random())

		f.writelines(str(x)+","+id_generator()+",0,0,"+id_generator()+","+id_generator()+","+id_generator()+","+id_generator()+",0,1,"+str(dates[x]) + "\n")
	f.close()
	pass

def gen_quests(dates):
	f = open('/tmp/quest.txt', 'w')
	for x in xrange(1,100000):
		usr_id = random.randint(2, 999)
		date = str(dates[usr_id])
		quest_dates[x] = randomDate( date, "1/1/2013 4:50 AM", random.random() )
		string = str(x) + "," + gen_quest_title() +"," + gen_text() + "," + str(quest_dates[x]) + "," + str(usr_id) + "\n"
		f.writelines(string)
 	f.close()
	pass

def gen_answers():
	f = open('/tmp/ans.txt', 'w')
	for x in xrange(1,1000000):
		usr_id = random.randint(2, 999)
		quest_id = random.randint(1, 99999)
		date = str(quest_dates[quest_id])
		date2 = randomDate( date, "1/1/2013 4:50 AM", random.random() )
		string = str(x) + "," + id_generator() +"," + gen_text() + "," + str(date2) + "," +str(quest_id)+"," + str(usr_id) + "\n"
		f.writelines(string)
	f.close()
	pass


gen_user(dates)
quest_dates={}
gen_quests(dates)
gen_answers()





