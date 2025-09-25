import tkinter as tk
import customtkinter as ctk

#app = tk.Tk()
#app.mainloop()

app = ctk.CTk()

app.geometry('350x550')
ctk.set_window_scaling(1.2)

def slider_event(value):
    print('slider value:',value)

slider = ctk.CTkSlider(app,from_ = 0 ,
                       to =100, 
                       button_color="#204F94",
                       progress_color= "#1A3661",
                       command= slider_event,
                       number_of_steps= 10 ,
                       orientation='vertical')
slider.pack()

label = ctk.CTkLabel(master = app ,
                     text='new app',
                     font=('arial' , 15, 'bold'),
                     text_color= "#8CAEE4").pack()

frame = ctk.CTkFrame(master = app , corner_radius=20)
frame.pack()

check_box = ctk.CTkCheckBox(app , text = 'test',checkbox_width=20,checkbox_height=20).pack()
ctk.set_widget_scaling(1.5)
ctk.set_appearance_mode("system")
ctk.set_default_color_theme('green')
button1 = ctk.CTkButton(master = app , 
                        text= 'b1',
                        fg_color= "#60B882",
                        font=('arial' , 15, 'bold'),
                        corner_radius=13,
                        )
button1.pack()

entry = ctk.CTkEntry(master=app, placeholder_text='Password',
                     placeholder_text_color="#ABABAB",
                     width= 200,
                     height= 30,
                     show = "*",
                     font=('arial',17),
                     corner_radius=25).pack()

entry = ctk.CTkEntry(master=app, placeholder_text='Persian-text',
                     placeholder_text_color="#ABABAB",
                     width= 200,
                     height= 30,
                     font=('arial',17),
                     corner_radius=25,
                     justify ='right').pack()




app.mainloop()