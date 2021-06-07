# TODO add your tests here
#Unit tests for all components defined
#• Each test has a single objective
#• Comprehensive test suite covering all normal situations, exception
#situations, and boundary situations
#• All tests run without errors


import pytest
from unittest.mock import Mock, patch, mock_open
from question_answering_manager import QuestionAnsweringManager
from matching import Matching
from question_log_access import LogAccess
from question_catalogue_access import StoreAccess
from best_question import BestQuestion
from utils import jaccard_similarity_score
#from main import main 

@pytest.fixture
def manager():
    accessor = QuestionAnsweringManager()
    return QuestionAnsweringManager(accessor)

@pytest.fixture
def scenario1_question_answering_manager(manager):
    manager.answerQuestion("what day is it tomorrow")
    
    
def test_open_and_store_txt_file(tmpdir):
    file = tmpdir.join('asked_questions_log.txt')
    logAccess = LogAccess()
    logAccess.openAndStoreTxtFile(file.strpath, question='I am a test question')
    assert file.read() == 'I am a test question\n'
    
def test_json_return_type():
   storeAccess = StoreAccess('faq.json') 
   data = storeAccess.openJson()
   assert type(data) is list
   #mention learning about the returned data via these tests
   
def test_json_returned_items_are_dict():
    storeAccess = StoreAccess('faq.json') 
    data = storeAccess.openJson()
    for value in data:
        assert type(value) is dict
        
        
def test_json_returned_questions():
    testQuestion = 'What day is today?'
    storeAccess = StoreAccess('faq.json') 
    data = storeAccess.openJson()
    assert data[0]['question'] == testQuestion
    
def test_json_returned_answers():
    testAnswer = 'Monday'
    storeAccess = StoreAccess('faq.json') 
    data = storeAccess.openJson()
    assert data[0]['answer'] == testAnswer
   
def test_sanitise_text():
    matching = Matching("What&@is the< best@ Weather(*")
    sanitisedString = matching.sanitiseText(matching.question_text)
    assert sanitisedString == "what is the best weather"
    #note underscores not being stripped - maybe refactor and add to reflection
    #reverse engineer this to use a few fixtures
    
def test_matching_return_type():
     matching = Matching("What are the weathers like todays")
     testMatchEngineResult = matching.match()
     #assert testMatchEngineResult == BestQuestion('What is the weather like today?', 'Same as yesterday.'), '1.0'
     #assert testMatchEngineResult == type(testMatchEngineResult) is tuple, 3.0
     assert type(testMatchEngineResult) is tuple
     
def test_matching_returns_best_question_object():
     matching = Matching("What are the weathers like todays")
     testMatchEngineResult = matching.match()
     #assert testMatchEngineResultFull == (isinstance(testMatchEngineResultFull[1], float) , 1.0 )
     assert isinstance(testMatchEngineResult[0], BestQuestion) 
     
def test_matching_returns_float_as_score():
     matching = Matching("What are the weathers like todays")
     testMatchEngineResult = matching.match()
     #assert testMatchEngineResultFull == (isinstance(testMatchEngineResultFull[1], float) , 1.0 )
     assert type(testMatchEngineResult[1]) is float
    
def test_jaccard():
    testSanitisedUserQuestionString1 = "did it be snowing yesterday"
    testSanitisedUserQuestionString2 = "will it be raining today"
    testSanitisedStoreQuestionString = "did it snow yesterday"
    
    testScore1 = jaccard_similarity_score(testSanitisedUserQuestionString1, testSanitisedStoreQuestionString)
    testScore2 = jaccard_similarity_score(testSanitisedUserQuestionString2, testSanitisedStoreQuestionString)
    
    assert testScore1 > testScore2
    
def test_manager_calls_with_argument():
    testObject = Mock()
    manager = QuestionAnsweringManager()
    manager.answer_question('how are you')
    assert testObject.answer_question.called_once_with('how are you')
    
    
def test_answer_question_result():
    manager = QuestionAnsweringManager()
    testResult = manager.answer_question('Was it snowing yesterday')
    assert testResult[0].question == 'Did it snow yesterday?' and testResult[0].answer == 'No.'

#check overall matching 
#test manager
#refactor above to use fixtures
#mock objects
#boundary issues


#class StoreAccess:
#    def __init__(self, filePath):
#        self.filePath = filePath
        
#    def openJson(self):
#        with open(self.filePath) as file:
#            data = json.load(file)
#        return data
        
    

#test_open_and_store_txt_file('test-directory')

#def test_open_and_store_txt_file():
#    open_mock = mock_open()
#    with patch("question_log_access.open", open_mock, create=True):
#        LogAccess.openAndStoreTxtFile("test-data")

#    open_mock.assert_called_with("asked_questions_log.txt", "a")
#    open_mock.return_value.write.assert_called_once_with("test-data")
    

#test_open_and_store_txt_file(manager)
    

#def test_manager_candidate_result():
    
#openAndStoreTxtFile(self, filePath, question)

# def openAndStoreTxtFile(self, filePath, question):
#        with open(filePath, 'a') as file:
#            file.write(question)
 #           file.write('\n')