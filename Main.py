import Student
import Hash_Bag
import time


def main():
    Bag = Hash_Bag.Bag()
    
    start_time = time.perf_counter()
    with open("FakeNames.txt", 'r') as file:
        for line in file:
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(Bag.Insert(new_student) == False):
                print(f"Error duplicate student {new_student.first} {new_student.last}")
    finish_time = time.perf_counter()

    elapsed = finish_time - start_time
    print(f"Insert time: {elapsed}")
    print(f"Size after insert: {Bag.Size()}")

    total_age = 0
    start_time = time.perf_counter()

    for x in Bag:
        total_age += int(x.age)

    finish_time = time.perf_counter()

    average = total_age / Bag.Size()
    elapsed = finish_time - start_time
    print(f"Iterate time: {elapsed}")
    print(f"Average age: {average}")



    start_time = time.perf_counter()
    with open("DeleteNames.txt", 'r') as file:
        for line in file:
            ssn = line.strip()
            # print(ssn)
            temp = Student.Student("", "", ssn, "", "")
            if(Bag.Delete(temp) == False):
                print(f"Error no item found to delete {temp.ssn}")

    finished_time = time.perf_counter()
    elapsed = finished_time - start_time
    print(f"Delete time: {elapsed}")
    print(f"Size after delete: {Bag.Size()}")

    total_age = 0
    count = 0 

    start_time = time.perf_counter()
    with open("RetrieveNames.txt", 'r')as file:
            for line in file:
                ssn = line.strip()
                # print(ssn)
                temp = Student.Student("", "", ssn, "", "")

                found = Bag.Retrive(temp)

                if(found == None):
                    print(f"Error no item found {temp.ssn}")
                else:
                    total_age += int(found.age)
                    count += 1
    finished_time = time.perf_counter()

    average = total_age / count
    elapsed = finished_time - start_time

    print(f"Average age of retrieved: {average}")
    print(f"Retrieve time: {elapsed}")
    print(f"Size after Retrieve {Bag.Size()}")
         
main()