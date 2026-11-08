class Student:
    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age


    def __eq__(self, rhs):
        if not isinstance(rhs, Student):    # to make sure it doesn't try to check if a student is equal to a clown
            return False                    # well if it does it returns false 
        return self.ssn == rhs.ssn

    def __ne__(self,rhs):
        if not isinstance(rhs,Student):
            return False
        return self.ssn != rhs.ssn
    
    def __gt__(self,rhs):
        if not isinstance(rhs,Student):
            return False
        return self.ssn > rhs.ssn
    
    def __lt__(self,rhs):
        if not isinstance(rhs,Student):
            return False
        return self.ssn < rhs.ssn
    
    def __ge__(self,rhs):
        if not isinstance(rhs, Student):
            return False
        return self.ssn >= rhs.ssn
    
    def __le__(self,rhs):
        if not isinstance(rhs, Student):
            return False
        return self.ssn <= rhs.ssn
    
    def __hash__(self):
        cleaned_ssn = self.ssn.replace('-', '')
        if cleaned_ssn == "":
            return 0
        return int(cleaned_ssn)
    