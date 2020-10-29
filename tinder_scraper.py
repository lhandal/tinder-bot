# MIT License
#
# Copyright (c) 2020 Leandro Handal
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from secrets import username, password
import os
from webptools import webplib as webp
import urllib.request
import datetime
import subprocess

pictures_folder = ""

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # def passport(self, lat=40.7128, lon=-74.0060):
    #     params = {
    #     "latitude": lat,
    #     "longitude": lon,
    #     "accuracy": 100}
    # self.driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

    def login(self):
        self.driver.maximize_window()

        self.driver.get('https://tinder.com')

        sleep(3)

        # Click on login button
        login_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_button.click()

        sleep(1)

        # Log in with Facebook
        login_with_facebook_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button/span[2]')
        login_with_facebook_button.click()

        # Marks base window to go back after facebook login window
        base_window = self.driver.window_handles[0]

        # Selects Facebook login window for interaction
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Inputs Facebook credentials and submits
        email_input_field = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input_field.send_keys(username)

        password_input_field = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_input_field.send_keys(password)

        facebook_login_button = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        facebook_login_button.click()

        sleep(8)

        # Switch back to Tinder main window
        self.driver.switch_to.window(base_window)

        # Dismiss pop-ups

        # Cookies
        accept_cookies_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span')
        accept_cookies_button.click()

        # Location
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        popup_1.click()

        # Notifications
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        popup_2.click()

        sleep(5)

        # Agree to passport mode and select city
        # passport_popup_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/a')
        # passport_popup_button.click()

        # sleep(5)

        # select_location_accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[2]/button')
        # select_location_accept.click()

        sleep(2)

    # Like action
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    # Dislike action
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    # Save picture
    def get_pic_path(self):
        try:
            pic_path = bot.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span[1]/div')
            pic_url = pic_path.get_attribute('style').split('"')[1]

        except:
            pic_path = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div')
            pic_url = pic_path.get_attribute('style')[0].split('"')[1]
        return pic_url

    def download_tinder_jpeg(self, file_name):
        path = pictures_folder

        try:
            pic_path = bot.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span[1]/div')
            pic_url = pic_path.get_attribute('style').split('"')[1]

        except:
            pic_path = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div')
            pic_url = pic_path.get_attribute('style')[0].split('"')[1]

        full_path = path + '/' + file_name + '.webp'
        urllib.request.urlretrieve(pic_url, full_path)
        print('Photo downloaded...')
        decoder = webp.dwebp(full_path, full_path[:-5] + ".jpg", "-o")
        print("Converting to jpeg...")
        print(decoder['stderr'])
        os.remove(full_path)
        print("WebP file removed!")


    # Auto-swipe right
    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                pic_id = datetime.datetime.now().strftime('%d%H%M%S%f')
                print(pic_id)
                try:
                    self.download_tinder_jpeg(pic_id)
                    self.dislike()
                except IndexError:
                    self.dislike()
            except Exception:
                print('Auto_swipe exception...')
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    # Close offer pop-up
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    # Close match pop-up
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()

logged_in = False
while not logged_in:
    try:
        bot.login()
        logged_in = True
        break
    except:
        bot.driver.quit()
        bot = TinderBot()
        logged_in = False

sleep(5)

# bot.passport()

bot.auto_swipe()

# subprocess.call(['osascript', '-e', 'tell application "Chrome" to quit'])
# os._exit(0)
