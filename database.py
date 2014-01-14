import psycopg2
import sys
import urlparse
import os

con = None

try:
    urlparse.uses_netloc.append("postgres")
    url = urlparse(os.environ["DATABASE_URL"])

    con=psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
   
    cur = con.cursor()
    cur.execute("CREATE TABLE newblogposts(id serial, title TEXT, body TEXT, day TEXT, time TEXT)")
    
    con.commit()

except psycopg2.DatabaseError, e:
    print 'Error %s' %e
    sys.exit(1)

finally:
    if con:
        con.close()


