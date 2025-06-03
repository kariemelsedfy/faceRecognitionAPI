import psycopg2
from helpers import getFaceRecognitionQuery, getTopXMatchesQuery
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
    cursor.execute("CREATE TABLE embeddings (id INTEGER PRIMARY KEY, userID INTEGER, embedding DECIMAL[]);")
    connection.commit()
    cursor.close()
    connection.close()

#Add embedding to database
def insertEmbedding(userID, embedding, username = "unknown"):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO embeddings (userID, embedding, username) VALUES (%s, %s, %s)",
        (userID, embedding, username)
    )
    connection.commit()
    cursor.close()
    connection.close()



 
def lookupFace(embedding):
    connection = getConnection()
    cursor = connection.cursor()
    #cursor.execute(getFaceRecognitionQuery.getFaceRecognitionQuery(10, embedding))
    cursor.execute(getFaceRecognitionQuery.getFaceRecognitionQuery(1, embedding))
    result = cursor.fetchall()
    
    if result: 
        print(result)
        return result   
    return None



