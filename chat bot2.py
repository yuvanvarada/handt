from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == ""):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Bot -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !")

	elif (user == "Say about dances in telangana" or user == "what are the types of dances in telangana" or user == "dance telangana"):
		txt.insert(END, "\n" + "Bot ->The dances are Gussadi dance, Dhimsa dance, Lambadi dance, Perini Sivatandavam,and Dappu dance")

	elif (user == "Famous national park of telangana" or user == "national park telangana" or user == "crack a funny line"):
		txt.insert(END, "\n" + "Bot ->kbr national park ")

	elif (user == "unesco sites telangana" or user == "unescot" or user == "unescotel"):
		txt.insert(END, "\n" + "Bot -> ramappatemple")

	elif (user == "unesco sites telangana" or user == "unescot" or user == "unescotel"):
		txt.insert(END, "\n" + "Bot -> ramappatemple")
   
   
   
   
    
	
	else:
		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
