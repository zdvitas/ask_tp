 # -*- coding: utf-8 -*-
 # coding: utf-8
import MySQLdb
import time
import random
import sys
import string

user_count = 10;
quest_count = 20;
end_date = "1/1/2013 4:50 AM"

q1=("Зачем " ,"Почему ", "Когда ","Как ")
q2=("Петя ", "Вася ", "Коля ", "Саша ", "Дима ", "Максим ")
q3=("ест " , "ломает " , "чинит ", "смотрит на ", "читает ")
q4=("яблоко?" , "дом?" , "газету?","колбасу?")


s2="Действительно???"



def id_generator(size=20, chars=string.ascii_lowercase ):
	return ''.join(random.choice(chars) for x in range(size))

def gen_quest_title():
	s1=q1[random.randint(0,2)] + q2[random.randint(0,5)] + q3[random.randint(0,4)] + q4[random.randint(0,3)]
	return s1.decode('utf-8')

def gen_quest_body(count=20):
	s = ""
	for i in xrange(1,count):
		s += id_generator() + " "
		pass
	return s

def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)



usr_name = id_generator()

user = []
dates = {}
# Генерация пользователя

for x in xrange(5,user_count):
	user.append(x)
	user.append(id_generator()) #
	user.append(0)
	user.append(0)
	user.append(id_generator())
	user.append(id_generator())
	user.append(id_generator())
	user.append(id_generator())
	user.append(0)
	user.append(0)
	dates[x] = randomDate("1/1/2008 1:30 PM", "1/1/2013 4:50 AM", random.random())
	user.append(dates[x])
	#print user
	user[:] = []
	pass
quest = []
quest_data = {}
#Генерация вопросов
for x in xrange(5,quest_count):

	quest.append(x)
	quest.append(gen_quest_title())
	usr_id = random.randint(5, user_count)
	date = randomDate("1/1/2013 4:50 AM", "1/1/2013 4:50 AM", random.random())
	quest_data[x]= date
	quest.append(quest_data[x])
	#quest[1] = quest[1].decode('utf-8')
	print type(quest[1])
	print quest
	quest[:] = []
	pass

print gen_quest_title()

# cursor.executemany(
#       """INSERT INTO `Ask`.`auth_user` (`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`,`date_joined`)
#       VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)""",
#       [
      
#       ] )
# db.commit()
#Генерим вопросы
