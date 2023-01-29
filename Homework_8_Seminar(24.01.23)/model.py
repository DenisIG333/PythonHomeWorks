from os import walk
journal = {}
subject = ""
path = ""
find_count = 0
list_classes = []
list_subject = []


def list_class():
    class_list = []
    for (dirpath, dirnames, filenames) in walk("Classes"):
        class_list.extend(filenames)
    return class_list

def set_class(class_path: str):
    global path
    path = "Classes/" + class_path + ".txt"

def set_subject(our_subject: str):
    global subject
    subject = our_subject

def open_file():
    global find_count
    global isExept
    try:
        with open(path, "r", encoding="UTF-8") as data:
            file = data.readlines()

        for sub in file:
            list_subject.append(sub.split(";")[0])
            if sub.split(";")[0] == subject:
                find_count += 1
                for study in sub.split(";")[1].strip().split(", "):
                    journal[study.split(":")[0]] = list(map(int, study.split(":")[1].split()))
    except:
        isExept = True




def save_file():
    new_file = []
    with open(path, "r", encoding="UTF-8") as data:
        file = data.readlines()
    for sub in file:
        if sub.split(";")[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ":" + " ".join(list(map(str, marks))))
    item = subject + ";" + ", ".join(item)
    new_file.append(item)
    with open(path, "w", encoding="UTF-8") as data:
        data.write("\n".join(new_file))


def student_mark(student: str, mark: int):
    marks = list(journal.get(student))

    marks.append(mark)
    journal[student] = marks



def get_journal():
    return journal

def list_0f_subjects():
    with open(path, "r", encoding="UTF-8") as data:
        file = data.readlines()
        list_subject.clear()
        for sub in file:
            list_subject.append(sub.split(";")[0])
        print(f"список предметов - {list_subject}")
        list_subject.clear()



