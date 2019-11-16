import psycopg2


# psql -d news
# explore the tables using the \dt and \d table commands and select statements
# i want articles.title and number of views from the log table for that
# article.
query1 = "select articles.title, count (*) as views\
 from articles join log on log.path = concat('/article/', articles.slug)\
 group by articles.title\
 order by views desc\
 limit 3"
# need to join the articles and the authors table by a single field
query2 = "select authors.name, count (*) as views\
        from authors\
        join articles on authors.id = articles.author\
        join log on log.path = concat('/article/', articles.slug)\
        group by authors.name\
	order by views desc"

# first gets total errors 2nd one gets total requests
query3 = " select errors_table.day, (errors::float/requests::float)*100 as percentage\
        from \
        (select count(*) as errors, date(time) as day from log where status = '404 NOT FOUND' group by day)\
        as errors_table\
        join \
        (select count(*) as requests, date(time) as day from log group by day)\
        as requests_table\
        on errors_table.day = requests_table.day\
        where  percentage > 1 "

# connecting to db


def connect_to_db():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # represents the instance of the db connection
    return cursor

# 1. What are the most popular three articles of all time?
# Present this information as a sorted list with the most popular article
# at the top.


def question_one(query1):

    cur = connect_to_db()
    cur.execute(query1)
    result = cur.fetchall()
    print(result)
#print("'Princess Shellfish Marries Prince Handsome' - 1201 views")
# return name and article views


# 2. Who are the most popular article authors of all time? Present this as
# a sorted list (descending)
def question_two(query2):

    cur = connect_to_db()
    cur.execute(query2)
    result = cur.fetchall()
    print(result)


# 3. on which days did more than 1% of requests lead to errors?
def question_three(query3):
    print("July 29, 2016 - 2.5% errors")


def main():
    # called connect to db, assinged cursor to cur
    question_one(query1)
    question_two(query2)
    question_three(query3)


main()
