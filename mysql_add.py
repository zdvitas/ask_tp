 # -*- coding: utf-8 -*-
 # coding: utf-8
import MySQLdb
import time
import random
import sys
import string


def gen_quest_title():
	for x in xrange(1,100):
		s1=q1[random.randint(0,2)] + q2[random.randint(0,5)] + q3[random.randint(0,4)] + q4[random.randint(0,3)]
		print(s1)

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

q1=("Зачем " ,"Почему ", "Когда ","Как ")
q2=("Петя ", "Вася ", "Коля ", "Саша ", "Дима ", "Максим ")
q3=("ест " , "ломает " , "чинит ", "смотрит на ", "читает ")
q4=("яблоко?" , "дом?" , "газету?","колбасу?")


s2="Действительно???"

def id_generator(size=20, chars=string.ascii_lowercase ):
	return ''.join(random.choice(chars) for x in range(size))
usr_name = id_generator()

user = []
dates = {}

for x in xrange(5,10000):
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
	print user
	user[:] = []
# 	users.append(user)
	
# print dates
# 	print x  # Печатаем id
# 	print " , "
# 	print id_generator() + " , "
# 	print "0 , "
# 	print "0 , "
# 	print id_generator() + " , "
# 	print id_generator() + " , "
# 	print id_generator() + " , "
# 	print id_generator() + " , "
# 	print "0 , "
# 	print "0 , "
# 	dates[x] = randomDate("1/1/2008 1:30 PM", "1/1/2013 4:50 AM", random.random())
	

	pass

# user.append(id_generator()) #
# user.append(0)
# user.append(0)
# user.append(id_generator())
# user.append(id_generator())
# user.append(id_generator())
# user.append(id_generator())
# user.append(0)
# user.append(0)
# user.append("2010-10-10 10:11:10")
# users.append(user)
# dates[10] = randomDate("1/1/2008 1:30 PM", "1/1/2013 4:50 AM", random.random())
# print dates



# cursor.executemany(
#       """INSERT INTO `Ask`.`auth_user` (`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`,`date_joined`)
#       VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)""",
#       [
      
#       ] )
# db.commit()
#Генерим вопросы
