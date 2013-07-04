from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
# This is required for virtual display
#from pyvirtualdisplay import Display

def set(element, keys):
	element.click()
	element.clear()
	element.send_keys(keys)

fireFoxProfile = FirefoxProfile()
fireFoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/comma-separated-values;text/csv;application/csv;application/excel;application/vnd.ms-excel;application/vnd.msexcel;text/anytext")
fireFoxProfile.set_preference("browser.helperApps.alwaysAsk.force", False)
fireFoxProfile.set_preference("browser.download.manager.addToRecentDocs", False)
fireFoxProfile.set_preference("browser.download.manager.closeWhenDone", False)
fireFoxProfile.set_preference("browser.download.manager.focusWhenStarting", False)
fireFoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
fireFoxProfile.set_preference("browser.download.manager.useWindow", False)
fireFoxProfile.set_preference("browser.download.folderList", 2)
fireFoxProfile.set_preference("browser.download.dir", "D:\\Data")

# This will launch the virtual display.  
#display = Display(visible=0, size=(800, 600))
#display.start()

# Set these any way you like: paste them here (bad), pass them in (less bad)
user = ''
password = ''
baseUrl = "http://www.shapeways.com/login"

d = webdriver.Firefox(fireFoxProfile)
d.get(baseUrl)
WebDriverWait(d,10).until(lambda d: d.find_element_by_css_selector("#login_username"))

login = d.find_element_by_css_selector("#login_username")
set(login, user)
passwd = d.find_element_by_css_selector("#login_password")
set(passwd, password)

d.find_element_by_css_selector(".login-lonely-button").click()

d.get("http://www.shapeways.com/shop/download-payments-overview")

time.sleep(5)
d.close()