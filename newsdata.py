import psycopg2

query1 = ""
query2 = ""
query3 = ""

#connecting to db
def connect_to_db():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    #represents the instance of the db connection
    return cursor

#get 3 most popular articles    
def question_one(query1):
    pass
#return name and article views

def question_two(query2):
    pass


def question_three(query3):
    pass





def main():
    cur = connect_to_db()
    #called connect to db, assinged cursor to cur
    print(question_one())
    print(question_two())
    print(question_three())


main()
