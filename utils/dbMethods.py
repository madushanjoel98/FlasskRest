import utils.connections as dbc
import bcrypt


class DBOperator:
    def __init__(self):
        self.mysb = dbc.MYConnection()

    def read(self, query):

        db = self.mysb.get_connection().cursor(dictionary=True)
        db.execute(str(query))
        myresult = db.fetchall()
        db.close()
        return myresult

    def insert(self, query, val):
        # insert Method query, val=Assign Value
        mydb = self.mysb.get_connection()
        try:
            mydb = self.mysb.get_connection()
            dbcr = mydb.cursor()
            dbcr.execute(str(query), val)
            mydb.commit()
        except:
            print()
        finally:
            mydb.close()

    def inserts(self, query):
        try:
            # Get the database connection
            mydb = self.mysb.get_connection()
            dbcr = mydb.cursor()
            # Execute the query
            dbcr.execute(str(query))
            # Commit the transaction
            mydb.commit()
        except Exception as e:
            # Handle any exceptions that occur
            print(f"An error occurred: {e}")
            if mydb:
                # Rollback the transaction in case of error
                mydb.rollback()
        finally:
            if dbcr:
                # Close the cursor
                dbcr.close()
            if mydb:
                # Close the connection
                mydb.close()

    def queryExecuter(self, query):
        # Query Executor use to execute the query
        mydb = self.mysb.get_connection()
        dbcr = mydb.cursor()
        dbcr.execute(str(query))
        mydb.commit()
        mydb.close()

# # Usage
# dbUsage = DBOperator()
# insert_query = """
# INSERT INTO programming_languages (name, released_year, githut_rank, pypl_rank, tiobe_rank)
# VALUES (%s, %s, %s, %s, %s)
# """
# values = ("Testi", "2001", "2", "4", "5")
# dbUsage.insert(insert_query, values)
# io = dbUsage.read("SELECT * FROM programming_languages LIMIT 100")
# for v in io:
#     print(v)
