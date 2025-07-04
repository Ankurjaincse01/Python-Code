import Database 
import pymysql

# Database connection function
def CreateConn():
    return pymysql.connect(host="ankur jain ",database="ankur jain ",
                          user="root",password="",port=3306)


# Table Create function

def CreateTable():
    conn = CreateConn()
    cursor = conn.cursor() # helping to execute your query
    query = "create table student(sid int primary key auto_increment,name VARCHAR(50),email VARCHAR(50),city VARCHAR(50))"
    cursor.execute(query)
    conn.commit()
    print("Table Created")
    conn.close()
    
CreateTable() # Calling create table functio