# THINGS TO ACHIEVE
# show the correct answer if wrong
# add a try again menu-done
# error for number range and letter-done
# add a message for 0 answers right

import requests
import random
from time import sleep
import html

print("Welcome to Rolling Through Time")

print(" ")

user_name = input("What is your name:")

sleep(1)
print(f"Welcome {user_name.title()}. How well do you know your Board Games")
print("")
print("*********************************************")
print("")
print("To answer you have to pick a number from 1-4")
print("Press any key to continue")
enter = input("")
print("")
print("*********************************************")
print("*********************************************")
print("")
parameters = {
    "amount": 5,
    "type": "multiple",
    "category": 16,
    # "difficulty": "easy",
}
while True:
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()["results"]
    answer_list = [] # to store both correct and incorrect answer
    right = 5
    wrong = 0
    for i in question_data:
        sleep(0.01)
        if i == question_data[0]:
            print(html.unescape(i['question']))
            answer = (html.unescape(i["correct_answer"]))
            answer_list.append(answer)
            for n in html.unescape(i["incorrect_answers"]):
                answer_list.append(n)
            random1 = random.sample(answer_list, 4)
            for (i, option) in enumerate(random1):
                print(f"{i + 1}){option}")
            while True:
                try:
                    print("")
                    user_ans = int(input("Pick a number:"))
                    print("")
                    if user_ans > 0 and user_ans < 5:
                        if random1[user_ans - 1] == answer_list[0]:
                            print("Aren't you a smarty-pants!")
                            break
                        else:
                            print("A five year old could do better!")
                            print(f"The correct answer is {answer}")
                            wrong += 1
                            right -= 1
                            break
                    else:
                        print("Choose from 1-4")
                except:
                    print("It has to be a number")

            print("-----------------------------------------------------")
            answer_list = []
        elif i == question_data[1]:
            print(html.unescape(i['question']))
            answer = (html.unescape(i["correct_answer"]))
            answer_list.append(answer)
            for n in html.unescape(i["incorrect_answers"]):
                answer_list.append(n)
            random2 = random.sample(answer_list, 4)
            for (i, option) in enumerate(random2):
                print(f"{i + 1}){option}")

            while True:
                try:
                    print("")
                    user_ans = int(input("Pick a number:"))
                    print("")
                    if user_ans > 0 and user_ans < 5:
                        if random2[user_ans - 1] == answer_list[0]:
                            print("Bravo, You're killing it!")
                            break
                        else:
                            print("Wrong!, You might want to consider going back to third-grade")
                            print(f"The correct answer is {answer}")
                            wrong += 1
                            right -= 1
                            break
                            # print((i["correct_answer"])+"is the correct answer")

                    else:
                        print("Choose from 1-4")
                except:
                    print("It has to be a number")

            print("-----------------------------------------------------")
            answer_list = []
        elif i == question_data[2]:
            print(html.unescape(i['question']))
            answer = (html.unescape(i["correct_answer"]))
            answer_list.append(answer)
            for n in html.unescape(i["incorrect_answers"]):
                answer_list.append(n)
            random3 = random.sample(answer_list, 4)
            for (i, option) in enumerate(random3):
                print(f"{i + 1}){option}")

            while True:
                try:
                    print("")
                    user_ans = int(input("Pick a number:"))
                    print("")
                    if user_ans > 0 and user_ans < 5:
                        if random3[user_ans - 1] == answer_list[0]:
                            print("Some People are born geniuses!")
                            break
                        else:
                            print("Incorrect,Do you need some coffee")
                            print(f"The correct answer is {answer}")
                            # print("The correct answer is:", (i["correct_answer"]))
                            wrong += 1
                            right -= 1
                            break
                    else:
                        print("Choose from 1-4")
                except:
                    print("It has to be a Number")

            print("-----------------------------------------------------")
            answer_list = []
        elif i == question_data[3]:
            print(html.unescape(i['question']))
            answer = (html.unescape(i["correct_answer"]))
            answer_list.append(answer)
            for n in html.unescape(i["incorrect_answers"]):
                answer_list.append(n)
            random4 = random.sample(answer_list, 4)
            for (i, option) in enumerate(random4):
                print(f"{i + 1}){option}")

            while True:
                try:
                    print("")
                    user_ans = int(input("Pick a number:"))
                    print("")
                    if user_ans > 0 and user_ans < 5:
                        if random4[user_ans - 1] == answer_list[0]:
                            print("Mind-Blown!")
                            break
                        else:
                            print("Incorrect, You might want to hit the text-books again!")
                            print(f"The correct answer is {answer}")
                            wrong += 1
                            right -= 1
                            break
                    else:
                        print("Choose from 1-4")
                except:
                    print("It has to be a number")

            print("-----------------------------------------------------")
            answer_list = []
        elif i == question_data[4]:
            print(html.unescape(i['question']))
            answer = (html.unescape(i["correct_answer"]))
            answer_list.append(answer)
            for n in html.unescape(i["incorrect_answers"]):
                answer_list.append(n)
            random5 = random.sample(answer_list, 4)
            for (i, option) in enumerate(random5):
                print(f"{i + 1}){option}")
            while True:
                try:
                    print("")
                    user_ans = int(input("Pick a number:"))
                    print("")
                    if user_ans > 0 and user_ans < 5:
                        if random5[user_ans - 1] == answer_list[0]:
                            print("Mr sponge-bob SMART-PANTS!!")
                            break
                        else:
                            print("Nuh-uh, All play and no work makes Jack a dull boy")
                            print(f"The correct answer is {answer}")
                            # print("The correct answer is:", (i["correct_answer"]))
                            wrong += 1
                            right -= 1
                            break
                    else:
                        print("Choose from 1-4")
                except:
                    print("It has to be a number")
            print("-----------------------------------------------------")
        else:
            break
    print(" ")
    # special message for extreme right or wrong
    if right >= 4:
        print("Looks like we got an Einstein in the house")
        print(" ")
        print(f"You got {right} answers right and {wrong} answers wrong")
    elif right == 0 or right == 1:
        print("Do you live in a hole?")
        print(" ")
        print(f"You got {right} answers right and {wrong} answers wrong")
    else:
        print(" ")
        print(f"You got {right} answers right and {wrong} answers wrong")
        print("Do better next-time")

    print("")

    enter = str(input("Do you want to try again (Y/N):"))
    if enter.upper() == "Y":
        print("")
        print("")
        print("")
        print("")

        continue
    else:
        print(" ")
        print(f"Thank you for playing,{user_name.title()} see you soon")
        break
