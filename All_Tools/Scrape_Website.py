from os import link
import requests
from bs4 import BeautifulSoup

res=requests.get("https://news.ycombinator.com/news")
soup =BeautifulSoup(res.text,'html.parser')# (res.text)
#print(soup.body)


links=soup.select('.titlelink')
#print(links)






subtext=soup.select('.subtext')

def sort_stories_by_votes(hn):
    return sorted(hn,key= lambda k:k['votes'],reverse=True)





def Create_Custom_hn(links,subtext):
    hn=[]
    #print(subtext)
    #print(links)
    for index,items in enumerate(links):
        title=links[index].get_text()
        href=links[index].get("href",None)
        #print(href)
        vote=subtext[index].select('.score')
        #print(vote)
        if len(vote):
            points = int(vote[0].getText().replace('points',''))
            print(points)
            if points > 99:
                hn.append({'title' : title,'link' : href,'votes' : points})
    return sort_stories_by_votes(hn)            




print(Create_Custom_hn(links,subtext))






""" points=votes[0].get_text()
list_points=points.split()
x=int(list_points[0])+1
print(x)
print(list_points[0])

 """





