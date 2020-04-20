# do all the imports
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading


# get html data of website
def get_html_data(url):
    data = requests.get(url)
    return data


# parsing html and extracting data
def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    all_details = ""
    #data set 1
    info_div1_text=bs.find("li",class_="bg-blue").find('span').contents[0]
    info_div1=bs.find("li",class_="bg-blue").find('strong').contents[0]
    all_details = all_details + info_div1_text + " : " + info_div1 + "\n"
    #data set 2
    info_div2_text=bs.find("li",class_="bg-green").find('span').contents[0]
    info_div2=bs.find("li",class_="bg-green").find('strong').contents[0]
    all_details = all_details + info_div2_text + " : " + info_div2 + "\n"
    #data set 3
    info_div3_text=bs.find("li",class_="bg-red").find('span').contents[0]
    info_div3=bs.find("li",class_="bg-red").find('strong').contents[0]
    all_details = all_details + info_div3_text + " : " + info_div3 + "\n"
    #data set 4
    info_div4_text=bs.find("li",class_="bg-orange").find('span').contents[0]
    info_div4=bs.find("li",class_="bg-orange").find('strong').contents[0]
    all_details = all_details + info_div4_text + " : " + info_div4 + "\n"
    #test
    ##print info_div.find('strong').contents[0]
    #print(all_details)
    return all_details


# function use to  reload the data from website
def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing..")
    mainLabel['text'] = newdata


# function for notifying...
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            app_icon='icon.ico'
        )
        time.sleep(300) ## refresh set to 5 min.


# creating gui:
root = tk.Tk()
root.geometry("450x600")
root.iconbitmap("icon.ico")
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background='white')
f = ("poppins", 25, "bold")
banner = tk.PhotoImage(file="banner.png")
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f, bg='white')
mainLabel.pack()

reBtn = tk.Button(root, text="REFRESH", font=f, relief='solid', command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()