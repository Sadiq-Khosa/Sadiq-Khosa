import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Khosa=platform.architecture()[0]
if Khosa=="32bit":__import__("Khosa32")
elif Khosa=="64bit":__import__("Khosa64")

