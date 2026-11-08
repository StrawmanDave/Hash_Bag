import Hash_Bag
import Student
from itertools import islice

def Test1():    # test all of Inserts case
    small_bag = Hash_Bag.Bag()
    # get the first 10 line sout of the fakenames file and Insert them
    with open("FakeNames.txt", 'r') as file:
        for line in islice(file, 10):
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            inserted_index = small_bag.Insert(new_student);

            if(inserted_index == False):
                print(f"Error duplicate insert of {new_student.first} {new_student.last}")
            else:
                saved_student = small_bag.table[inserted_index]
                print(f"Successfully inserted: {saved_student.first} {saved_student.last}")

    print(small_bag.Insert(Student.Student("GREGORY", "DON", "574-28-3634", "", "")))   # test if it sees a dupilcate

Test1()

def Test2():    # test all of Exists cases
    small_bag = Hash_Bag.Bag(10)
    with open("FakeNames.txt", 'r') as file:

        for line in islice(file, 10):
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])

            if(small_bag.Insert(new_student) == False):
                print(f"Error duplicate insert of {new_student.first} {new_student.last}")
            # else:
            #   print(f"{small_bag.first.item.first} {small_bag.first.item.last}")

    print( small_bag.Exists(Student.Student("", "", "574-28-3634", "", "")) )       # one that does exists
    print( small_bag.Exists(Student.Student("", "", "", "", "")) )        # one that does not

# Test2()

def Test3():    # Test Size
    small_bag = Hash_Bag.Bag(10)
    print(small_bag.Size())
    with open("FakeNames.txt", 'r') as file:
        for line in islice(file, 10):
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(small_bag.Insert(new_student) == False):
                print(f"Error duplicate insert of {new_student.first} {new_student.last}")
            # else:
            #   print(f"{small_bag.first.item.first} {small_bag.first.item.last}")

    print(small_bag.Size())

# Test3()

def Test4():     # Test iterate
    small_bag = Hash_Bag.Bag(10)
    for x in small_bag:
        print(x.first, x.last)

    with open("FakeNames.txt", 'r') as file:
        for line in islice(file, 10):
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(small_bag.Insert(new_student) == False):
                print(f"Error duplicate insert of {new_student.first} {new_student.last}")
            # else:
            #   print(f"{small_bag.first.item.first} {small_bag.first.item.last}")
    
    for x in small_bag:
        print(x.first, x.last)     # this prints them backwards is that intended or not?

# Test4()

def Test5():    #Test Delete
    small_bag = Hash_Bag.Bag(10)
    print(small_bag.Delete(Student.Student("","","451-30-3555", "","")))    # test with empty list

    with open("FakeNames.txt", 'r') as file:
        for line in islice(file, 10):
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(small_bag.Insert(new_student) == False):
                print(f"Error duplicate insert of {new_student.first} {new_student.last}")
            # else:
            #   print(f"{small_bag.first.item.first} {small_bag.first.item.last}"))
    print(small_bag.Delete(Student.Student("","","451-30-1234","","")))     # test if the item does not exist

    print(small_bag.Delete(Student.Student("","","463-89-5218","","")))     # deleting ACEVEDO WILLIE the first item in the list
    print(small_bag.Size())                                                 # should return true and there the size should be 9 

    print(small_bag.Delete(Student.Student("","","451-30-3555","","")))     # delete BUSH JUSTIN some item in the middle
    print(small_bag.Size())                                                 # should return size 8

# Test5()

def Test6():    #Test Retrive
    small_bag = Hash_Bag.Bag(10)
    student_retrieve = Student.Student("","","463-89-5218","","")
    print(small_bag.Retrive(student_retrieve), small_bag.Retrive(student_retrieve))  # test on an empty list

    with open("FakeNames.txt", 'r') as file:
        for line in islice(file, 10):
            words = line.split(" ")
            new_student = Student.Student(words[0], words[1], words[2], words[3], words[4])
            if(small_bag.Insert(new_student) == False):
                print(f"Error duplicate insert of {new_student.first} {new_student.last}")
            # else:
            #   print(f"{small_bag.first.item.first} {small_bag.first.item.last}"))

    student_retrieve = Student.Student("","","463-89-1243","","")
    print(small_bag.Retrive(student_retrieve), small_bag.Retrive(student_retrieve))  # test on when the item is just not there

    student_retrieve = Student.Student("","","463-89-5218","","")
    print(small_bag.Retrive(student_retrieve).first, small_bag.Retrive(student_retrieve).last) # test on when the item is there

Test6()