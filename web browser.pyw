import webbrowser
import tkinter as tk

root=tk.Tk()
root.title("Web Browser")
root.geometry("340x250")
root.configure(background="Black")
def fonk1():
    searchh=search.get()
    webbrowser.open("www."+searchh+".com")

def youtube():
    webbrowser.open("www.youtube.com")

def instagram():
    webbrowser.open("www.instagram.com")

def twitter():
    webbrowser.open("www.twitter.com")

def facebook():
    webbrowser.open("www.facebook.com")

def github():
    webbrowser.open("www.github.com")

ara=tk.Label(text="Search",font="Arial 15",bg="black",fg="red")
ara.pack()

search=tk.Entry(font="1")
search.pack()

enter=tk.Button(text="Enter",command=fonk1,font="Arial 13",bg="red")
enter.pack()

youtube=tk.Button(text="Youtube",command=youtube,font="Arial 11",bg="red")
youtube.pack(side="left")

instagram=tk.Button(text="Instagram",command=instagram,font="Arial 11",bg="red")
instagram.pack(side="left")

twitter=tk.Button(text="Twitter",command=twitter,font="Arial 11",bg="red")
twitter.pack(side="left")

facebook=tk.Button(text="Facebook",command=facebook,font="Arial 11",bg="red")
facebook.pack(side="left")

github=tk.Button(text="Github",command=github,font="Arial 11",bg="red")
github.pack(side="left")

root.mainloop()
