from app.services import *
from app.models import Question

def get_question_by_index(index):
    obj = Question.objects.get(index=index)
    return obj

def check_question_availability_by_index(index):
    if Question.objects.filter(index=index):
        return True
    else:
        return False