import psycopg2
import csv

conn = psycopg2.connect("dbname=sports user=David host=/tmp/")

cur = conn.cursor()

search_by =input('Which way would you like to search for the Rushing and Receiving'
                ' stats for the 2015 Eagles?'
                '\nEnter n to search by name'
                '\nEnter a to search by age'
                '\nEnter p to search by position'
                '\nOr press enter to add a new player\n')

if search_by == 'n':
    name = input('Please enter the name '
                'of the player you would like to find: ')


    cur.execute("SELECT age from birds WHERE name='{}';".format(name))
    age = cur.fetchall()[0][0]

    cur.execute("SELECT pos from birds WHERE name='{}';".format(name))
    pos = cur.fetchall()[0][0]

    cur.execute("SELECT yds from birds WHERE name='{}';".format(name))
    rush_yds = cur.fetchall()[0][0]

    cur.execute("SELECT ydsrec from birds WHERE name='{}';".format(name))
    rec_yds = cur.fetchall()[0][0]

    cur.execute("SELECT td from birds WHERE name='{}';".format(name))
    rush_td = cur.fetchall()[0][0]

    cur.execute("SELECT tdrec from birds WHERE name='{}';".format(name))
    rec_td = cur.fetchall()[0][0]


    print(name, '\nage: ', age, '\nPosition: ', pos,
            '\nRush Yards: ', rush_yds, '\nRec Yards: ', rec_yds, '\nRush TDs: ',
            rush_td, '\nRec TDs: ', rec_td)

elif search_by == 'a':
    age = input('Enter the age you would like to search by: ')
    cur.execute("SELECT Name from birds WHERE age='{}';".format(age))
    players = cur.fetchall()
    print(players)


elif search_by == 'p':
    pos = input('Enter the pos you would like to search by: ')
    cur.execute("SELECT Name from birds WHERE pos='{}';".format(pos))
    players = cur.fetchall()
    print(players)

elif search_by == '':
    name = input('What is the new players\'s name? ')
    age = input('What is the new players\'s age? ')
    pos = input('What is the new players\'s pos? ')
    rush_yds = input('What is the new players\'s total rush yards? ')
    rec_yds = input('What is the new players\'s total rec yards? ')
    rush_td = input('What is the new players\'s total rushing touchdowns? ')
    rec_td = input('What is the new players\'s total rec touchdowns? ')
    # cur.execute("INSERT INTO bird (name) VALUES (%s)", name)
    cur.execute("INSERT INTO birds (name, age, pos, yds, ydsrec, td, tdrec) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, age, pos, rush_yds, rec_yds, rush_td, rec_td))
    cur.execute("SELECT * from birds WHERE name='{}';".format(name))
    asdf = cur.fetchall()
    print(asdf)
