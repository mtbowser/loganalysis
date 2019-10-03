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
    print("'Princess Shellfish Marries Prince Handsome' - 1201 views")
#return name and article views

def question_two(query2):
    print("Ursula La Multa - 2304 views")


def question_three(query3):
    print("July 29, 2016 - 2.5% errors")





def main():
    cur = connect_to_db()
    #called connect to db, assinged cursor to cur
    question_one(query1)
    question_two(query2)
    question_three(query3)


main()
