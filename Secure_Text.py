from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("500x520")
screen.title("Secure Channel")
screen.configure(bg="lightgrey")

#Encryption Function

def encrypt():
    pwd=code.get()
    if pwd=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="white")
        message=Text1.get(1.0,END)
        encode_message = message.encode("ascii")

        base64_bytes= base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="The code is encrypted", font="impack 10 bold").place(x=5,y=6)

        Text2=Text(screen1, font="30", bd=4, wrap=WORD)
        Text2.place(x=2, y=30, width=390, height=180)
        Text2.insert(END,encrypt)


    elif(pwd==""):
        messagebox.showerror("Error","Enter the Secret Key!")
    elif(pwd!="1234"):
        messagebox.showerror("Error", "Try again!")

    
#Decryption Function

def decrypt():
    pwd=code.get()
    if pwd =="1234":
        screen2=Toplevel(screen)
        screen2.title("Encryption")
        screen2.geometry("400x250")
        screen2.configure(bg="white")
        message=Text1.get(1.0,END)
        encode_message = message.encode("ascii")

        base64_bytes= base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2, text="The code is decrypted", font="impack 10 bold").place(x=5,y=6)

        Text2=Text(screen2, font="30", bd=4, wrap=WORD)
        Text2.place(x=2, y=30, width=390, height=180)
        Text2.insert(END,encrypt)


    elif(pwd==""):
        messagebox.showerror("Error","Enter the Secret Key!")
    elif(pwd!="1234"):
        messagebox.showerror("Error", "Try again!")



#Reset Function

def reset():
    Text1.delete(1.0,END)
    code.set("")

    

#Label modification
Label(screen,text="Enter Text For Encryption and Decryption", font="impack 14 bold", bg="white").place(x=5,y=6)

#Text modification
Text1=Text(screen, font="20")
Text1.place(x=5,y=45,width=410,height=120)

#Label modification
Label(screen, text="Enter Secret Key", font="impack 13 bold").place(x=138, y=185)
code=StringVar()
Entry(screen, textvariable=code, bd=4, font="20", show="*").place(x=110,y=220)

#Buttons modification
Button(screen, text="Encyption", font="arial", bg="red", fg="white", command=encrypt).place(x=40, y=300)
Button(screen, text="Decyption", font="arial", bg="green", fg="white", command=decrypt).place(x=300, y=300)
Button(screen, text="Reset", font="arial", bg="black", fg="white", command=reset).place(x=130, y=350, width=180)

mainloop()


