import urllib2
from bs4 import BeautifulSoup as bs
def getPageData(url):
    soup = bs(urllib2.urlopen(url).read(),'html.parser')
    title = []
    price = []
    specs = []
    data = {}
    for tag in soup.find_all('div',{'class':'pu-title fk-font-13'}):
        title.append(tag.text.strip())
    for tag in soup.find_all('span',{'class':'fk-font-17 fk-bold'}):
        try:
            price.append(tag.text.strip())
        except:
            price.append("PRICE NOT AVAILABLE")
    for tag in soup.find_all('ul',{'class':'pu-usp'}):
        try:
            specs.append(tag.text.split('\n'))
        except:
            pass
    data['title'] = title
    data['price'] = price
    data['specs'] = specs
    return data

def displayData(data):
    n = len(data['title'])
    for i in range(n):
        print str(i+1) + ". " + data['title'][i].upper() + " -- " + data['price'][i]
        try:
            for spec in data['specs'][i]:
                print "\t" + spec
        except:
            pass

if __name__ == '__main__':
    url = raw_input("ENTER URL : ")
    data = getPageData(url)
    displayData(data)
    raw_input() #HOLD
            
