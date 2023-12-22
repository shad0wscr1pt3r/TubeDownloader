from pytube import YouTube
from pytube.exceptions import RegexMatchError
from tkinter import *
from tkinter import filedialog, messagebox
import os

def action(type):
    link = videos.get()
    try:
        video = YouTube(link)

        if type == "mp3":
            download = video.streams.filter(only_audio=True).first()
        elif type == "mp4":
            download = video.streams.get_highest_resolution()
        else:
            return

        output_path = filedialog.askdirectory()
        if output_path:
            download.download(output_path)
            if type == "mp3":
                # Change the file extension to mp3
                old_file_path = os.path.join(output_path, download.default_filename)
                new_file_path = os.path.join(output_path, f"{video.title}.mp3")
                os.rename(old_file_path, new_file_path)

            messagebox.showinfo("Download completed", f"The video was successfully downloaded to {output_path}")
    except RegexMatchError:
        messagebox.showerror("Error", "No streams were found for the provided URL.")
    except Exception as e:
        messagebox.showerror("Error", f"There was an error downloading the video: {str(e)}")

def popup():
    messagebox.showinfo("About me", "Hello :) This is version 1.0 of the program Created by shad0wscr1pt3r.")

root = Tk()
root.config(bd=15)
root.title("Download videos")

image = PhotoImage(file="Youtube.png")
photo = Label(root, image=image, bd=0)
photo.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="For more information", menu=helpmenu)
helpmenu.add_command(label="Author information", command=popup)
menubar.add_command(label="Exit", command=root.destroy)

instructions = Label(root, text="Program created in Python to download YouTube videos\n")
instructions.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

mp3_button = Button(root, text="Download MP3", command=lambda: action("mp3"))
mp3_button.grid(row=2, column=1, pady=5)

mp4_button = Button(root, text="Download MP4", command=lambda: action("mp4"))
mp4_button.grid(row=3, column=1, pady=5)

root.mainloop()
