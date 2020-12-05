from datetime import datetime, date, timedelta
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from robot.libraries.BuiltIn import BuiltIn
from pynput.keyboard import Key, Controller
from robot.api import logger
from QWeb.internal import frame, decorators, browser,  exceptions, element, download
import glob
import os

L = ['-', '31.12.2017', '31.10.2018', '20.10.2019', '30.12.2021', '-', '31.12.2027', '-', '-', '31.12.2023', '1.3.2020', '30.1.2021', '-', '31.12.2019', '-', '-', '-', '27.2.2021', '-']


time = datetime.strptime('04.11.2020', '%d.%m.%Y')
print(time)
for i, el in enumerate(L):
    # print(el)
    try:
        el = datetime.strptime(str(el), '%d.%m.%Y')
        print(el)
    except:
        continue
    if el > time:
        print(i)
        break

