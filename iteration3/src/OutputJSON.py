import Student
import json
class OutputJSON:
    def saveStudent(student:Student):
        str = json.dumps(student.__dict__)
        print(str)