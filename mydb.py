import mysql.connector


dataBase =mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Abdullah389140@'

)



cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE crm")

print("ALL Done!")