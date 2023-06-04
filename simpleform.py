questions = ["Date: ", "Name: ",'Address: ',"Problem: ", "Password:", "Install any Software or Hardware?",  ]
list_of_responses = []
def ask_question():
    qna = []
    for qs in questions:
        print(qs)
        qna.append(input())
    list_of_responses.append(qna)

for i in range(4):
    ask_question()
import pandas as pd
pd.DataFrame(list_of_responses, columns=questions)
df = pd.DataFrame(list_of_responses, columns=questions)
print(df)

