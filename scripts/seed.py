import psycopg2

try:
    conn = psycopg2.connect("dbname='hackton' user='hackton' host='10.0.1.19' password='CHUBACA1234'")
    print "connection OK"
except:
    print "I am unable to connect to the database"