import os
# import pandas as pd
import pyautogui
import time
from datetime import datetime
import schedule
import subprocess
import psutil,os

def signIn(meeting_id,password):

    #Open's Zoom Application from the specified location
    os.startfile("C:/Users/Zver/AppData/Roaming/Zoom/bin/Zoom.exe")
    time.sleep(2)

    #Click's join button
    joinbtn=pyautogui.locateCenterOnScreen("join_conf.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    #Type the meeting id
    meetingidbtn=pyautogui.locateCenterOnScreen("meet_id.png")
    pyautogui.moveTo(meetingidbtn)
    pyautogui.write(meeting_id)
    time.sleep(1)

    #To turn of video and audio
    mediaBtn=pyautogui.locateAllOnScreen("media.png")
    for btn in mediaBtn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)

    #To join
    join=pyautogui.locateCenterOnScreen("join_.png")
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(2)

    #Enter's passcode to join meeting
    passcode=pyautogui.locateCenterOnScreen("meeting_password.png")
    pyautogui.moveTo(passcode)
    pyautogui.write(password)
    time.sleep(1)

    #Click's on join button
    joinmeeting=pyautogui.locateCenterOnScreen("final_join.png")
    pyautogui.moveTo(joinmeeting)
    pyautogui.click()
    time.sleep(1)

def terminate_zoom():
    """
    terminate zoom task
    """
    
    os.system("taskkill /im zoom.exe")

# df = pd.read_excel('timings.xlsx',index=False)

"""
while True:
    #To get current time
    now = datetime.now().strftime("%H:%M")
    if now in str(df['Timings']):
        
        mylist=df["Timings"]
        mylist=[i.strftime("%H:%M") for i in mylist]
        c= [i for i in range(len(mylist)) if mylist[i]==now]
        row = df.loc[c] 
        meeting_id = str(row.iloc[0,1])  
        password= str(row.iloc[0,2])  
        time.sleep(5)
        signIn(meeting_id, password)
        time.sleep(2)
        print('signed in')
        break
"""

