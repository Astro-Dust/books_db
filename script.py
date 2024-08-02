from getpass import getpass # esconde a senha no terminal
from mysql.connector import connect, Error

try:
	conn = connect(
			host='localhost',
			user=input('Username: '),
			password=getpass('Password: ')
		)
except Error as e:
	print(e)
