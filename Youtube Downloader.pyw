import customtkinter
from tkinter import *
from tkinter.ttk import *
from pytube import YouTube 
from PIL import ImageTk, Image
from PIL import *
import io
import urllib.request
from io import BytesIO
import threading

def App():
    ##########    global declaration     #####################
    global menu, yt, boolean, url, initial , running, res, total_size, downloaded
    boolean= False
    res= "1080p"
    initial=0
    running=0
    total_size=0
    downloaded=[0, "0%"]
    ##########    function     ####################
    def Mp4():
        menu_mp3.grid_forget()
        menu_mp4.grid(row=3, column=2)

    def Mp3():
        menu_mp4.grid_forget()
        menu_mp3.grid(row=3, column=2, sticky=E)

    def On_progress(stream, chunk, byte_rem):
        global running , total_size, downloaded
        running = 4
        download=total_size-byte_rem
        print(download)
        downloaded[1]=f"{(round(download/total_size*100, 2))}%"
        downloaded[0]=float(round(download/total_size, 5))
        pass

    def On_completion(stream, filepath):
        global initial, running
        running = 5
    
        initial=0

    def Choice(choice):
        global res
        res=choice
        size_label.grid(row=2, column=2, sticky=N)
        size_label.configure(text=f"{yt.streams.get_by_resolution(res).filesize_mb} mb")
        return res

    def Search():
        ####  global declaration  ####
        global yt, boolean, url, running, total_size
        url=str(url_entry.get())
        ####
        try:
            running=1.5
            status.configure(text="Searching for Video....", text_color="cyan")
            yt= YouTube(url,
            on_progress_callback=On_progress,
            on_complete_callback=On_completion,
            use_oauth=False,
            allow_oauth_cache=True
            )

            running = 1

            boolean=True
            u = urllib.request.urlopen(yt.thumbnail_url)
            raw_data = u.read()
            u.close()

            ytstream=yt.streams
            ytubetitle=yt.title

            mp4_btn.grid(row=2, column=1, sticky=W)
            mp3_btn.grid(row=2, column=2, sticky=E)
            name_label.grid(row=1, column=2, sticky=N)
            name_label.configure(text=ytubetitle)
            size_label.grid(row=2, column=2, sticky=N)
            size_label.configure(text=f"{yt.streams.get_by_resolution(res).filesize_mb} mb")
            total_size=float(yt.streams.get_by_resolution(res).filesize_approx)
            yt_download.grid(row=4, column=2, sticky=N)
            ###############  image  ##############
            img= io.BytesIO(raw_data)
            img=Image.open(img)
            img=img.resize(((400, 250)))
            img=ImageTk.PhotoImage(img)
            img_label.configure(image=img, text="")

            ######################################

            return yt, boolean

        except:
            running = 2

    def Download():
        ####  global declaration  ####
        global yt, boolean, res, initial, running 
        ####
        try:
            #if boolean==True:
            running =4
            yd =yt.streams.get_by_resolution(res)
            thread=threading.Thread(target=yd.download, args=("C:\\Users\\Owner\\Downloads\\Video",))
            thread.start()
            #yd.download("C:\\Users\\Owner\\Downloads\\Video")
        
            initial =0
    
        except:
           running = 3 

    def Download_progress():
        global initial, running
        if initial == 0:
                status.configure(text="Downloading .", text_color="cyan")
                initial +=1

        elif initial == 1:
                status.configure(text="Downloading ..", text_color="cyan")
                initial +=1

        elif initial == 2:
                status.configure(text="Downloading ...", text_color="cyan")
                initial +=1

        elif initial == 3:
                status.configure(text="Downloading ....", text_color="cyan")
                initial =0
        
        else:
                initial =0

        if running == 4:
             window.after(7000 ,Download_progress)

    def Status():
        global running, initial, downloaded
        if running == 0:
            status.configure( text="No download yet", text_color="cyan")

        elif running == 1.5:
            status.configure(text="Searching for Video....", text_color="cyan")
            download_bar.grid_forget()
            download_percent.grid_forget()

        elif running == 1:
            status.configure(text="video was successfully found....", text_color="cyan")
            download_bar.grid_forget()
            download_percent.grid_forget()

        elif running == 2:
            status.configure(text="Error!! The Video was not found or check you Internet connection!!!", text_color="red")
    
        elif running == 3:
            status.configure(text="Error...", text_color="red")
            download_bar.grid_forget()
            download_percent.grid_forget()

    
        elif running == 4:
            Download_progress()
            download_bar.set(downloaded[0])
            download_bar.grid(row=0, column=2)
            download_percent.configure(text=downloaded[1])
            download_percent.grid(row=0, column=3)

        elif running == 5:
            status.configure(text="Successfully Downloaded...", text_color="cyan")
            download_bar.set(1.0)
            download_percent.configure(text="100%")

        else:
            running=0

        window.after(200, Status)
    
    ##############  variable declaration  #################
    res="720p"

    ###############################

    ##############  Tkinter GUI  #################
    customtkinter.set_default_color_theme("dark-blue")
    customtkinter.set_appearance_mode("dark")
    window=customtkinter.CTk()
    window.title("Youtube Downloader")
    window.geometry("1300*1000")
    title_img="C:\\Users\\owner\\Documents\\coding\\youtube download\\youtube.ico"
    window.iconbitmap(title_img)
    window.resizable(width=False, height=False)

    url_entry=customtkinter.CTkEntry(window, width=700, placeholder_text="Copy URL from youtube then press 'CTRL + V' here to paste the URL")
    url_entry.grid(row=1, column=1, columnspan=2)

    search_img=Image.open("C:\\Users\\owner\\Documents\\coding\\youtube download\\search.png")
    search_img=search_img.resize(((20, 20)))
    search_img=ImageTk.PhotoImage(search_img)

    download_frame=customtkinter.CTkFrame(window, width=750, height=400)
    download_frame.grid(row=3, column=1,columnspan=2 ,sticky=W)

    #################  Status  #################
    status=customtkinter.CTkFrame(window)
    status.grid(row=4, column=1, columnspan=2, sticky=S + W)

    status_frame1=customtkinter.CTkFrame(status)
    status_frame1.grid(row=1, column=1)
    status=customtkinter.CTkLabel(status_frame1, anchor=W, width=150)
    status.grid(row=1, column=1, sticky=W)
    download_bar=customtkinter.CTkProgressBar(status, width=180)
    download_bar.grid(row=1, column=2)
    download_bar.grid_forget()
    download_percent=customtkinter.CTkLabel(status, text="", width=50)
    download_percent.grid(row=1, column=3)
    download_percent.grid_forget()

    #################  Label  #####################
    img_label=customtkinter.CTkLabel(download_frame, text="", width=400, height=250)
    img_label.grid(row=1, column=1, rowspan=4, sticky=W)

    name_label=customtkinter.CTkLabel(download_frame, text="Download youtube videos through Youtube Downloader", font=('times new roman', 25),wraplength=300)
    name_label.grid(row=1, column=2, sticky=N)
    name_label.grid_forget()

    size_label=customtkinter.CTkLabel(download_frame, text="", font=('times new roman', 20))
    size_label.grid(row=2, column=2, sticky=N)
    size_label.grid_forget()
    ############## Drop down list  #############

    #mp4
    menu_mp4=customtkinter.CTkOptionMenu(download_frame, values=["1080p","720p", "480p", "360p", "144p"], command=Choice)
    menu_mp4.grid(row=3, column=2)
    menu_mp4.grid_forget()

    menu_mp3=customtkinter.CTkOptionMenu(download_frame, values=["160kbps","128kbps", "170kbps", "50kbps"],command=Choice)
    menu_mp3.grid(row=3, column=2)
    menu_mp3.grid_forget()

    #################### Buttons ######################
    search_btn=customtkinter.CTkButton(window, width=30, text="", image=search_img, command=Search)
    search_btn.grid(row=1,column=2, sticky=E)

    mp4_btn=customtkinter.CTkButton(window, width=385, text="MP4", command=Mp4)
    mp4_btn.grid(row=2, column=1, sticky=W)
    mp4_btn.grid_forget()

    mp3_btn=customtkinter.CTkButton(window, width=385, text="MP3", command=Mp3)
    mp3_btn.grid(row=2, column=2, sticky=E)
    mp3_btn.grid_forget()

    yt_download=customtkinter.CTkButton(download_frame, text="download", command=Download)
    yt_download.grid(row=4, column=2, sticky=N)
    yt_download.grid_forget()

    ##########################################
    Status()
            
    window.mainloop()

App()
