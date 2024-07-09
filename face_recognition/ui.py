from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import package.main
from admin import Admin

def train_function():
    package.main.train()
    
def test_function():
    package.main.test()

class Face_Recognition_System:
    def __init__(self,root):
        global photoimg1
        global bg_img
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=('times new roman bold',40),bg="white",fg="red")
        title_lbl.pack(pady=5)
        
        img1=Image.open(r"C:\Users\grooky\Downloads\face_recognition\face_recognition\background.png")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=photoimg1)
        bg_img.pack()
        
        
        b1=Button(bg_img,text="TRAIN IMAGES",cursor="hand2",font=("times new roman",15,"bold"),fg="black",command=train_function)
        b1.place(x=200,y=50,width=220,height=40)
        b2=Button(bg_img,text="ADD IMAGE",cursor="hand2",font=("times new roman",15,"bold"),fg="black",command=self.admin_login)
        b2.place(x=500,y=50,width=220,height=40)
        b3=Button(bg_img,text="RECOGNIZE FACES",cursor="hand2",font=("times new roman",15,"bold"),fg="black",command=test_function)
        b3.place(x=800,y=50,width=220,height=40)
        b4=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),fg="black",command=root.destroy)
        b4.place(x=1100,y=50,width=220,height=40)
        
    def admin_login(self):
        self.new_window=Toplevel(self.root)
        self.app=Admin(self.new_window)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
