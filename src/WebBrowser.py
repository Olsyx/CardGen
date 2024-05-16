
from src.HtmlGenerator import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from urllib3.exceptions import NewConnectionError, MaxRetryError
import os
import time


class WebBrowser:

    web_path = ""
    driver = None


    @staticmethod
    def init(output_folder): 
        index_file = HtmlGenerator.html_file_path
        if not os.path.isabs(index_file):
            index_file = os.path.join(output_folder, index_file)

        WebBrowser.web_path = "file:///" + index_file
   

    @staticmethod
    def open(): 
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        WebBrowser.driver = webdriver.Chrome(chrome_options)
        WebBrowser.driver.get(WebBrowser.web_path)
    
    @staticmethod
    def refresh():      
        scrollX = WebBrowser.driver.execute_script("return window.pageXOffset")
        scrollY = WebBrowser.driver.execute_script("return window.pageYOffset")

        WebBrowser.driver.get(WebBrowser.web_path)
        WebBrowser.driver.execute_script("window.scrollTo(" + str(scrollX) + ", " + str(scrollY) +")")

    @staticmethod    
    def is_open() -> bool:
        """
        Checks if the webdriver is still open by checking the logs.
        """

        driver = WebBrowser.driver
        if driver == None:
            return False

        disconnected_msg = 'Unable to evaluate script: disconnected: not connected to DevTools\n'
        disc_msg = "Unable to evaluate script: no such window: target window already closed" \
                "\nfrom unknown error: web view not found\n"
        message_listener = "subscribing a listener to the already connected DevToolsClient"
        if driver:
            try:
                log = driver.get_log('driver')
            except (ConnectionRefusedError, MaxRetryError, NewConnectionError):
                # The webdriver is closed, the connection to the Chrome is refused.
                return False
            
            # print(f"is_driver_open(): log: {log}")
            
            if len(log) != 0:  # This does not catch all other messages.
                if log[-1]['message'] in (disconnected_msg, disc_msg):
                    print("Webdriver was closed.")
                    return False
                elif message_listener in log[-1]['message']:
                    # It's not closed.
                    return True
                else:
                    return True
            else:  # No errors, return True.
                return True