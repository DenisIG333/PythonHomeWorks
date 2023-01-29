# list_subject = []
def input_class():
    return input("С каким классом работаем? ").upper()

def input_subject():
    return input("Какой предмет? ").lower()

def who_answer():
    return input("Кто будет отвечать? ")

def what_mark():
    return input("На какую оценку ответил(а)? ")

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f"{i}. {child:20} {journal.get(child)}")

