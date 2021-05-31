#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:51:37 2021

@author: chrismacbook
"""
import json

class StoreAccess:
    def __init__(self, filePath):
        self.filePath = filePath
        
    def openJson(self):
        with open(self.filePath) as file:
            data = json.load(file)
        return data
        