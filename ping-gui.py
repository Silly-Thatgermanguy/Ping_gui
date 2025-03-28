import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import pythonping
import time
import threading

skibidid = '0'
skibidid = int(skibidid)
server = ""
request_text = tk.StringVar
request_text = ""  
status = ""
status = tk.StringVar 
stop_threads = False
print("variables assigned")

y = 0


window2 = ttk.Window(themename='vapor')
window2.geometry("500x500")
window2.title('pinger')
print("basic window info created")

def place(): #pladds kdsk
    place



def start_pinging():
 global skibidid    #blehaus
 global y 
#  global status
 print("getting entry data")
 ping_server = Server_entry.get()
 skibidid = int(server_count.get())
 print("skibdid created and runneed")

 print("entry data received")

 ping = pythonping.ping(ping_server,count=skibidid,size=56)  #ping server incline

 for response in ping: 
  global stop_threads     #response
  print("response started ") 
  print("Received: response.received")
  time.sleep(1)
  y = y +1 
  print(f"responses:{y}")   #erm what the sigma
  request_text.config(text = f"responses:{y}")
  if y == skibidid:
    print("done pinging")
    my_thread.join()
    print("ended thread")
    stop_threads = True
# status_text.config(text = status)

print("pingin process created")

style = Style("vapor")            #stayle urt 

style.configure('TEntry', font=('Helvetica', 16))

entry_style = style.configure(                       #idk k
  'LargeButton.TButton',
   font=('Arial', 10),  # Set font size
   padding=10,height=40,width = 10)


my_thread = threading.Thread(target=start_pinging)
print("created thread")


def start_thread_update():
  global request_text
  global stop_threads
  # global status_text
  # global status 
  my_thread.start()
  if stop_threads:
    my_thread.kill

print("started thread")

#gui thingys

Server_text = ttk.Label(window2, text='SERVER:',font=('Arial', 30))
Server_text.place(x=90,y=40)

Server_entry = ttk.Entry(window2,style='TEntry',)
Server_entry.place(x=275,y=45)

server_starter_button = ttk.Button(window2, text='start pinging',command=start_thread_update)
server_starter_button.place(x=90,y=150)

request_text = ttk.Label(window2, textvariable=request_text, font=("arial", 30))
request_text.place(x=90,y=250)

server_counter_text = ttk.Label(window2, text='Amount of pings:', font=("arial",15))
server_counter_text.place(x=90,y=100)

server_count = ttk.Entry(window2,style='TEntry',)
server_count.place(x=275,y=100)



# status_text = ttk.Label(window, textvariable=status, font=("arial", 30))
# status_text.place(x=90,y=200)


window2.mainloop()