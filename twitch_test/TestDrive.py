import time
from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from twitch_test import page_object
from twitch_test import utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch:
	"""This class represent the test"""

	def __init__(self, mobile_emulator):
		"""Constructor for the class
		:arg
			mobile_emulator: Emulator"""
		self.service = Service(ChromeDriverManager().install())
		options = Options()

		self.mobile_emulator = mobile_emulator
		options.add_experimental_option(name="mobileEmulation", value=self.mobile_emulator)
		drive = webdriver.Chrome(service=self.service, options=options)
		self._drive = drive
		self.drive.implicitly_wait(30)

	@property
	def drive(self):
		return self._drive

	@drive.setter
	def drive(self, value):
		self._drive = value

	def wait_for(self, item, for_seconds=30):
		"""Waiting for specific amount of time"""
		WebDriverWait(self.drive, for_seconds).until(
			EC.visibility_of(item)
		)

	def go_landing_page(self):
		"""Go to the URL"""
		self.drive.get(url=page_object.URL)

	def click_search_button(self):
		"""Click in the search button"""
		search_button = self.drive.find_element(By.XPATH, page_object.search_button)
		search_button.click()

	def search_for(self, keyword):
		"""Search for specific keyword (channel)"""
		search_field = self.drive.find_element(By.XPATH, page_object.search_field)
		search_field.send_keys(keyword + Keys.RETURN)

	def switch_to_tab_channels(self):
		"""Switch to Tab Channel"""
		switch_to_channels = self.drive.find_element(By.XPATH, page_object.channels_tab)
		switch_to_channels.click()

	def scroll_down(self):
		"""Scroll down"""
		videos = self.drive.find_elements(By.XPATH, page_object.anchor_video_list)
		self.drive.execute_script("arguments[0].scrollIntoView();", videos[-1])

	def search(self, channel):
		"""Search for specific channel"""
		element = self.drive.find_elements(By.XPATH, page_object.anchor_video_list)
		try:
			WebDriverWait(self.drive, 30).until(
				EC.visibility_of(element[1])
			)
		except:
			print("error")
		creators_elements = self.drive.find_elements(By.TAG_NAME, 'h4')
		creators_list = {i.text: i for i in creators_elements}
		if channel in creators_list.keys():
			print("Found it ")
			return True

	def grap_random_channel(self):
		"""Grap random channel"""
		videos = self.drive.find_elements(By.XPATH, page_object.anchor_video_list)
		self.wait_for(item=videos[0], for_seconds=30)
		self.drive.execute_script("arguments[0].click();", videos[1])

	def scroll_down_search(self, times, channel="Miltrivd"):
		"""Scroll Down and search for a channel"""
		flag = True
		for _ in range(times):
			if self.search(channel=channel):
				user_name = utils.clean_user_name(channel).lower()
				self.click_on_video(video=f"//a[@href='/{user_name}']")
				flag = False
				break
			else:
				self.scroll_down()
		if flag:
			self.grap_random_channel()

	def click_on_video(self, video=page_object.video_on_list):
		"""Click on video"""
		video_tag = self.drive.find_element(By.XPATH, '//video')
		self.wait_for(item=video_tag, for_seconds=30)
		try:
			video = self.drive.find_element(By.XPATH, video)
			video.click()
		except ElementClickInterceptedException:
			print("Element cannot be click")

	def close_modal(self):
		"""Close modal suggesting lightweight"""
		video_tag = self.drive.find_element(By.XPATH, '//video')
		self.wait_for(item=video_tag, for_seconds=30)
		try:
			x = self.drive.find_element(By.XPATH, page_object.close_try_lightweight_twitch_modal)
			x.click()

		except AttributeError:
			print("the modal is not present")
		except NoSuchElementException:
			print("the modal is not present")

	def click_start_watching(self):
		"""Click Warning button"""
		try:
			start = self.drive.find_element(By.XPATH, page_object.start_streaming_button)
			start.click()
		except AttributeError:
			print("some attributes are incorrect ")
		except ElementNotInteractableException:
			print('the "start streaming" button is not present')

	def wait_number_second(self, seconds=5):
		time.sleep(seconds)

	def take_snapshot(self):
		"""Take a snapshot"""
		body = self.drive.find_element(By.XPATH, page_object.full_page)
		current_time = utils.get_current_date()
		body.screenshot(filename=f"{current_time}.png")




# user_agent_android = "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
# user_agent_iPhone = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'"

# search_result.screenshot("image2.png")
#
# browser.quit()
