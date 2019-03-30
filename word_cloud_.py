# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:37:00 2019

@author: harsh
"""
#!/usr/bin/evn python
try :
    import requests
    from bs4 import BeautifulSoup
    from wordcloud import WordCloud,STOPWORDS
    from nltk.corpus import stopwords
    import re
    from filesaver import save_img,save_file
except ImportError:
    print ("Library not found")
def Get_html(url):
    if 'http://'in url or 'https://'in url:
        try:
            response = requests.get(url,verify=False)
            html = response.text.encode("utf-8")
            if str(html) is not None:
                return str(html)
            else:
                    pass
        except requests.exceptions.ConnectionError as e:
            print ("connection not establised")
            print(e)
            html = "connection not establised"
    else:
        try:
            url = 'http://'+url
            response = requests.get(url,verify=False)
            html = response.text.encode("utf-8")
            if str(html) is not None:
                return str(html)
            else:
                pass
        except requests.exceptions.ConnectionError as e:
            print ("connection not establised")
            print(e)
            html = "connection not establised"
def cleaning_html(html):
    if html is not None:
        text_val = BeautifulSoup(html)
        for script in text_val(["script","style"]):
            script.decompose()
        cleantext_html = ' '.join(text_val.stripped_strings)
        cachedStopWords = set(stopwords.words("english"))
        cleantext_html = cleantext_html.lower()
        cleantext_html = re.sub('\W+',' ',cleantext_html)#removing spsl character
        cleantext_html = re.sub("^\d+\s|\s\d+\s|\s\d+$"," ",cleantext_html)#removing words ending with number
        cleantext_html = re.sub(r"(^|\W)\d+","",cleantext_html)#removing words starting with number
        cleantext_html = re.sub(r'\b\d+(?:\.\d+)?\s+',' ',cleantext_html)#removing numbers
        cleantext_html = re.sub(r'^[^a-zA-Z]',r' ',cleantext_html)#non words
        cleantext_html = ' '.join(word for word in cleantext_html.split(' ') if len(word) >1)
        cleantext_html = ' '.join([word for word in cleantext_html.split() if word not in cachedStopWords]) 
        return cleantext_html
    else:
        pass
def word_count(cleantext_html):
    if cleantext_html is not None:
        counts = dict()
        words =cleantext_html.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        final_count = dict((key_count, value_count) for key_count, value_count in counts.items() if value_count > 1)
        return(final_count)
    else:
        pass
def word_cloud(cleantext_html):
    if cleantext_html is not None:         
        try:
            stopwords = set(STOPWORDS)
            wc = WordCloud(width =800,
                           height = 800,
                           background_color = 'white',
                           max_words=20,
                           stopwords = stopwords,
                           min_font_size =10
                           ).generate(cleantext_html)
            return wc
        except:
            pass
    else:
        pass

def percentage_count(query,cleantext_html):
    count1 = 0
    for i in query:
        count1 = cleantext_html.count(i) + count1
    cleantext_html = cleantext_html.split(" ")
    perc = round(((count1*100)/len(cleantext_html)),3)
    return perc

def main(url,query):
    html = Get_html(url)
    save_file(html,"text_data_store")
    cleantext_html = cleaning_html(html)
    save_file(cleantext_html,"html_data_store")
    xyz = word_count(cleantext_html)
    wc = word_cloud(cleantext_html)
    perc = percentage_count(query,cleantext_html)
    save_img(wc)
    return xyz, perc , len(cleantext_html)
