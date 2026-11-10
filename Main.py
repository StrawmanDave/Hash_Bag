import Student
import Hash_Bag
import time

def Main():
    smallBag = Hash_Bag.Bag()

    print("Small        Times   Success   Failures    Average Age")
    start_insert = time.perf_counter()
    insert_success = 0
    insert_error = 0
    with open("FakeNames.txt", 'r') as file:
        for line in file:
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(smallBag.Insert(new_student) == False):
                insert_error += 1
            else:
                insert_success += 1
    finish_insert = time.perf_counter()

    small_insert_time =  finish_insert - start_insert
    print(f"Insert      {small_insert_time:.6f}   {insert_success}    {insert_error}")

    total_age = 0
    start_iter = time.perf_counter()
    for x in smallBag:
        total_age += int(x.age)
    finish_iter = time.perf_counter()
    small_iter_time = finish_iter - start_iter 
    average = total_age / smallBag.Size()
    print(f"Traverse    {small_iter_time:.6f}                     {average:.6f}")

    start_del = time.perf_counter()
    delete_success = 0
    delete_error = 0
    with open("DeleteNames.txt", 'r') as file:
        for line in file:
            ssn = line.strip()
            # print(ssn)
            temp = Student.Student("", "", ssn, "", "")
            if(smallBag.Delete(temp) == False):
                delete_error += 1
            else:
                delete_success += 1
    finish_del = time.perf_counter()
    small_delete_time = finish_del - start_del
    print(f"Delete      {small_delete_time:.6f}    {delete_success}    {delete_error}")

    retr_start = time.perf_counter()
    retr_error = 0
    retr_success = 0
    retrive_age = 0
    with open("RetrieveNames.txt", 'r')as file:
        for line in file:
            ssn = line.strip()
            # print(ssn)
            temp = Student.Student("", "", ssn, "", "")

            found = smallBag.Retrive(temp)

            if(found == None):
                retr_error += 1
            else:
                retr_success += 1
                retrive_age += int(found.age)
    retr_average = retrive_age / retr_success
    retr_finish = time.perf_counter()
    retr_time = retr_finish - retr_start
    print(f"Retrive     {retr_time:.6f}   {retr_success}    {retr_error}        {retr_average:.6f}")

    print()
    mediumBag = Hash_Bag.Bag()
    print("Medium        Times   Success   Failures    Average Age")
    start_insert = time.perf_counter()
    insert_success = 0
    insert_error = 0
    with open("FakeNamesMedium.txt", 'r') as file:
        for line in file:
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(mediumBag.Insert(new_student) == False):
                insert_error += 1
            else:
                insert_success += 1
    finish_insert = time.perf_counter()

    insert_time =  finish_insert - start_insert
    print(f"Insert      {insert_time:.6f}   {insert_success}    {insert_error}")

    total_age = 0
    start_iter = time.perf_counter()
    for x in mediumBag:
        total_age += int(x.age)
    finish_iter = time.perf_counter()
    iter_time = finish_iter - start_iter 
    average = total_age / mediumBag.Size()
    print(f"Traverse    {iter_time:.6f}                     {average:.6f}")

    start_del = time.perf_counter()
    delete_success = 0
    delete_error = 0
    with open("DeleteNamesMedium.txt", 'r') as file:
        for line in file:
            ssn = line.strip()
            # print(ssn)
            temp = Student.Student("", "", ssn, "", "")
            if(mediumBag.Delete(temp) == False):
                delete_error += 1
            else:
                delete_success += 1
    finish_del = time.perf_counter()
    small_delete_time = finish_del - start_del
    print(f"Delete      {small_delete_time:.6f}    {delete_success}    {delete_error}")

    retr_start = time.perf_counter()
    retr_error = 0
    retr_success = 0
    retrive_age = 0
    with open("RetrieveNamesMedium.txt", 'r')as file:
        for line in file:
            ssn = line.strip()
            temp = Student.Student("", "", ssn, "", "")

            found = mediumBag.Retrive(temp)

            if(found == None):
                retr_error += 1
            else:
                retr_success += 1
                retrive_age += int(found.age)
    retr_average = retrive_age / retr_success
    retr_finish = time.perf_counter()
    retr_time = retr_finish - retr_start
    print(f"Retrive     {retr_time:.6f}   {retr_success}    {retr_error}        {retr_average:.6f}")

Main()