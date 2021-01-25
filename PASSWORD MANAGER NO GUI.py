import  sqlite3
conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()
#create the salesman table 
#
# cursor.execute("CREATE TABLE profiledetails(platform char(10), user_id char(30), password char(35));")
#cursor.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
option=input('type "n" for new entry any key to check the database:')


if option=='n':
    s_id = input('platform:')
    s_name = input('Username:')
    s_city = input('password:')
    cursor.execute("""
    INSERT INTO profiledetails(platform , user_id, password)
    VALUES (?,?,?)
    """, (s_id, s_name, s_city))
    conn.commit ()
    print ( 'Data entered successfully.' )

else:
    root_pswd=input('enter root password :-')
    if root_pswd=='0409':
        def get_profiledetails():
            cursor.execute("SELECT * FROM profiledetails")
            print(cursor.fetchall())

        get_profiledetails()
    else: 
        print("wrong password")
    conn . close ()
if (conn):
  conn.close()