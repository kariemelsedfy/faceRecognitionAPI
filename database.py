import psycopg2

#Connection string to postgresql
def getConnection():
    connection = psycopg2.connect(
        host='localhost', 
        port='5432', 
        database='userfaces', 
        user='karim', 
        password='koko2005'
    )

    return connection



#To do sql commands from python code
def initDatabase():
    connection = getConnection()
    cursor = connection.cursor()

    #Initializing database schema
    cursor.execute("CREATE TABLE embeddings (userID INTEGER PRIMARY KEY, embedding DECIMAL[]);")
    connection.commit()
    cursor.close()
    connection.close()

#Add embedding to database
def insertEmbedding(userID, embedding):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO embeddings (userID, embedding) VALUES (%s, %s) ON CONFLICT (userID) DO UPDATE SET embedding = EXCLUDED.embedding;",
        (userID, embedding)
    )
    connection.commit()
    cursor.close()
    connection.close()



