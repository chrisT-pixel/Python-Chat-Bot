#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:47:24 2021

@author: chrismacbook
"""

from matching import Matching
from question_log_access import LogAccess


#once doing this investigate if abstract class is suitable for best_question
#class - maybe not as then this class needs access to question class??
#get interface right for this manager 
#format console questions?
#testing 


class QuestionAnsweringManager:
   
    def __init__(self):
        #self.questionAnswering = inMemoryQuestionAnsweringAccessor()
        pass


    
    def answer_question(self, question_text):
        
        logAccess = LogAccess()
        logAccess.openAndStoreTxtFile('asked_questions_log.txt', question_text)
        
        matching = Matching(question_text)
        candidate, highestScore = matching.match()
        
        return candidate, highestScore
    
        
      
    

#class inMemoryQuestionAnsweringAccessor:
#    def __init__(self):
#        self.questionAnswering = inMemoryQuestionAnswering()
        
#    def answer_question(self, question_text):
#        print('question answered')
#        pass
        

#class inMemoryQuestionAnswering:
#     def __init__(self):
#         self.answers = []
#         pass
     
     
#     def answer_question(self, question_text):
#         print('question answered')
#         pass

#implementation here - bubbles up to the top level manager