# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:30:47 2019

@author: harsh
"""

try :
    from googlesearch import search
    import pandas as pd
    import os
    import time
    from word_cloud_ import main as wc
    #import tldextract
except ImportError:
    print ("Library not found")


def Downloading_data():
    a = 0
    queries = []
    while a != 'exit':
        query = str(input("Enter the query to be searched \n"))
        if len(query) is 0:
            print ( "Please enter the query to search\n")
        else:
            values_websites = validinputs(query)
        queries.append(query)
        a = str(input('\nExit / For staying press enter.')).lower()      
    return values_websites,queries

def validinputs(query):
    domain = str(input("Enter the Domain to be searched \n1.USA\n2.UK\n3.Canada\n4.Austraila\n If search all domain leave null\n")).lower()
    if len(domain) == 0:
        values_websites = stringcheck(query,domain=0)
        return values_websites
    else :
        if isIntorString(domain):
            if int(domain)<5 and 0<int(domain):
                values_websites = stringcheck(query,domain)
                return values_websites
            elif 4<int(domain):
                print( "\nEnter a valid input")
                validinputs(query)
        else:
            values_websites = stringcheck(query,domain)
            return values_websites

def isIntorString(domain):
    for i in range(len(domain)):
        if domain[i].isdigit() != True:
            return False
    return True

def stringcheck(query,domain):

    dict_domain = {1:"com",'usa':"com",2:"co.uk",'uk':"co.uk",3:"ca",'canada':"ca",4:"com.au",'austraila':"com.au"}
    list_domain =["co.uk","com","ca","com.au"]
    i = 1
    values_websites = []
    if domain != 0:
        if isIntorString(domain):
            domain = int(domain)
            domain = dict_domain[domain]
            values_websites = query_return(domain,query)
            return values_websites
        else:
            if domain in dict_domain.keys():
                domain = dict_domain[domain]
                values_websites = query_return(domain,query)
                return values_websites
            else:
                print( "\nEnter a valid Input")
                validinputs(query)
    else:
        for j in range( len(list_domain)):  
            for result in search(query,tld = list_domain[j],num =100,stop=1,pause =2):
                print (str(i) + "-->" + result)
                i=i+1
                values_websites.append(result)
        return values_websites

def query_return(domain,query):
    #try :
    values_websites = []
    i = 1
    for result in search(query,tld = domain,num =100,stop=1,pause =2):
                print (str(i) + "-->" + result)
                i=i+1
                values_websites.append(result)
    return values_websites
#except AttributeError:
#        print("Value found Null")
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
    print("\n\n\n\nThe Website which contains the queries as domain name.")
    if len(websitelistfinal) > 0:
        for i in range(len(websitelistfinal)):
            print (websitelistfinal[i])
        websitelistfinal = list(set(websitelistfinal))
    else :
        print ( "No values Found")
    return websitelistfinal
    

def output_saving(websitelistfinal,values_websites):
    df = pd.DataFrame(websitelistfinal)
    df.columns = ['Website Address']
    if os.path.exists("xls_file_data"):
        if os.path.exists("xls_file_data/output_website.xls"):
            df.to_excel("xls_file_data/output_website{}.xls".format(int(time.time())),index =False)
        else:
            df.to_excel("xls_file_data/output_website.xls",index =False)
    else:
        os.mkdir("xls_file_data")
        if os.path.exists("xls_file_data/output_website.xls"):
            df.to_excel("xls_file_data/output_website{}.xls".format(int(time.time())),index =False)
        else:
            df.to_excel("xls_file_data/output_website.xls",index =False)
        
    with open('website_data/website_data.txt','w') as f:
        if os.path.exists("website_data"):
            if os.path.exists("website_data/website_data.txt"):
                with open('website_data/website_data{}.txt'.format(int(time.time())),'w') as f:                    
                    f.write("Queries \n\n")
                    for item in queries:
                        f.write("%s\n" %item)   
                    f.write("\n \n \nWebsite_final_list \n\n")
                    for item in websitelistfinal:
                        f.write("%s\n" %item)
                    f.write("\n \n \nValues_Websites \n\n")
                    for item in values_websites:
                        f.write("%s\n" %item)   
            else:
                with open('website_data/website_data.txt','w') as f:
                    
                    f.write("Queries \n\n")
                    for item in queries:
                        f.write("%s\n" %item)   
                    f.write("\n \n \nWebsite_final_list \n\n")
                    for item in websitelistfinal:
                        f.write("%s\n" %item)
                    f.write("\n \n \nValues_Websites \n\n")
                    for item in values_websites:
                        f.write("%s\n" %item)   
        else:
            os.mkdir("website_data")
            if os.path.exists("website_data/website_data.txt"):
                with open('website_data/website_data{}.txt'.format(int(time.time())),'w') as f:
                    
                    f.write("Queries \n\n")
                    for item in queries:
                        f.write("%s\n" %item)   
                    f.write("\n \n \nWebsite_final_list \n\n")
                    for item in websitelistfinal:
                        f.write("%s\n" %item)
                    f.write("\n \n \nValues_Websites \n\n")
                    for item in values_websites:
                        f.write("%s\n" %item)   
            else:
                with open('website_data/website_data.txt','w') as f:
                    
                    f.write("Queries \n\n")
                    for item in queries:
                        f.write("%s\n" %item)   
                    f.write("\n \n \nWebsite_final_list \n\n")
                    for item in websitelistfinal:
                        f.write("%s\n" %item)
                    f.write("\n \n \nValues_Websites \n\n")
                    for item in values_websites:
                        f.write("%s\n" %item)   
def sending_url(websitelistfinal):
    lst = []
    for i in websitelistfinal:
        lst.append(wc(i))
    return lst
if __name__ == "__main__":
    
    returned_list,queries = Downloading_data()
    returned_list2 = cleaing_data(returned_list) 
    returned_list3 = finding_string(returned_list2,queries)
    lst = sending_url(returned_list3)
    output_saving(returned_list3,returned_list)
