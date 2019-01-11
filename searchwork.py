# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:30:47 2019

@author: harsh
"""

try :
    from googlesearch import search
    #import tldextract
except ImportError:
    print ("No module named google found")


def Downloading_data():
    a = 0
    i = 1
    values_websites = []
    queries = []
    while a != 'exit':
        query = str(input("Enter the query to be searched "))
        queries.append(query)
        for result in search(query,tld = "com",num =100,stop=1,pause =2):
            print (str(i) + "-->" + result)
            i=i+1
            values_websites.append(result)
        for result in search(query,tld = "co.uk",num =100,stop=1,pause =2):
            print (str(i) + "-->" + result)
            i=i+1
            values_websites.append(result)
        for result in search(query,tld = "ca",num =100,stop=1,pause =2):
            print (str(i) + "-->" + result)
            i=i+1
            values_websites.append(result)
        for result in search(query,tld = "com.au",num =100,stop=1,pause =2):
            print (str(i) + "-->" + result)
            i=i+1
            values_websites.append(result)
        a = str(input('Exit / For staing press enter.'))        
    return values_websites,queries
def cleaing_data(values_websites):
    new_data =[]
    a = len(values_websites)
    for j in range(0, a):
        review = values_websites[j]
        review = review.lower()
        spltAr = review.split("://")
        i = (0,1)[len(spltAr)>1]
        review =spltAr[i].split("?")[0].split('/')[0].lower()
        new_data.append(review)
    new_data = list(set(new_data))
    return new_data

def finding_string(new_data,queries):
    websitelistfinal = []
    a = len(new_data)
    for i in range(len(queries)):
        for j in range(a):
            if queries[i] in new_data[j]:
                websitelistfinal.append(new_data[j])

    for i in range(len(websitelistfinal)):
        print (websitelistfinal[i])
if __name__ == "__main__":
    returned_list,queries = Downloading_data()
    returned_list2 = cleaing_data(returned_list) 
    finding_string(returned_list2,queries)
