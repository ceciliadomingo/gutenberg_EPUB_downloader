#! python3
#Program that opens Chrome and searches for EPUBs on gutenberg
#Usage: gutenberg whatever_search_term

import sys, os, shutil, time, logging
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) 


#OPENING THE BROWSER
path_to_chromedriver = r'******YOUR/PATH/TO/CHROMEDRIVER******/chromedriver.exe'
browser = webdriver.Chrome(executable_path=path_to_chromedriver)
browser.get('https://www.gutenberg.org/')


#SEARCH FUNCTION
def getEPUBgutenberg(search_term):
    searchbar = browser.find_element_by_xpath('//*[@id="menu-book-search"]')
    searchbar.send_keys(search_term)
    #searchbar.submit() #Did not work, this web requires using button
    submit_button = browser.find_element_by_name('submit_search')
    submit_button.click()

#------------TRY FINDING RESULTS---------------:
    try:
        #Click on first result
        results = browser.find_elements_by_class_name('booklink')
        first_result = results[0]
        first_result.click()

        #........TRY FINDING EPUB WITH PICTURES........:
        try:
            #I use xpath to look for section of Download EPUB with pics
            #a are links, <a href="link.com" type="blahblah")
            #I search the text part <a href="bla.com">text</a>
            #using [contains(text(),'my text')]
            download_epub_withpics = browser.find_element_by_xpath("// a[contains(text(),'EPUB (with images)')]")
            download_epub_withpics.click()
            time.sleep(15) #Allow time for download

        #........NO PICTURES FOUND........:
        except:
            print(search_term + ' was not available as EPUB with pictures, searching without pictures.')

            #//////////TRY FINDING EPUB WITHOUT PICTURES//////////:
            try:
                download_epub_nopics = browser.find_element_by_xpath("// a[contains(text(),'EPUB')]")
                download_epub_nopics.click()
                time.sleep(15) #Allow time for download

            #//////////NO EPUB FOUND//////////:
            except:
                raise Exception(search_term + ' was not available as EPUB :(')

#------------NO RESULTS---------------:
    except: #No results
        raise Exception(search_term + ' returned no results.')

    #Closing the browser
    browser.quit()

#SEARCHING
#Getting the search term
logging.debug('sys.argv is %s' % sys.argv)
if len(sys.argv) > 1: #Item 1 is the program, I need more
    search_term_list = sys.argv[1:] #Include everything except index 0, the program name
    search_term_string = ' '.join(search_term_list)
    logging.debug('search term string is %s' % search_term_string)
    #Applying the seach function
    getEPUBgutenberg(search_term_string)
    
else: #No search term
    raise Exception('No search term was introduced')


#MOVING DOWNLOADED FILES TO EPUB FOLDER
os.chdir(r'******YOUR\DEFAULT\DOWNLOADS\FOLDER******\Downloads')
for file in os.listdir():
    logging.debug('something in listdir %s' % file)
    if os.path.isfile(file):
        logging.debug('general filename is %s' % file)
        if file.endswith('.epub'):
            newname = search_term_string + '.epub'
            newpath = '******YOUR\DEFAULT\DOWNLOADS\FOLDER******\\Downloads\\EPUBs bajados\\' + newname
            logging.debug('epub filename is %s' % file)
            logging.debug('newpath is %s' % newpath)
            shutil.move(file,newpath)
