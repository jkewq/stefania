import psycopg2
import tkinter as tk
import sys

# konfiguracios adatok
database_name = 'balazs'
database_user = 'balazs'
database_pass = ''

# a beszuras gombra kattintva hivodik meg
def do_insertion():
	if (validate_data() == True):
		insert_record()
		alert_ok()
		empty_fields()
	else:
		alert_error()
		
def validate_data():
	return True

def insert_record():
	try:
		cursor = conn.cursor()
		query = '''INSERT INTO girl (name, birth_year, birth_month, location, notes)
		VALUES (%s, %s, %s, %s, %s)'''
		cursor.execute(query, (form_name.get(), form_birth_year.get(), form_birth_month.get(), form_location.get(), form_notes.get()))
		cursor.commit()
	except: 
		print("HIBA TORTENT")

def empty_fields():
	form_name.delete(0, tk.END)
	form_birth_year.delete(0, tk.END)
	form_birth_month.delete(0, tk.END)
	form_location.delete(0, tk.END)
	form_notes.delete(0, tk.END)
	form_name.focus()

def alert_ok():
	return ''

def alert_error():
	return ''

# csatlakozas a PostgreSQL-hez
try:
	conn = psycopg2.connect("dbname='"+database_name+"' user='"+database_user+"' password='"+database_pass+"'")
except:
	print("Unable to connect database")
	sys.exit()
	
# tkinter peldanyositasa
root = tk.Tk()

# cimek kiirasa
tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Birth year").grid(row=1)
tk.Label(root, text="Birth month").grid(row=2)
tk.Label(root, text="Location").grid(row=3)
tk.Label(root, text="Notes").grid(row=4)

# mezok kirakasa
form_name = tk.Entry(root)
form_name.grid(row=0, column=1)
form_birth_year = tk.Entry(root)
form_birth_year.grid(row=1, column=1)
form_birth_month = tk.Entry(root)
form_birth_month.grid(row=2, column=1)
form_location = tk.Entry(root)
form_location.grid(row=3, column=1)
form_notes = tk.Entry(root)
form_notes.grid(row=4, column=1)

# gomb kirakasa
tk.Button(root, text='Insert record', command=do_insertion).grid(row=5, column=1, sticky=tk.W, pady=4)

root.mainloop()