#Import the files
import pymysql
import os
#Clear the window
os.system("cls") 
#Just to set the colors
COLORS = {\
"green":"\u001b[32m",
"white":"\u001b[37m",
"red":"\033[1;31m"
}
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
#MySQL Connecting
mydb = pymysql.connect(host="localhost",user="root",password="",database="wherearemypasswords")
#To set the cursor
mycursor = mydb.cursor()
#To get the name of the site from the user
name = input ("What is the name of the site you would like to get its password? ")
#The SQL command
sql = "select * from passwords where name = '%s'"%name
#To execute the SQL command
res = mycursor.execute(sql)
if res > 0:
	#To fetch the data
	for i in mycursor:
		id_n = i[2]
		id_n = ("[[green]]"+id_n+"[[white]]")
		print(colorText(id_n))
else:
	e = ("[[red]]"+"there's no password with this site name"+"[[white]]")
	print(colorText(e))
#To close the connection
mydb.close()