# FlipkartBot
This is a robot that fetches a list of products displayed on a particular page of flipkart

# Required Libraries:
1. BeautifulSoup4 
2. urllib2

# Functions:
1. getPageData(url):
      Takes in a url (only flipkart). Fetches the titles, prices and specs of all the products displayed on the page.
      It returns a dictionary of the format : {'title':[...],'price':[...],'specs':[[...],[...],...]}.
2. displayData(dict):
      Takes the data obtained by getPageData(url), and displays it in order.
