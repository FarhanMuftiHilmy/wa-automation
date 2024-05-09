import pymysql.cursors

# Connect to Database
def open_conn():
    database = pymysql.connect(host="localhost", 
                               user="yourusername", 
                               passwd="yourpasswd",
                               database="dbname", 
                               cursorclass=pymysql.cursors.DictCursor)
    return database

# Execute "Retrieve All" Query
def execute_query(database):
    with database:
        with database.cursor() as cursor:
            # Query to retrieve all data
            sql = "Select * from tablename;"
            cursor.execute(sql)
            result = cursor.fetchall()
            # close database connection
            database.commit()
            return result