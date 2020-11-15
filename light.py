import tkinter as tk
import tkinter.ttk as ttk

from PIL import Image,ImageTk, ImageSequence
from chatterbot.chatterbot import ChatBot
import light_think as think

# what can you do   


def dark():
    global bg_color,fg_color,text_bg,enter_bg
    bg_color= 'grey10'
    fg_color= 'gold'
    text_bg = 'gray20'
    enter_bg = 'gray20'




dark()




class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        
        fileMenu = tk.Menu(self, tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='dodgerblue')
        self.add_cascade(label="Menu",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Clear", underline=1,command=lambda : chatbox.delete(1.0,tk.END))


class Chat_box(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.config(self,bg=bg_color)
        self.geometry('665x460')
        self.title('LIGHT')# Learning Inteligence of First(I) Generation for Handling Technology
        self.config(bg=bg_color)


        self.withdraw()
        splash=Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
        def main():
            ## simulate a delay while loading
            # time.sleep(6)

            ## finished loading so destroy splash
            splash.destroy()

            ## show window again
            self.deiconify()
        splash.after(4000,main)
        # main()

        menubar = MenuBar(self)
        self.config(menu=menubar)
        H_frame = tk.Frame(self,bg=bg_color)
        H_frame.pack()

        def wishMe():
            import datetime
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                return("Good Morning")

            elif hour>=12 and hour<18:
                return("Good Afternoon")   

            else:
                return("Good Evening") 


        self.logo =  ImageTk.PhotoImage(Image.open(f"data\img\logo.png"))
        Heading_img= tk.Label(H_frame,image=self.logo,bg=fg_color)
        Heading_img.grid(row=0,column=0,padx=5)

        Heading = tk.Label(H_frame,text='LIGHT',font='Helvetica 40 bold',fg=fg_color,bg=bg_color)
        Heading.grid(row=0,column=1)
        greet= tk.Label(self,text=f'{wishMe()}, I am Light',font='Helvetica 10 bold',fg=fg_color,bg=bg_color)
        greet.pack(pady=(0,10))

        Scrollbar2 = ttk.Scrollbar(self)
        Scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
        global chatbox
        chatbox= tk.Text(self,width=65,height=20,yscrollcommand=Scrollbar2.set, bg=text_bg,wrap=tk.CHAR)
        chatbox.pack(fill=tk.BOTH,padx=10)

        Scrollbar2.config(command=chatbox.yview)
        

        enter_frame = tk.Frame(self,bg=bg_color)
        enter_frame.pack(pady=5,fill='y')

        command_ = tk.StringVar()

        enter_command = tk.Entry(enter_frame,width=74,font='Helvatica 11',fg='white', bg=enter_bg,textvariable=command_,insertbackground='white')
        enter_command.pack(side='left',fill=tk.Y,padx=(2,0))
        
        def added(event=None):
            greet['text']='Thinking'
            if command_.get()=='exit':
                self.destroy()
                quit()
            else:   
                think.input(command_,chatbox)
                command_.set('')
            greet['text']=''

        
        self.send =  ImageTk.PhotoImage(Image.open(f"data\img\send.png"))
        enter= tk.Button(enter_frame,text='Enter',command=lambda:added(),image=self.send,background=fg_color,borderwidth=0,activebackground=fg_color)
        enter.pack(side='right',padx=5,)
        self.bind('<Return>',added)
        enter_command.focus()

        

class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        tk.Toplevel.config(self,bg=bg_color)
        self.geometry('665x450')
        self.title('LIGHT')# Learning Inteligence of First(I) Generation for Handling Technology
        self.config(bg='#eff723')
        self.gif_play(self,'data/img/bulb.gif')
        loading=tk.Label(self,text='LOADING...',bg='#eff723',font='None 30')
        loading.pack()
        # while True:
        #     if loading['text']=='LOADING.':
        #         loading['text']='LOADING..'
        #     elif loading['text']=='LOADING..':
        #         loading['text']='LOADING...'
        #     elif loading['text']=='LOADING...':
        #         loading['text']='LOADING.'

    def gif_play(self, parent,img):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=400, height=300,bg='#eff723',bd=0,highlightbackground='#eff723')
        self.canvas.pack(pady=(30,20))
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(img))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))
        self.update()




app_main = Chat_box()
app_main.mainloop()
quit()

