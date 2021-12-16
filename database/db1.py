import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',user='root',password='on07mawa',database='python')

except mysql.connector.Error as erro:
    print(erro)
    
else:
    print("connection ok ::")
    pointer = con.cursor()
    try:
        pointer.execute("SELECT * FROM ones")
        record=pointer.fetchall()
        
    except Exception as err2:
        print(err2)
    else:
         
         print(record[0][0])
finally:
    con.close()

