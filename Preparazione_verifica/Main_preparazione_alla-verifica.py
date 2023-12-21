import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
)
def creazione():
  mycursor = mydb.cursor()

  mycursor.execute("CREATE DATABASE Animali")


def aggiungi_animali():
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="Animali"
    )
   
    mycursor = mydb.cursor()

    
    for i in range(2):
      id=input("inserisci id: ")
      nome=input("inserisci nome: ")
      razza=input("inserisci razza: ")
      peso=input("inserisci peso: ")
      eta=input("inserisci età: ")

     
      sql = "INSERT INTO mammiferi (id, nome, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
    
      val = (id, nome, razza, peso, eta)

      mycursor.execute(sql, val)

      mydb.commit()

      
      print(mycursor.rowcount, "record inserted.")

def inserimento_Valori():
  mycursor = mydb.cursor()
  sql = "INSERT INTO mammiferi (id,nome,razza,peso,eta) VALUES (%s,%s,%s,%s,%s)"
  val =[ ("111", "Minasi", "serpente", 44, 12),
  ("222", "Matteo", "elefante", 33, 65),
  ("333", "Simone", "rana", 27, 11),
  ("444", "Lorenzo", "leone", 49, 5),
  ("555", "Gianluca", "gru", 22, 67)
  ]

  mycursor.executemany(sql, val)
 
  mydb.commit()


def visualizza_Animali():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM mammiferi")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def visualizza_peso():
      mycursor = mydb.cursor()

      mycursor.execute("SELECT nome FROM mammiferi WHERE peso <= 2")

      myresult = mycursor.fetchall()
      print(myresult)


def main():
    x=int(input(" 1 per inserire gli animali animali n(5), 2 per visualizzare tutti gli animali, 3 per visualizzare gli animali che pesano 2 o più kg, 4 per eliminare un'animale "))
    if x==1 :
       inserimento_Valori()
    if x==2:
        visualizza_Animali()
    if x==3:
        visualizza_peso()
    if x==4:
       print("da finire")

main()
