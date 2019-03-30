# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:30:47 2019

@author: harsh
"""
#!/usr/bin/evn python
try :
    from googlesearch import search
    from word_cloud_ import main as wc
    from filesaver import output_saving
    from graphplt import pie_chart,histo_gram,scateer_plot
    import urllib
    import re
    from urllib.parse import urlparse
    import tldextract

except ImportError:
    print ("Library not found")

values_websites = []
queries = []
def dic_split(d):
    sizes=[]
    labels = []
    for i,j in d.items():
        labels.append(i)
        sizes.append(j)
    list3 = [list(a) for a in zip(sizes,labels)]
    return list3 ,labels ,sizes
def domain_type(_list,_count):
    urls = []
    for i in _list:
        a = tldextract.extract(i).suffix
        urls.append(a)
    d = {x:urls.count(x) for x in urls}
    list3 ,labels ,sizes= dic_split(d)
    di = {}
    count =0
    for i in list3:
        cou = i[0]
        val = i[1]
        if i[0]>=_count:
           di[str(val)]=int(cou)
        else:
            count = count+1
    if count >0:
        di['others']=count
    list3 ,labels ,sizes=dic_split(di)
    pie_chart(sizes, labels)
def Downloading_data():
    a = 0
    global queries
    values_web = []
    while a != 'exit':
        query = str(input("Enter the query to be searched \n"))
        if len(query) is 0:
            print ( "Please enter the query to search\n")
        else:
            values_websites = validinputs(query)
            search_query = query.split("\"")
            search_query = [x for x in search_query if x is not None]
            for j in search_query:    
                queries.append(j)
        if type(values_websites) == str:
            values_web.append(values_websites)
            break
        else:
            values_web.append(values_websites)
        
        a = str(input('\nExit / For staying press enter.')).lower() 
        if values_web == None:
            print("Exit without output")
    return values_web[0],queries

def key_word_domain_name(returned_list_):
    list_webpage =[]
    key_words = str(input("\nEnter Key Words if you want to have certain keywords to look after comma seprated\n"))
    key_words = key_words.split(",")
    for i in key_words:
        for j in returned_list_:
            if i in j:
                list_webpage.append(j)
    list_webpage = list(set(list_webpage))
    return list_webpage, key_words

def key_word_domain_content(key_words,lst):
    list_content = []
    for i in lst:
        for j,k in i.items():
            for l in key_words:
                if l in j and k>7:
                    list_content.append(i)
    return list_content

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
    global values_websites
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
        try:
            for j in range( len(list_domain)):  
                for result in search(query,tld = list_domain[j],num =100,stop=1,pause =2):
                    print (str(i) + "-->" + result)
                    i=i+1
                    values_websites.append(result)

            return values_websites
        except urllib.error.HTTPError as e:
            print("Service Unavailable")
            print(e)
            return "Service Unavailable"
            
def query_return(domain,query):
    try :
        try:
            global values_websites
            i = 1
            for result in search(query,tld = domain,num =100,stop=1,pause =2):
                        print (str(i) + "-->" + result)
                        i=i+1                    
                        if len(values_websites)==0:
                            values_websites.append(result)
                        else:
                            values_websites.append(result)
    
            
            return values_websites
        
        except :
             print("Service Unavailable")
             return "Service Unavailable"
    except urllib.error.HTTPError as e:
        print("Service Unavailable")
        print(e)
        return "Service Unavailable"

def second_data(values_websites,queries):
    second_final_list = []
    for link in values_websites:
        review = link.lower()
        review = review.split("://")
        review = re.split(r"[^a-zA-Z0-9\s]",review[1])
        review = list(set(review))
        x = 0
        for i in review:
            for word in queries:
                if x <4: 
                    if i == word:
                        second_final_list.append(link)
            x = x+1
    return second_final_list
        
def removing_listed_webpage(_list):
    val = []
    with open('xyzq.txt','r') as f:
        words = f.read().lower().split("\n")
    for i in _list:
        for j in words:
            url = urlparse(i).hostname
            if (j in url.lower()):
                val.append(i)
    val = [z for z in _list if z not in val]
    val = list(set(val))
    return val

def cleaing_data(values_websites):
    new_data =[]
    a = len(values_websites)
    if a>0:
        for j in range(0, a):
            if returned_list[j] != None:
                url = values_websites[j]
                review = urlparse(url).hostname
                new_data.append(review)
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
    

def sending_url(websitelistfinal,queries,key_words):
    lst = []
    perc= []
    key_words = queries + key_words
    for i in websitelistfinal:
        x, y, z= wc(i, key_words)
        lst.append(x)
        perc.append((y,z))
    scateer_plot(perc)
    return lst, perc
def graph1(lst):
    m={}
    li = []
    for i in lst:
        for j,k in i.items():
            if int(k) > 12:
                if 'x' not in j:
                    m[j]=k
        li.append(m)
        m={}
    histo_gram(li)
    return li    
if __name__ == "__main__":
    returned_list,queries = Downloading_data()
    if "Service Unavailable" in returned_list:
        print("No values found")
    else:   
        returned_list2 = cleaing_data(returned_list)
        returned_list3 = finding_string(returned_list2,queries)
        returned_list4 = second_data(returned_list,queries)
        
        key_counted_list, key_words = key_word_domain_name(returned_list4)
        key_counted_list = removing_listed_webpage(key_counted_list)
        cleaned_key_counted_list = cleaing_data(key_counted_list)
        
        returned_list5 = removing_listed_webpage(returned_list4)
        returned_list6 = cleaing_data(returned_list5)+cleaned_key_counted_list
        returned_list6 = list(set(returned_list6))
        for i in returned_list6:
            print(i)
        lst, perc= sending_url(returned_list3,queries,key_words)
        lst = [x for x in lst if x is not None]
        _lst = key_word_domain_content(key_words,lst)

        li = graph1(_lst)
        li2 = graph1(lst)
        domain_type(returned_list,5)
        domain_type(returned_list3,0)
        
        output_saving(returned_list3,returned_list,queries)
