from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
user_agent_android = "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
user_agent_iPhone = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'"
mobile_emulator = {"deviceName": "iPhone XR"}

# mobile_emulator = {
#     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#     "userAgent": user_agent_iPhone }
# options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

options.add_experimental_option("mobileEmulation", mobile_emulator)

# service = "chromedriver_103.exe"

service = Service(ChromeDriverManager().install())


# browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser = webdriver.Chrome(service=service, options=options)

browser.get('http://twitch.tv')
element = '/html/body/div/div/div/nav/div/div/div[2]/div/input[@type="search"]'

el = '//div/a/button'
search = '//div/input'

elem = browser.find_element(By.XPATH, el)  # Find the search box
elem.click()
elem = browser.find_element(By.XPATH, search)
elem.click()
elem.send_keys('Mounster hunter' + Keys.RETURN)
search_result = browser.find_element(By.XPATH, "//main/div/div/section")
search_result.screenshot("image2.png")

browser.quit()