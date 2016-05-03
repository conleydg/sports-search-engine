import psycopg2
import csv

conn = psycopg2.connect("dbname=sports user=David host=/tmp/")

cur = conn.cursor()




cur.execute("CREATE TABLE bird (num varchar, name varchar PRIMARY KEY, Age varchar, Pos varchar, G varchar, GS varchar,Att varchar, Yds varchar, TD varchar, Lng varchar,YA varchar, YG varchar, AG varchar, Tgt varchar, Rec varchar, Ydsrec varchar, YRrec varchar, TDrec varchar, Lngrec varchar, RGrec varchar, YGrec varchar, YScmrec varchar, RRTDrec varchar, Fmbrec varchar);")


with open('stats.csv') as f:
    f = csv.reader(f)
    for row in f:
        # row = cur.mogrify("SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s;", (row, ))
        cur.execute("INSERT INTO bird (num, name, Age, Pos, G, GS, Att, Yds, TD, Lng,YA, YG, AG, Tgt, Rec, Ydsrec, YRrec, TDrec, Lngrec, RGrec, YGrec, YScmrec, RRTDrec, Fmbrec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
#
# cur.execute("COPY birds_rushrec(num, name, Age, Pos, G, GS, Att, Yds, TD, Lng,YA, YG, AG, Tgt, Rec, Ydsrec, YRrec, TDrec, Lngrec, RGrec, YGrec, YScmrec, RRTDrec, Fmbrec) FROM '/Users/David/documents/tiy/sports-search-engine/stats.csv' DELIMITER',' CSV")

conn.commit()

cur.close()
conn.close()
