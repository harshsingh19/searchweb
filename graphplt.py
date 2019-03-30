#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:22:52 2019

@author: harsh
"""

import pylab
import os
import matplotlib.pyplot as plt
import time
def scateer_plot(data):
    plt.scatter(*zip(*data))
    if os.path.exists("scateer_plot"):
        if os.path.exists("scateer_plot/result.png"):
            plt.savefig('scateer_plot/result_{}.png'.format(int(time.time())))
            plt.close()
        else:
            plt.savefig('scateer_plot/result.png')
            plt.close()
    else:
        os.mkdir("scateer_plot")
        if os.path.exists("scateer_plot/result.png"):
            plt.savefig('scateer_plot/result_{}.png'.format(int(time.time())))
            plt.close()
        else:
            plt.savefig('scateer_plot/result.png')
            plt.close()
    plt.show()
    plt.close()
def pie_chart(sizes,labels):
    plt.pie(sizes,labels=labels, autopct='%1.1f%%',shadow=True,startangle=140)
    plt.axis('equal')
    if os.path.exists("pie_chart_data_store"):
        if os.path.exists("pie_chart_data_store/result.png"):
            plt.savefig('pie_chart_data_store/result_{}.png'.format(int(time.time())))
            plt.close()
        else:
            plt.savefig('pie_chart_data_store/result.png')
            plt.close()
    else:
        os.mkdir("pie_chart_data_store")
        if os.path.exists("pie_chart_data_store/result.png"):
            plt.savefig('pie_chart_data_store/result_{}.png'.format(int(time.time())))
            plt.close()
        else:
            plt.savefig('pie_chart_data_store/result.png')
            plt.close()
    plt.show()
    plt.close()
def histo_gram(li):
    l = 0
    for i in li:
        if len(i) >1:
            l = l+1
            plt.bar(range(len(i)), list(i.values()),align ='center')
            plt.xticks(range(len(i)),list(i.keys()))
            x = plt.gca().xaxis
            for item in x.get_ticklabels():
                item.set_rotation(45)
            plt.subplots_adjust(bottom =0.25)
            if os.path.exists("bar_graph_data_store"):
                if os.path.exists("bar_graph_data_store/result.png"):
                    plt.savefig('bar_graph_data_store/result_{}.png'.format(int(time.time())+l))
                    plt.close()
                else:
                    plt.savefig('bar_graph_data_store/result.png')
                    plt.close()
            else:
                os.mkdir("bar_graph_data_store")
                if os.path.exists("bar_graph_data_store/result.png"):
                    plt.savefig('bar_graph_data_store/result_{}.png'.format(int(time.time())+l))
                    plt.close()
                else:
                    plt.savefig('bar_graph_data_store/result.png')
                    plt.close()
            plt.show()
            plt.close()