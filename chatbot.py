from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import wikipediaapi

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.geometry("730x620+0+0")
        self.root.title("Chatbot")
        self.root.bind('<Return>',self.enter_func)
        

        main_frame = Frame(self.root, bd=4, bg="powder blue",width=610)
        main_frame.pack()

        img_chat = Image.open(r"C:\Users\prath\OneDrive\Documents\chatbot\th1.jpg")
        img_chat = img_chat.resize((200, 70))
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_label = Label(main_frame,image=self.photoimg,compound=LEFT, bd=3,anchor='nw',width=730,relief=RAISED,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,width=40,textvariable=self.entry,font=("times new roman",16,"bold"))
        self.entry1.grid(row=0,column=1,padx=10,sticky= W)

        self.send=Button(btn_frame,command=self.send,text="Send>>",font=("arial",14,"bold"),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky= W)

        self.clear=Button(btn_frame,text="clear Data",command=self.clear,font=("arial",15,"bold"),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky= W)

        self.msg=''
        self.label_11 = Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

    # ===================Function Declaration===============

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)    
        self.entry.set('')

    def send(self):
        send='\t\t\t' + 'You: '+ self.entry.get()   
        self.text.insert(END,'\n'+ send)
        self.text.yview(END)
        
        if (self.entry.get()==''):
            self.msg='Please enter the input'
            self.label_11.config(text=self.msg, fg='red')

        else:
            self.msg=''    
            self.label_11.config(text=self.msg,fg='red')
           
            try:
                headers = {'User-Agent': 'Chatbot/1.0 (Contact: your@email.com)'}
                wiki_wiki = wikipediaapi.Wikipedia('en', headers=headers)
                page_py = wiki_wiki.page(self.entry.get())
                if page_py.exists():
                    summary = page_py.summary[:400] 
                else:
                    summary = "Sorry, I couldn't find information on that topic."

                bot_response = f'\n\nBot: {summary}'
                self.text.insert(END, bot_response)
                self.text.yview(END)

            except Exception as e:
                print(f"An error occurred: {e}")
                bot_response = "\n\nBot: Sorry, an error occurred while fetching information."
                self.text.insert(END, bot_response)
                self.text.yview(END)

        
        
        


if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()           