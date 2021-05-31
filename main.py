from interactive_console_client import InteractiveConsoleClient
from question_answering_manager import QuestionAnsweringManager


def main(candidates_path, questions_log_path):
    #TODO your initialization code goes here, replacing the `manager = None` statement
    #
    manager = QuestionAnsweringManager()
    #
    client = InteractiveConsoleClient(manager)
    client.run()


if __name__ == '__main__':
    main("faq.json", "asked_questions_log.txt")
    
