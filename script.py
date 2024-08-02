from getpass import getpass # esconde a senha no terminal
from mysql.connector import connect, Error

try:
	conn = connect(
		host='localhost',
		user=input('Username: '),
		password=getpass('Password: ')
	)
	
	cursor = conn.cursor() # para interagir com o BD
    
	cursor.execute("SHOW DATABASES LIKE 'online_movie_rating';")
	database_exists = cursor.fetchone()

	if database_exists:
		print('Database exists already!')
	else:
		create_db_query = 'CREATE DATABASE online_movie_rating'
		cursor.execute(create_db_query)
		print('Database created successfully!')

	show_db_query = 'SHOW DATABASES;'

	cursor.execute(show_db_query)
	for db in cursor: # mostra todos os BD
		print(db)

except Error as e:
	print(e)
