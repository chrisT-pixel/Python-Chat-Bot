#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:11:04 2021

@author: chrismacbook
"""
from utils import jaccard_similarity_score
from utils import strip_punctuation
from utils import text_to_words
from utils import words_to_lowercase
from question_catalogue_access import StoreAccess
from best_question import BestQuestion

class Matching:
    def __init__(self, question_text):
        self.question_text = question_text
        
    def sanitiseText(self, question):
        
        emptyString = " "
        sanitisedPunctuation = strip_punctuation(question)
        sanitisedWords = text_to_words(sanitisedPunctuation)
        sanitisedQuestionList = words_to_lowercase(sanitisedWords)
        sanitisedQuestionString = emptyString.join(sanitisedQuestionList)
        return sanitisedQuestionString
        
    def match(self):
        
        storeAccess = StoreAccess('faq.json')
        data = storeAccess.openJson()
        
        sanitisedUserQuestionString = self.sanitiseText(self.question_text)
        
        i = 0
        highestScore = 0.0
        
        for a_dict in data:
            
            sanitisedStoreQuestionString = self.sanitiseText(data[i]['question'])
            
            questionScore = jaccard_similarity_score(sanitisedUserQuestionString, sanitisedStoreQuestionString)
           #greater than or equal to??
            if(questionScore > highestScore):
                
                highestScore = questionScore
                bestQuestion = data[i]['question']
                bestIndex = i
            
            i+=1
                       
        
        bestAnswer = data[bestIndex]['answer']
       
        candidate = BestQuestion(bestQuestion, bestAnswer)
        
        return candidate, highestScore
    

    
   