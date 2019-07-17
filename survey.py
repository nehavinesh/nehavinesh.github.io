import json
def main():

    data_list = []
    again = True

    while again == True:
        name = input("What's your name?\n ")
        age = input("What's your age?\n ")
        food = input("What's your favorite food?\n ")
        book = input("What's your favorit book?\n ")
        answers = {"Name":name, "Age":age, "Food":food,"book":book}
        data_list.append(answers)
        answer = True

        while answer == True:
            collection = input("Would you like to add more answers? (yes/no)\n ")
            if collection == "yes":
                again = True
                answer = False
            elif collection == "no":
                answer = False
                again = False
            else:
                answer = True

        output_file = open('survery.json','w', encoding = 'utf-8')
        for dic in data_list:
            json.dump(dic, output_file)
            output_file.write("\n")

        with open('survey.json', 'w') as json_file:
            json.dump(data_list, json_file)

    print(data_list)


if __name__ == "__main__":
    main()
