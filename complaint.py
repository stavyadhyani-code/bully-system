class Complaint:
    def __init__(self, victim_name, bully_name, description, severity):
        self.victim_name = victim_name
        self.bully_name = bully_name
        self.description = description
        self.severity = severity
        self.next = None

    def __repr__(self):
        return f"[Victim: {self.victim_name}, Bully: {self.bully_name}, Severity: {self.severity}]"

class ComplaintList:
    def __init__(self):
        self.head = None

    def add_complaint(self, victim_name, bully_name, description, severity):
        new_complaint = Complaint(victim_name, bully_name, description, severity)
        if not self.head:
            self.head = new_complaint
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_complaint

    def display_complaints(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next
