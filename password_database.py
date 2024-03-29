from tkinter import *
import sqlite3

screen = Tk()
screen.geometry("400x500")
screen.title("passwords")

# connet to database
conn = sqlite3.connect("passwords_data.db")

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE data (
		username text,
		password text,
		email text,
        facebook text, 
        instagram text,
        amazon text,
        goat text,
        stockx text
        )""")
'''

def sign_up():

	# input passwords
	global email_entry
	global facebook_entry
	global instagram_entry
	global amazon_entry
	global goat_entry
	global stockx_entry

	email_entry = Entry(screen, width = 30)
	email_entry.grid(row = 4, column = 1, pady = (25, 0))

	email_label = Label(screen, text = "Email :")
	email_label.grid(row = 4, column = 0, pady = (25, 0))

	facebook_entry = Entry(screen, width = 30)
	facebook_entry.grid(row = 5, column = 1)

	facebook_label = Label(screen, text = "Facebook :")
	facebook_label.grid(row = 5, column = 0)

	instagram_entry = Entry(screen, width = 30)
	instagram_entry.grid(row = 6, column = 1)

	instagram_label = Label(screen, text = "Instagram :")
	instagram_label.grid(row = 6, column = 0)

	amazon_entry = Entry(screen, width = 30)
	amazon_entry.grid(row = 7, column = 1)

	amazon_label = Label(screen, text = "Amazon :")
	amazon_label.grid(row = 7, column = 0)

	goat_entry = Entry(screen, width = 30)
	goat_entry.grid(row = 8, column = 1)

	goat_label = Label(screen, text = "Goat :")
	goat_label.grid(row = 8, column = 0)

	stockx_entry = Entry(screen, width = 30)
	stockx_entry.grid(row = 9, column = 1)

	stockx_label = Label(screen, text = "Stockx :")
	stockx_label.grid(row = 9, column = 0)

	# add data to database
	save_button = Button(screen, text = "Save", height = 1, width = 5, command = save)
	save_button.grid(row = 10, column = 0, columnspan = 2,  pady = (25, 0))

def save():
	# create a database/connect to one
	conn = sqlite3.connect("passwords_data.db")

	# create cursor
	c = conn.cursor()

	# add account to database
	c.execute("INSERT INTO data VALUES (:username, :password, :email, :facebook, :instagram, :amazon, :goat, :stockx)", 
            {
                "username": username_entry.get(),
                "password": password_entry.get(),
                "email": email_entry.get(),
                "facebook": facebook_entry.get(),
                "instagram": instagram_entry.get(),
                "amazon": amazon_entry.get(),
                "goat": goat_entry.get(),
                "stockx": stockx_entry.get()
      		})      

	# commit changes
	conn.commit()

    # close connection
	conn.close()


	
	

def sign_in():
	view = Tk()
	view.geometry("375x250")
	view.title("View Passwords")


	# create a database/connect to one
	conn = sqlite3.connect("passwords_data.db")

    # create cursor
	c = conn.cursor()
    
	username_entered = username_entry.get()
    
    #select data from database
	c.execute("SELECT * FROM data WHERE username  = " + username_entered)
	all_password = c.fetchall()
	
	





	#create global variables for entrys
	global email_view
	global facebook_view
	global instagram_view
	global amazon_view
	global goat_view
	global stockx_view
	    


    # text box
	email_view = Entry(view, width= 30)
	email_view.grid(row= 0, column= 1, padx= 20, pady=(10,0))

	facebook_view = Entry(view, width= 30)
	facebook_view.grid(row= 1, column= 1)

	instagram_view = Entry(view, width= 30)
	instagram_view.grid(row= 2, column= 1)

	amazon_view = Entry(view, width= 30)
	amazon_view.grid(row= 3, column= 1)

	goat_view = Entry(view, width= 30)
	goat_view.grid(row= 4, column= 1)

	stockx_view = Entry(view, width= 30)
	stockx_view.grid(row= 5, column= 1)

	
	# text box label
	email_view = Label(view, text = "Email")
	email_view.grid(row= 0, column= 0, pady=(10,0))

	facebook_view = Label(view, text = "Facebook")
	facebook_view.grid(row= 1, column= 0)

	instagram_view = Label(view, text = "Instagram")
	instagram_view.grid(row= 2, column= 0)

	amazon_view = Label(view, text = "Amazon")
	amazon_view.grid(row= 3, column= 0)

	goat_view = Label(view, text = "Goat")
	goat_view.grid(row= 4, column= 0)

	stockx_view = Label (view, text = "StockX")
	stockx_view.grid(row = 5, column = 0)

	# put results in text boxes
	for password in all_password:
		email_view.insert(0, record[2])
		facebook_view.insert(0, record[3])
		instagram_view.insert(0, record[4])
		amazon_view.insert(0, record[5])
		goat_view.insert(0, record[6])
		stockx_view.insert(0, record[7])

	# save button
	done_button = Button(view, height = 1, width = 5, command = view.exit())
	done_button.grid(row = 6, column = 0, columnspan = 2)

	



# create/login to account
username_label = Label(screen, text = "Username : ")
username_label.grid(row = 0, column = 0, padx = 20, pady=(10,0))

username_entry = Entry(screen, width = 30)
username_entry.grid(row = 0, column = 1, pady=(10,0))

password_label = Label(screen, text = "Password : ")
password_label.grid(row = 1, column = 0)

password_entry = Entry(screen, width = 30)
password_entry.grid(row = 1, column = 1)

sign_in_button = Button(screen, text = "Sign in", height = 1, width = 5, command = sign_in)
sign_in_button.grid(row = 2, column = 0, pady = (25, 0), columnspan = 2)

sign_up_button = Button(screen, text = "Sign up", height = 1, width = 5, command = sign_up)
sign_up_button.grid(row = 3, column = 0, columnspan = 2)








# commit changes
conn.commit()

# close connection
conn.close()

screen.mainloop()