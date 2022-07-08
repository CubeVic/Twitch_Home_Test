from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from twitch_test import page_object


class Twitch:

	def __init__(self, mobile_emulator):
		self.service = Service(ChromeDriverManager().install())
		options = Options()

		self.mobile_emulator = mobile_emulator
		options.add_experimental_option(name="mobileEmulation", value=self.mobile_emulator)
		drive = webdriver.Chrome(service=self.service, options=options)
		self._drive = drive
		self.drive.implicitly_wait(60)

	@property
	def drive(self):
		return self._drive

	@drive.setter
	def drive(self, value):
		self._drive = value

	def go_landing_page(self):
		self.drive.get(url=page_object.URL)

	def click_search_button(self):
		search_button = self.drive.find_element(By.XPATH,page_object.search_button)
		search_button.click()

	def search_for(self, keyword):
		search_field = self.drive.find_element(By.XPATH, page_object.search_field)
		search_field.send_keys(keyword + Keys.RETURN)

	def switch_to_tab_channels(self):
		switch_to_channels = self.drive.find_element(By.XPATH, page_object.channels_tab)
		switch_to_channels.click()

	def find_user(self, user_name):
		# find_first_video = self.drive.find_element(By.XPATH, "//div[@role='list']")
		# print(find_first_video)
		names = []
		elements = []
		for _ in range(2):
			self.drive.find_element(By.XPATH, "//div[@role='list']//a").send_keys(Keys.END)
			f = self.drive.find_elements(By.TAG_NAME, 'h4')
			for i in f:
				if i.text not in names:
					names.append(i.text)
					elements.append(i)
				print(i.text)
				# print(f"get the location {i.location}")
		print(names)
		# print(elements)
		print(True if user_name in names else False)

		el = self.drive.find_element(By.XPATH, "//div[@class='Layout-sc-nxg1ff-0 cIRhsZ']")
		el.click()

	def click_on_video(self):
		video = self.drive.find_element(By.XPATH, '//div/a')
		video.click()

	def click_start_watching(self):
		try:
			x = self.drive.find_element(By.XPATH, "//button[@aria-label='Close']")
			x.click()
		except:
			pass

		start= self.drive.find_element(By.XPATH,'//button/div/div[@data-a-target="tw-core-button-label-text"]')
		start.click()




# user_agent_android = "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
# user_agent_iPhone = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'"

# search_result.screenshot("image2.png")
#
# browser.quit()
