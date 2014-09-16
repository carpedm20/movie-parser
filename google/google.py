import sys # Used to add the BeautifulSoup folder the import path
import urllib2 # Used to read the html document
from time import sleep

if __name__ == "__main__":
    ### Import Beautiful Soup
    ### Here, I have the BeautifulSoup folder in the level of this Python script
    ### So I need to tell Python where to look.
    sys.path.append("./BeautifulSoup")
    from BeautifulSoup import BeautifulSoup

    ### Create opener with Google-friendly user agent
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    ### Open page & generate soup
    ### the "start" variable will be used to iterate through 10 pages.
    for start in range(0,4680):
        sleep(1)
        # https://www.google.com/search?q=inurl:https://watcha.net/m/mv/+-staffs&newwindow=1&biw=1095&bih=617&ei=tr0YVK3JEYH78QXHv4CICQ&start=20&sa=N&filter=0
        url = "https://www.google.com/search?q=inurl:https://watcha.net/m/mv/+-staffs+-comments+-similar_movies&newwindow=1&biw=1095&bih=617&ei=tr0YVK3JEYH78QXHv4CICQ&sa=N&filter=0&start=" + str(start*10)
        page = opener.open(url)
        soup = BeautifulSoup(page)

        ### Parse and find
        ### Looks like google contains URLs in <cite> tags.
        ### So for each cite tag on each page (10), print its contents (url)
        for cite in soup.findAll('cite'):
            print cite.text
