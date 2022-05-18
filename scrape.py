import requests
from bs4 import BeautifulSoup
from pprint import pprint
scrapedData=[]       # list of scraped articles
articlesDict={}      #  data of an article

'''
articlesDict={'title_link':'','cited_by_link':'','line1':'','line2':'',
'title':'','year':'','cited_by':''}
'''

# Making a GET request

r = requests.get('https://scholar.google.com/citations?view_op=list_works&hl=en&hl=en&user=5zbn8FcAAAAJ')
  
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# finding articles 
articles=soup.find_all('tr',class_='gsc_a_tr')
#print(articles)

links=['title_link','cited_by_link']
lines=['line1','line2']
for article in articles:
    for key,link in zip(links,article.find_all('a')):
        val=link.get('href')
        if(key=='title_link'):
            val="https://scholar.google.com"+val
        articlesDict[key]=val
    for key,line in zip(lines,article.find_all('div',class_='gs_gray')):
        articlesDict[key]=line.text
    # get the title
    articlesDict['title']=article.find('td',class_='gsc_a_t').text
    # get the year
    articlesDict['year']=article.find('span',class_='gsc_a_h gsc_a_hc gs_ibl').text
    # get the cited by data
    articlesDict['cited_by']=article.find('a',class_='gsc_a_ac gs_ibl').text
    
    # append the scraped article to list
    scrapedData.append(articlesDict)
pprint(scrapedData)