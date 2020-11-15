import os
# import pandas as pd
import pyautogui
import time
from datetime import datetime
import schedule
from main import signIn , terminate_zoom


#meetings
economika = {
    "id":"9563617467",
    "pass":"U0xmZEcwRkd0SldqOUJpOFBNQlBUQT09"
}
ohrana_truda = {
    "id":"6970240442",
    "pass":"K0NMb0tRUFprZ2YvdW1BYkNDWjlTQT09"
}
sns = {
    "id":"2688376461",
    "pass":"ja0aQ9CcItONO7zv4oOlvzTBlh66TA"
}
bisembeeva = {
    "id":"4123427527",
    "pass":"ejVaUnEzaENKcDg0aXlmOW16REhQQT09"
}
kartbaeva = {
    "id":"5210212462",
    "pass":"aTc1UXc1dDF1d1Z4WmxvNktnbFlkUT09"
}
kuzya = {
    "id":"9240549506",
    "pass":"V0VwdEd4NGkyNXYxMUo3RjVVZCtRdz09"
}
my = {
    "id":"3122896402",
    "pass":"ZWl1NW0vNzNvMmRYMFFCRWdadjk1dz09"
}
#schedule
#monday
schedule.every().monday.at("08:43").do(signIn,meeting_id = economika["id"],password = economika['pass'])
schedule.every().monday.at("09:30").do(terminate_zoom)
schedule.every().monday.at("09:43").do(signIn,meeting_id = kuzya['id'],password = kuzya["pass"])
schedule.every().monday.at("10:30").do(terminate_zoom)
schedule.every().monday.at("10:43").do(signIn,meeting_id = sns["id"],password = sns['pass'])
schedule.every().monday.at("11:30").do(terminate_zoom)
schedule.every().monday.at("11:43").do(signIn,meeting_id = kartbaeva['id'],password = kartbaeva["pass"])
schedule.every().monday.at("12:30").do(terminate_zoom)
schedule.every().monday.at("13:13").do(signIn,meeting_id = bisembeeva['id'],password = bisembeeva['pass'])
schedule.every().monday.at("13:52").do(terminate_zoom)

#tuesday
schedule.every().tuesday.at("08:43").do(signIn,meeting_id = kartbaeva["id"],password = kartbaeva['pass'])
schedule.every().tuesday.at("09:30").do(terminate_zoom)
schedule.every().tuesday.at("10:43").do(signIn,meeting_id = kuzya["id"],password = kuzya['pass'])
schedule.every().tuesday.at("11:30").do(terminate_zoom)
schedule.every().tuesday.at("11:43").do(signIn,meeting_id = bisembeeva['id'],password = bisembeeva["pass"])
schedule.every().tuesday.at("12:30").do(terminate_zoom)
schedule.every().tuesday.at("13:13").do(signIn,meeting_id = ohrana_truda['id'],password = ohrana_truda['pass'])
schedule.every().tuesday.at("13:52").do(terminate_zoom)

#wednesday
schedule.every().wednesday.at("08:43").do(signIn,meeting_id = sns["id"],password = sns['pass'])
schedule.every().wednesday.at("09:30").do(terminate_zoom)
schedule.every().wednesday.at("09:43").do(signIn,meeting_id = economika['id'],password = economika["pass"])
schedule.every().wednesday.at("10:30").do(terminate_zoom)
schedule.every().wednesday.at("10:43").do(signIn,meeting_id = kuzya["id"],password = kuzya['pass'])
schedule.every().wednesday.at("11:30").do(terminate_zoom)

schedule.every().wednesday.at("11:43").do(signIn,meeting_id = sns['id'],password = sns["pass"])
schedule.every().wednesday.at("12:30").do(terminate_zoom)

#thursday
schedule.every().thursday.at("08:43").do(signIn,meeting_id = ohrana_truda["id"],password = ohrana_truda['pass'])
schedule.every().thursday.at("09:30").do(terminate_zoom)

schedule.every().thursday.at("09:43").do(signIn,meeting_id = kartbaeva['id'],password = kartbaeva["pass"])
schedule.every().thursday.at("10:30").do(terminate_zoom)

schedule.every().thursday.at("10:43").do(signIn,meeting_id = economika["id"],password = economika['pass'])
schedule.every().thursday.at("11:30").do(terminate_zoom)

#friday
schedule.every().friday.at("08:43").do(signIn,meeting_id = bisembeeva["id"],password = bisembeeva['pass'])
schedule.every().friday.at("09:30").do(terminate_zoom)

schedule.every().friday.at("09:43").do(signIn,meeting_id = bisembeeva['id'],password = bisembeeva["pass"])
schedule.every().friday.at("10:30").do(terminate_zoom)

schedule.every().friday.at("10:43").do(signIn,meeting_id = bisembeeva["id"],password = bisembeeva['pass'])
schedule.every().friday.at("11:30").do(terminate_zoom)

#for test
schedule.every().sunday.at("08:09").do(signIn,meeting_id = my["id"],password = my['pass'])
schedule.every().sunday.at("08:13").do(terminate_zoom)
schedule.every().sunday.at("08:14").do(signIn,meeting_id = my["id"],password = my['pass'])


while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print (e)