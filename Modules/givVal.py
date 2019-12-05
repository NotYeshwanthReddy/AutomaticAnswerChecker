import math
import re

import nav_test
import pyrebase
import requests
from fuzzywuzzy import fuzz

import cosine_similarity as keywordVal
# import configurations
config = {
       
  'apiKey': "AIzaSyACAssH2w9e7NJp-vULkwNbIFngGokKNt8",
  'authDomain': "test-63d5a.firebaseapp.com",
  'databaseURL': "https://test-63d5a.firebaseio.com/",
  'projectId': "test-63d5a",
  'storageBucket': "test-63d5a.appspot.com",
  'messagingSenderId': "665581966414",

}


def givVal(model_answer, keywords, answer, out_of):
    # for keywords
    if (len(answer.split())) <= 5 :
        return 0
        
    k = keywordVal.givKeywordsValue(model_answer, answer)


    # for Grammer

    req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=JmcxHCCPZ7jfXLF6")
    no_of_errors = len(req.json()['errors'])

    if no_of_errors > 5 or k == 6:
        g = 0
    else:
        g = 1

    # for Question Specific Tag

    q = math.ceil(fuzz.token_set_ratio(model_answer, answer) * 6 / 100)

    print("Keywords : ", k)
    print("Grammar  : ", g)
    print("QST      : ", q)

    predicted = nav_test.predict(k, g, q)

    result = predicted * out_of / 10
    return result[0]

# firebsevar = pyrebase.initialize_app(config=configurations.config)
firebsevar = pyrebase.initialize_app(config)
db = firebsevar.database()

model_answer1 = db.child("model_answers").get().val()[1]['answer']
out_of1 = db.child("model_answers").get().val()[1]['out_of']
keywords1 = db.child("model_answers").get().val()[1]['keywords']
keywords1 = re.findall(r"[a-zA-Z]+", keywords1)

model_answer2 = db.child("model_answers").get().val()[2]['answer']
out_of2 = db.child("model_answers").get().val()[2]['out_of']
keywords2 = db.child("model_answers").get().val()[2]['keywords']
keywords2 = re.findall(r"[a-zA-Z]+", keywords2)

model_answer3 = db.child("model_answers").get().val()[3]['answer']
out_of3 = db.child("model_answers").get().val()[3]['out_of']
keywords3 = db.child("model_answers").get().val()[3]['keywords']
keywords3 = re.findall(r"[a-zA-Z]+", keywords3)

all_answers = db.child("answers").get()

for each_users_answers in all_answers.each():
    # 1st
    print("\n\n" + each_users_answers.val()['email'])

    answer = each_users_answers.val()['a1']
    result = givVal(model_answer1, keywords1, answer, out_of1)
    print("Marks : " + str(result))
    db.child("answers").child(each_users_answers.key()).update({"result1": result})

    # 2nd
    answer = each_users_answers.val()['a2']
    result = givVal(model_answer2, keywords2, answer, out_of2)
    print("Marks : " + str(result))
    db.child("answers").child(each_users_answers.key()).update({"result2": result})

    # 3rd
    answer = each_users_answers.val()['a3']
    result = givVal(model_answer3, keywords3, answer, out_of3)
    print("Marks : " + str(result))
    db.child("answers").child(each_users_answers.key()).update({"result3": result})