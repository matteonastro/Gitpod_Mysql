import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE mammiferi (id char(3) PRIMARY KEY, nome_proprio varchar(20),razza varchar(25),peso int, eta int)")