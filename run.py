import os
# import pandas as pd
import pyautogui
import time
from datetime import datetime
import schedule
from main import signIn

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
#schedule
#monday
schedule.every().monday.at("08:43").do(signIn,meeting_id = economika["id"],password = economika['pass'])
schedule.every().monday.at("09:43").do(signIn,meeting_id = kuzya['id'],password = kuzya["pass"])
schedule.every().monday.at("10:43").do(signIn,meeting_id = sns["id"],password = sns['pass'])
schedule.every().monday.at("11:43").do(signIn,meeting_id = kartbaeva['id'],password = kartbaeva["pass"])
schedule.every().monday.at("13:13").do(signIn,meeting_id = bisembeeva['id'],password = bisembeeva['pass'])
#tuesday
schedule.every().tuesday.at("08:43").do(signIn,meeting_id = kartbaeva["id"],password = kartbaeva['pass'])
schedule.every().tuesday.at("10:43").do(signIn,meeting_id = kuzya["id"],password = kuzya['pass'])
schedule.every().tuesday.at("11:43").do(signIn,meeting_id = bisembeeva['id'],password = bisembeeva["pass"])
schedule.every().tuesday.at("13:13").do(signIn,meeting_id = ohrana_truda['id'],password = ohrana_truda['pass'])
#wednesday
schedule.every().wednesday.at("08:43").do(signIn,meeting_id = sns["id"],password = sns['pass'])
schedule.every().wednesday.at("09:43").do(signIn,meeting_id = economika['id'],password = economika["pass"])
schedule.every().wednesday.at("10:43").do(signIn,meeting_id = kuzya["id"],password = kuzya['pass'])
schedule.every().wednesday.at("11:43").do(signIn,meeting_id = sns['id'],password = sns["pass"])
#thursday
schedule.every().thursday.at("08:43").do(signIn,meeting_id = ohrana_truda["id"],password = ohrana_truda['pass'])
schedule.every().thursday.at("09:43").do(signIn,meeting_id = kartbaeva['id'],password = kartbaeva["pass"])
schedule.every().thursday.at("10:43").do(signIn,meeting_id = economika["id"],password = economika['pass'])
#friday
schedule.every().friday.at("08:43").do(signIn,meeting_id = bisembeeva["id"],password = bisembeeva['pass'])
schedule.every().friday.at("09:43").do(signIn,meeting_id = bisembeeva['id'],password = bisembeeva["pass"])
schedule.every().friday.at("10:43").do(signIn,meeting_id = bisembeeva["id"],password = bisembeeva['pass'])


while True:
    schedule.run_pending()
    time.sleep(1)