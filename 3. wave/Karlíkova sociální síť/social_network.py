from abc import ABC

class Animal(ABC):
    def __init__(self, name, university_num):
        self.name = name
        self.university_num = university_num

    def __repr__(self):
        return f'Ahoj, já jsem {self.name}!'
    

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.university_num == other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")
        

    def __ne__(self, other):
        if isinstance(other, Animal):
            return self.university_num != other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")


    def __lt__(self, other):
        if isinstance(other, Animal):
            return self.university_num < other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")


    def __le__(self, other):
        if isinstance(other, Animal):
            return self.university_num <= other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")
        


    def __gt__(self, other):
        if isinstance(other, Animal):
            return self.university_num > other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")
        


    def __ge__(self, other):
        if isinstance(other, Animal):
            return self.university_num >= other.university_num

        else:
            raise Exception("Can't compare with other type than Animal")





class Student(Animal):
    def __init__(self, name, university_num):
        super().__init__(name, university_num)

        if not (100000 <= self.university_num <= 700000):
            raise ValueError("Error, id should be in the range 100 000 - 700 000.")
        

class AkademickyPracovnik(Animal):
    def __init__(self, name, university_num):
        super().__init__(name, university_num)

        if not (700001 <= self.university_num <= 999999):
            raise ValueError("Error, id should be in the range 700 001 - 999 999.")
        


## !!!!!!!!!! HOST CAN BE FRIENDS ONLY WITH ACADEMIC WORKERS !!!!!!!!!!! ##
class Host(Animal):
    def __init__(self, name, university_num):
        super().__init__(name, university_num)

        if not (self.university_num > 1000000):
            raise ValueError("Error, id should be in greater than 1 000 000.")
        






def test_university_users():
    print("Starting tests...")
    
    # Test Student creation
    try:
        student = Student("Petr", 150000)
        print(student)  # Should print "Ahoj, já jsem Petr!"
    except ValueError as e:
        print("Failed to create valid Student:", e)
    
    # Test invalid Student creation
    try:
        invalid_student = Student("Jan", 666)  # Should raise ValueError
        print("Error: Created invalid student!")
    except ValueError:
        print("Correctly caught invalid student ID.")
    
    # Test Academic Worker creation
    try:
        academic = AkademickyPracovnik("Dr. Novák", 800000)
        print(academic)  # Should print "Ahoj, já jsem Dr. Novák!"
    except ValueError as e:
        print("Failed to create valid Academic Worker:", e)
    
    # Test invalid Academic Worker creation
    try:
        invalid_academic = AkademickyPracovnik("Dr. Chybný", 500000)  # Should raise ValueError
        print("Error: Created invalid academic worker!")
    except ValueError:
        print("Correctly caught invalid academic worker ID.")
    
    # Test Host creation
    try:
        host = Host("Visiting Researcher", 1000001)
        print(host)  # Should print "Ahoj, já jsem Visiting Researcher!"
    except ValueError as e:
        print("Failed to create valid Host:", e)
    
    # Test invalid Host creation
    try:
        invalid_host = Host("Invalid Host", 999999)  # Should raise ValueError
        print("Error: Created invalid host!")
    except ValueError:
        print("Correctly caught invalid host ID.")
    
    # Test comparisons
    try:
        assert student < academic, "Comparison failed: student should be less than academic."
        assert academic > student, "Comparison failed: academic should be greater than student."
        assert student != academic, "Comparison failed: student and academic should not be equal."
        assert student == Student("Another Student", 150000), "Comparison failed: students with same ID should be equal."
        assert academic >= student, "Comparison failed: academic should be greater or equal to student."
        assert student <= academic, "Comparison failed: student should be less or equal to academic."
        print("All comparisons passed!")
    except AssertionError as e:
        print("Comparison test failed:", e)
    
    print("All tests completed.")

# Run the tests
test_university_users()
