class management:
    company="codersnest"
    valid_ids = [74341, 74342, 74343]

    def __init__(self,emp_name,emp_id,emp_pos):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_pos=emp_pos

    def details(self):
        entered_id = int(input("Enter employee id: "))

        if entered_id in management.valid_ids:
            print(f"Company name: {self.company}")
            print(f"Employee name: {self.emp_name}")
            print(f"Employee id: {entered_id}")
            print(f"Employee Position: {self.emp_pos}")
            print()
        else:
            print("Invalid details")
            print()


s1=management("shaik umar",74341,"trainer")
s2=management("Manar",74342,"trainer")
s3=management("shahid",74343,"trainer")
result=[s1,s2,s3]
for people in result:
    people.details()

