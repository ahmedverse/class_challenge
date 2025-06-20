from datetime import datetime

class FriendsRecord:
    # User-facing properties:
    #   records = empty list

    def __init__(self):
        
        self.records = []
        
    def add_friend(self, name, birthdate):

        self.records.append({"name":name, "birthdate":birthdate})

    def ammend_birthdate(self, name, new_date):
        
        for i in self.records:
            if i["name"] == name:
                i["birthdate"] = new_date

    def ammend_name(self, name, new_name):
        
        for i in self.records:
            if i["name"] == name:
                i["name"] = new_name

    def check_earliest_birthdate(self):

        for record in self.records:
            record["birthdate_dt"] = datetime.strptime(record["birthdate"], "%d/%m/%Y") 
        
        earliest = min(self.records, key=lambda x: x["birthdate_dt"])

        return earliest['name']


    def calculate_age(self, name):
        # Returns:
        #  returns the age of the name given
        # Side-effects
        #  none
        pass