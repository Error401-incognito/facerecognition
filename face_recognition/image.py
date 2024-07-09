from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import package.main
from tkinter import filedialog as fd
import shutil
from tkinter import messagebox

class add_image:
    def __init__(self,root):
        global photoimg1
        global bg_img
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Add Image")
        
        title_lbl=Label(self.root,text="ADD IMAGE",font=('times new roman bold',40),bg="white",fg="red")
        title_lbl.pack(pady=5)
        
        img1=Image.open(r"C:\Users\grooky\Downloads\face_recognition\face_recognition\upload.jpg")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=photoimg1)
        bg_img.pack()
        
        b_1=Button(bg_img,text="BROWSE",font=('times new roman bold',20),bg='darkcyan',borderwidth=5,fg='white',command=self.copyFile)
        b_1.place(x=650,y=350,width=220,height=40)

    def copyFile(self):    
       file = fd.askopenfilename(title = "Select a file to copy",filetypes=[('Jpg Files', '*.jpg')])  
       directory = r"C:\Users\grooky\Downloads\face_recognition\face_recognition\train"

       try:   
          shutil.copy(file, directory)   
          messagebox.showinfo("Message","The Image is successfulling added!")  
       except:    
          messagebox.showerror(title = "Error!",message = "Operation unsuccessful. Please try again!")  

if __name__=="__main__":
    root=Tk()
    obj=Admin(root)
    root.mainloop()