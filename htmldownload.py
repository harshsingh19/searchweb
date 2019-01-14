# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:37:00 2019

@author: harsh
"""
try :
    import requests
    from bs4 import BeautifulSoup 
except ImportError:
    print ("Library not found")
def Get_html():
    
    url = str(input("Enter the url to be downloaded\n")).lower()
    if 'http://'in url or 'https://'in url:
        response = requests.get(url)
        html = response.text
        return html
    else:
        url = 'http://'+url
        response = requests.get(url,verify=False)
        html = response.text
        return html
def cleaning_html(html):
    text_val = BeautifulSoup(html)
    for script in text_val(["script","style"]):
        script.decompose()
    cleantext_html = ' '.join(text_val.stripped_strings)
    return cleantext_html

if __name__ == "__main__":
    html = Get_html()
    cleantext_html = cleaning_html(html)
    with open('website_html_data.txt','w') as f:
        f.write("%s\n" %html)  