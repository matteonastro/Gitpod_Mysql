import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
)

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



