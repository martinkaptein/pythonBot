import splinter
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import exceptions
import os
import urllib2
import glob
import time
browser = Browser('chrome')
driver = webdriver.Chrome
WhileCounter = 0
print 'Hey!'
uploadLocation = raw_input('What is the source of the file? Drag and drop file here (only on OSX):')
UserCounter = int(input('How many times repeat (something like 20)?? : '))
while WhileCounter < UserCounter:
    browser.visit('http://deepdreamgenerator.com/')
    uploadButton = browser.find_by_id('upload-form')
    uploadButton.click
#    uploadLocation = '/Users/mkaptein172/Pictures/dream/wallpaper_1371895785.jpg'
    browser.attach_file('file', uploadLocation)
    #Now, it's doing stuff
    #Be sure it is there
    time.sleep(25)
    #try to avoid sketchy stuff
    try:
        browser.click_link_by_partial_href('/ddream/')
    except selenium.common.exceptions.ElementNotVisibleException:
        #IF exception, wait, then try do stuff again 
        print 'Here was an exception, but we have dealt with the situation!'
        time.sleep(30)
        browser.reload()
        browser.click_link_by_partial_href('/ddream/')
#    browser.find_by_css('download-btn btn btn-primary').first.click()
    #It's downloading into Downloads
    time.sleep(20)
    #Make sure download finished

    filename = max(glob.iglob('/Users/mkaptein172/Downloads/*.jpg'), key=os.path.getctime)
    #get filename of download.jpg >> latest jpg in Download folder
    #print filename #debug
    os.rename(filename, uploadLocation)
    #Overwrite old (orig) file with new file ONLY ON OS X AND LINUX!!!!
    WhileCounter += 1
    print 'Progress: ', WhileCounter , ' out of ' , UserCounter
    
print uploadLocation , ' is finished!! Please check your source!'
browser.quit()