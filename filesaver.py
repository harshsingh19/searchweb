#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:47:20 2019

@author: harsh
"""
import os
import time
import pandas as pd
import matplotlib.pyplot as plt

def output_saving(websitelistfinal,values_websites,queries):
    try:
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
                    f.close()
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
                    f.close()
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
                    f.close()
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
                    f.close()
    except :
        print("Unable to save CSV data")
def save_img(wc):

    if wc is not None:
        try:
            plt.figure(figsize = (8,8),facecolor =None)
            plt.imshow(wc)
            plt.axis("off")
            plt.tight_layout(pad =0)
            if os.path.exists("image_data_store"):
                if os.path.exists("image_data_store/result.png"):
                    plt.savefig('image_data_store/result_{}.png'.format(int(time.time())))
                    plt.close()
                else:
                    plt.savefig('image_data_store/result.png')
                    plt.close()
            else:
                os.mkdir("image_data_store")
                if os.path.exists("image_data_store/result.png"):
                    plt.savefig('image_data_store/result_{}.png'.format(int(time.time())))
                    plt.close()
                else:
                    plt.savefig('image_data_store/result.png')
                    plt.close()
            plt.show()
        except:
            pass
    else:
        pass

def save_file(html,name_file):
    if html is not None:
        if os.path.exists(name_file):
            if os.path.exists(str(name_file+"/website_html_data.txt")):
                with open(str(name_file+'/website_html_data{}.txt').format(int(time.time())),'w') as f:
                    f.write("%s\n" %html)
                    f.close()
            else:
                with open(str(name_file+'/website_html_data.txt'),'w') as f:
                    f.write("%s\n" %html)
                    f.close()
        else:
            os.mkdir(name_file)
            if os.path.exists(str(name_file+"/website_html_data.txt")):
                with open(str(name_file+'/website_html_data{}.txt').format(int(time.time())),'w') as f:
                    f.write("%s\n" %html)
                    f.close()
            else:
                with open(str(name_file+'/website_html_data.txt'),'w') as f:
                    f.write("%s\n" %html)
                    f.close()
    else:
        pass