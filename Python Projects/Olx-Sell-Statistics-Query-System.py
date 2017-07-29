

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 08:18:44 2017

@author: dipak
"""

loopVariable = input()
infoString=[]
queryString=[]

while(loopVariable!=0):
    string = raw_input()
    string = string.split(' ')
    count=0
    if string[0] == 'S':
         infoString.append(string[1]+" "+string[2]+" "+string[3])
    
    if string[0] == 'Q':
        queryString.append(string[1]+" "+string[2]+" "+string[3])
        
        for Qline in queryString:
            Qline = Qline.rstrip()
            
        for line in infoString:
            line = line.rstrip()
            
            if line == Qline:
                count+=1
            
            else:
                words = line.split()
                string[1]= str(float(string[1]))
                a=string[1].split('.')
                i=0
                if (int(a[1])!=0):
                    start = int(a[0])
                    end = int(a[1])
                    while (start!=end-1):
                        a.append(str(start+1))
                        start+=1
                    
                if (string[1] == words[0]) or (words[0] in a):
                    if (string[2] == words[1]): 
                        if (string[3] == str(int(float(words[2])))) or (string[3] == '-1'):
                            count+=1
                        
                    elif (string[2] == str(int(float(words[1])))):
                        if (string[3] == str(int(float(words[2])))) or (string[3] == words[2]) or (string[3] == '-1'):
                            count+=1
                            
                    elif (string[2] == '-1'):
                        if (string[3] == str(int(float(words[2])))) or (string[3] == words[2]) or (string[3] == '-1'):
                            count+=1
                     
        print count
    loopVariable-=1
    
    
    
