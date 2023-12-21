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
    #configurazione per la connessione al database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="Animali"
    )
    #cursore che ci permette di eseguire i comandi su mysql
    mycursor = mydb.cursor()

    #ciclo for
    for i in range(2):
      id=input("inserisci id: ")
      nome=input("inserisci nome: ")
      razza=input("inserisci razza: ")
      peso=input("inserisci peso: ")
      eta=input("inserisci età: ")

      #sintassi per inserire una tupla
      sql = "INSERT INTO mammiferi (id, nome, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
    
      val = (id, nome, razza, peso, eta)

      #esegue il comando
      mycursor.execute(sql, val)

      #applica le modifiche apportate al database, le salva
      mydb.commit()

      #restituisce il numero di righe modificate
      print(mycursor.rowcount, "record inserted.")

def inserimento_Valori():
  mycursor = mydb.cursor()
  sql = "INSERT INTO mammiferi (Id,Nome,Razza,Peso,Eta) VALUES (%s,%s,%s,%s,%s)"
  val =[ ("111", "Minasi", "serpente", 44, 12)
  ("222", "Matteo", "elefante", 33, 65)
  ("333", "Simone", "rana", 27, 11)
  ("444", "Lorenzo", "leone", 49, 5)
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

inserimentoval()
visualizza_Animali()