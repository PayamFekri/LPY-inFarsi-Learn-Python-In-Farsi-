import customtkinter as ctk

#-----------------functions
def printUsername():
    name = entry.get()
    print(name)
    label.configure(text = name)
    entry.delete(0,ctk.END)
    
#-----------------gui
app = ctk.CTk()
app.geometry('400x300')
app.title('name')

label = ctk.CTkLabel(app,
                     text='welcome',
                     font=('arial', 12)
                     )
label.pack()

entry = ctk.CTkEntry(app, placeholder_text='enter name')
entry.pack()

button = ctk.CTkButton(app, text='print name', command=printUsername)
button.pack()

app.mainloop()