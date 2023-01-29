import model
import view
import re


def start():
    is_input_class = False

    while True:
        classes = model.list_class()
        for i in range(len(classes)):
            classes[i] = re.sub('.txt', '', classes[i])
        print(f"список классов - {classes}")
        model.set_class(view.input_class())
        # classes = model.list_class()
        # print(classes)

        for i in range(len(classes)):
            if classes[i] in model.path:
                is_input_class = True
        if is_input_class == True:
            break
        else:
            print("класс не найден, повторите ввод")

    while True:
        model.list_0f_subjects()
        model.set_subject(view.input_subject())
        model.open_file()
        if model.find_count > 0:
            break
        else:
            print("предмет не найден, повторите ввод")

    student = ""

    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()

        if journal.get(student) == None:
            print("Ученик не найден, введите правильные фамилию и имя")

        else:
            break

    while True:
        try:
            mark = int(view.what_mark())

            if mark >= 1 and mark <= 5:
                model.student_mark(student, mark)
                model.save_file()
                break
            print("Некорректный ввод. Введите оценку от 1 до 5 баллов")
        except:
            print("Вы ввели не цифру. Введите оценку от 1 до 5 баллов")
