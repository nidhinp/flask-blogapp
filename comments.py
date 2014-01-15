import psycopg2
import sys
import urlparse
import os

con = None

try:
    #urlparse.uses_netloc.append("postgres")
    #url = urlparse.urlparse(os.environ["DATABASE_URL"])

    con = psycopg2.connect(database="d600bqomrbg8er", user = "mxwgzzfpkciuuh", password = "tVKQ_Quhpk1m2yejMakND1MEAn", host = "ec2-184-73-194-196.compute-1.amazonaws.com" , port = "5432")
   
    cur = con.cursor()
    cur.execute("CREATE TABLE newcomments(id serial, title TEXT, name TEXT, comment TEXT)")
    
    con.commit()

except psycopg2.DatabaseError, e:
    print 'Error %s' %e
    sys.exit(1)

finally:
    if con:
        con.close()


