from .models import Test
from .models import Question
from .models import Answer
from .models import AnswerWeight
from .models import CombinedTest
from .models import CombinedTestQuestion

tests = [
    Test(test_name="Опросник Смирнова", question_count=5, characteristics="Тип мышления, Общительность"),
    Test(test_name="Тест на модальность", question_count=5, characteristics="Тип мышления, Уверенность в себе"),
    Test(test_name="Тест на доброжелательность", question_count=5, characteristics="Доброжелательность, Общительность"),
]

Test.objects.bulk_create(tests)



questions = [
    Question(test=tests[0], question_text="Как часто вы принимаете решения, основываясь на логике, а не эмоциях?"),
    Question(test=tests[0], question_text="Предпочитаете ли вы структурированные планы или спонтанные решения?"),
    
    Question(test=tests[1], question_text="Вы быстрее запоминаете информацию на слух или в виде текста?"),
    Question(test=tests[1], question_text="В сложной ситуации вы действуете уверенно или сомневаетесь в себе?"),

    Question(test=tests[2], question_text="Легко ли вы находите общий язык с новыми людьми?"),
    Question(test=tests[2], question_text="Считаете ли вы себя доброжелательным человеком?"),
]

Question.objects.bulk_create(questions)


answers = [
    Answer(question=questions[0], answer_text="Всегда"),
    Answer(question=questions[0], answer_text="Часто"),
    Answer(question=questions[0], answer_text="Редко"),

    Answer(question=questions[1], answer_text="Структурированные планы"),
    Answer(question=questions[1], answer_text="Спонтанные решения"),

    Answer(question=questions[2], answer_text="На слух"),
    Answer(question=questions[2], answer_text="В виде текста"),
    
    Answer(question=questions[3], answer_text="Всегда уверен"),
    Answer(question=questions[3], answer_text="Иногда сомневаюсь"),

    Answer(question=questions[4], answer_text="Да, очень легко"),
    Answer(question=questions[4], answer_text="Иногда трудно"),

    Answer(question=questions[5], answer_text="Да"),
    Answer(question=questions[5], answer_text="Нет"),
]

Answer.objects.bulk_create(answers)


answer_weights = [
    AnswerWeight(question=questions[0], trait="Тип мышления", weight=2),
    AnswerWeight(question=questions[0], trait="Общительность", weight=1),

    AnswerWeight(question=questions[1], trait="Тип мышления", weight=3),

    AnswerWeight(question=questions[2], trait="Тип мышления", weight=2),

    AnswerWeight(question=questions[3], trait="Уверенность в себе", weight=3),

    AnswerWeight(question=questions[4], trait="Общительность", weight=2),

    AnswerWeight(question=questions[5], trait="Доброжелательность", weight=3),
]

AnswerWeight.objects.bulk_create(answer_weights)


combined_tests = [
    CombinedTest(combined_test_name="Общий психологический тест", characteristics="Тип мышления, Общительность, Доброжелательность, Уверенность в себе"),
]

CombinedTest.objects.bulk_create(combined_tests)



combined_test_questions = [
    CombinedTestQuestion(combined_test=combined_tests[0], original_test=tests[0], question=questions[0]),
    CombinedTestQuestion(combined_test=combined_tests[0], original_test=tests[1], question=questions[3]),
    CombinedTestQuestion(combined_test=combined_tests[0], original_test=tests[2], question=questions[5]),
]

CombinedTestQuestion.objects.bulk_create(combined_test_questions)
