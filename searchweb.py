# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:30:47 2019

@author: harsh
"""

try :
    from googlesearch import search
    import pandas as pd
    #import tldextract
except ImportError:
    print ("No module named google found")



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

websitelistfinal = []
a = len(new_data)
for i in range(len(queries)):
    for j in range(a):
        if queries[i] in new_data[j]:
            websitelistfinal.append(new_data[j])
print("\n\n\n\n The Website which contains the queries as domain name.")
for i in range(len(websitelistfinal)):
    print (websitelistfinal[i])
websitelistfinal = list(set(websitelistfinal))
df = pd.DataFrame(websitelistfinal)
df.columns = ['Website Address']
df.to_excel("D:\\output_website.xls",index =False)
with open('website_data.txt','w') as f:
    f.write("Queries \n\n")
    for item in queries:
        f.write("%s\n" %item)   
    f.write("\n \n \nWebsite_final_list \n\n")
    for item in websitelistfinal:
        f.write("%s\n" %item)
    f.write("\n \n \nValues_Websites \n\n")
    for item in values_websites:
        f.write("%s\n" %item)   
