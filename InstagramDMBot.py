import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

myemail = "slowfashiontest@gmail.com"
mypassword = "2ZSX\"edc"
numoftimes = "1"
numofmessages= 0
friendusernames = []
data = pandas.read_csv('scrapping1.csv')
df = pandas.DataFrame(data)
for key, value in df.iteritems():
    friendusernames.append(value)
message = "Hello there, this is Slow Fashion Test, I sent this from an automatic script"
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

url = "https://www.instagram.com/"
driver.get(url)

try:
    try:
        cookiebutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.aOOlW')))
        cookiebutton.click()
        print("Cookies Validated")
    except:
        print("No cookies to validate")
    try:
        usernamebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        usernamebox.send_keys(myemail)
        passwordbox = driver.find_element_by_name('password')
        passwordbox.send_keys(mypassword)
        loginbutton = driver.find_element_by_css_selector('.Igw0E')
        loginbutton.click()
        print("Logging in")
    except:
        print("Could not login!")
    for friendusername in friendusernames:
        try:
            dmbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xWeGp')))
            dmbtn.click()
        except:
            print ("Could not find or click the direct message button")
        try:
            notificationsnotnow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.HoLwm')))
            notificationsnotnow.click()
        except:
            print ("Could not click not now on the notifications pop up!")
        try:
            searchuser = driver.find_element_by_css_selector('.S-mcP .wpO6b')
            searchuser.click()
            print('user message button : done')
        except:
            print ("Could not click on the new message button!")

        try:
            driver.implicitly_wait(5)
            searchuserbox = driver.find_element_by_css_selector('.focus-visible')
            searchuserbox.click()
            searchuserbox.send_keys(friendusername)
        except:
            print ("Could not find the enter username box!")
        try:
            time.sleep(2)
            firstuser = driver.find_element_by_css_selector('.HVWg4:first-of-type')
            firstuser.click()
            print('select first user : done')
        except:
            print("Could not click on the first user!")

        try:
            pressingnext = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rIacr')))
            pressingnext.click()
        except:
            print ("Could not press \"Next\"!")

        try:
            messagebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.focus-visible')))
            messagebox.click()
        except:
            print ("Could not find the text box!")

        try:
            textbox = driver.find_element_by_css_selector('.focus-visible')
        except:
            print("Could not find the text box!")

        try:
            for i in range(int(numoftimes)):
                textbox.send_keys(message)
                textbox.send_keys(Keys.RETURN)
                numofmessages= numofmessages+1
        except:
            print("Error sending the message!")

except:
    print("An error has occurred")
    time.sleep(1)
    driver.quit()
