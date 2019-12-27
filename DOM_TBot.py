from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time


# * PATH SETTING FOR SELENIUM INTEGRATION WITH FIREFOX TO WORK PROPERLY

# * SETTING THE FIREFOX BINARY
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')

# * FETCHING THE DESIRED FUNCTIONALITIES
caps = DesiredCapabilities.FIREFOX.copy()
caps['marionette'] = True

# * SETTING DRIVER PATH
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps,
                           executable_path=r'C:\Users\US\AppData\Local\Programs\Python\Python38-32\geckodriver.exe')

# * CLASS FOR STORING THE BOT'S RELATED METHODS, MORE USEFULL IN CASE YOU WANT TO EXTEND/MODIFY IT
class TwitterBot:
    # * USED FOR INITIALISING THE BOT
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    # * USED FOR LOGGING IN TO YOUR ACCOUNT
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(10)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(30)

    # * 
    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd_query')
        time.sleep(5)
        for i in range(1, 10):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                bot.find_element_by_class_name('HeartAnimation').click()
                time.sleep(30)


# * USE YOUR OWN CREDENTIALS HERE
us = TwitterBot('your-username', 'your-password')

us.login()

# * PUT IN THE STRING OR HASHTAG YOU WANT TO SEARCH AND LIKE
us.like_tweet('#100daysofcode')
