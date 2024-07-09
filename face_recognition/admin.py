from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import package.main
from image import add_image
from tkinter import messagebox

class Admin:
    def __init__(self,root):
        global photoimg1
        global bg_img
        global t_1
        global t_2
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Add Image")
        
        title_lbl=Label(self.root,text="ADMIN LOGIN",font=('times new roman bold',40),bg="white",fg="red")
        title_lbl.pack(pady=5)
        
        img1=Image.open(r"C:\Users\grooky\Downloads\face_recognition\face_recognition\login.jpg")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=photoimg1)
        bg_img.pack()
        
        l_1=Label(bg_img,text='Enter admin id:',font=("times new roman",20,"bold"))
        l_1.place(x=200,y=150,width=320,height=40)

        t_1=Entry(bg_img,width=25,font=("times new roman",20,"bold"))
        t_1.place(x=200,y=250,width=320,height=40)
        
        l_2=Label(bg_img,text='Enter password:',font=("times new roman",20,"bold"))
        l_2.place(x=200,y=350,width=320,height=40)

        t_2=Entry(bg_img,width=25,show='*',font=("times new roman",20,"bold"))
        t_2.place(x=200,y=450,width=320,height=40)
        
        b_1=Button(bg_img,text="LOG IN",font=('times new roman bold',20),bg='darkcyan',borderwidth=5,fg='white',command=self.fn)
        b_1.place(x=250,y=550,width=220,height=40)

    def fn(self):
        if((t_1.get()=="admin") and (t_2.get()=="admin")):
            self.upload()  
        else:
            messagebox.showerror("Error", "Invalid user id and password")
            
    def upload(self):
            self.new_window=Toplevel(self.root)
            self.app=add_image(self.new_window) 

if __name__=="__main__":
    root=Tk()
    obj=Admin(root)
    root.mainloop()