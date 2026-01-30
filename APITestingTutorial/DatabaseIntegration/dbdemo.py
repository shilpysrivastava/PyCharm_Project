import mysql.connector

connection = mysql.connector.connect(host='localhost',database='APIDevelop',user='root',password='root')
print(connection.is_connected())  #this will check whether the connection is established or not
cursor= connection.cursor()        #this will create a streamline with database
cursor.execute("select * from CustomerInfo")
#print(cursor.fetchone())
#fetch all row
rows = cursor.fetchall()
print(rows)
sum = 0

# Sum all the amount received from the database
for row in rows:
    sum = sum +int(row[2])

print(sum)

#update the query
query = "update CustomerInfo set ion = %s where Coursename = %s"
data =("UK","Jmeter")
cursor.execute(query,data)
connection.commit()


connection.close()