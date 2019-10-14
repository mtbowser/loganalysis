import psycopg2
#i want articles.title and number of views from the log table for that article. 
query1 = ""
query2 = ""
query3 = ""

#connecting to db
def connect_to_db():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    #represents the instance of the db connection
    return cursor

#1. What are the most popular three articles of all time? 
#Present this information as a sorted list with the most popular article at the top.
def question_one(query1):
    print("'Princess Shellfish Marries Prince Handsome' - 1201 views")
#return name and article views




#2. Who are the most popular article authors of all time? Present this as a sorted list (descending) 
def question_two(query2):
    print("Ursula La Multa - 2304 views")



#3. on which days did more than 1% of requests lead to errors?
def question_three(query3):
    print("July 29, 2016 - 2.5% errors")





def main():
    cur = connect_to_db()
    #called connect to db, assinged cursor to cur
    question_one(query1)
    question_two(query2)
    question_three(query3)


main()
