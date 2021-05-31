#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:06:33 2021

@author: chrismacbook
"""

class LogAccess:
   
    def __init__(self):
       pass
        
    def openAndStoreTxtFile(self, filePath, question):
        with open(filePath, 'a') as file:
            file.write(question)
            file.write('\n')
            
            
        