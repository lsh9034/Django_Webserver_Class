from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm): #어떤 형식의 form으로 화면을 뿌릴지 전체적인 뼈대를 정의
    class Meta:
        model = Question
        fields = ['subject', 'content']  #question 테이블의 속성이 정의된거임.
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }