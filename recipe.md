# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

<!-- # As a user
# So I don't forget the details
# I want to keep a record of friends' names and birthdates

# As a user
# So I can make edits when I've got dates wrong
# I want to be able to update a record by passing in a name and new date

# As a user
# So I can make edits when people change their name
# I want to be able to update a record by passing in an old and a new name

# As a user
# So I can remember to send birthday cards at the right time
# I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

# As a user
# So I can buy age-appropriate birthday cards
# I want to calculate the upcoming ages for friends with birthdays -->


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class FriendsRecord:
    # User-facing properties:
    #   records = empty list

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #  create empty list to store our friends records
        pass # No code here yet

    def add_friend(self, name, birthdate):
        # Parameters:
        #   date = birthdate 
        #   name = name 
        # Returns:
        #   Nothing
        # Side-effects
        #   adds the name and thier birthdate on the records
        pass # No code here yet

    def ammend_birthdate(self, name, new_date):
        # Parameters:
        #   new date = new_date 
        #   name = name 
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the birthdate on the records
        pass # No code here yet

    def ammend_name(self, name, new_name):
        # Parameters:
        #   new name = new_name
        #   name = name 
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the name on the records
        pass # No code here yet

    def check_earliest_birthdate(self):
        # Returns:
        #   Name of the person with the earliest birthdate
        # Side-effects
        #  none

   def calculate_age(self, name):
        # Returns:
        #  returns the age of the name given
        # Side-effects
        #  none
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given an friend record class an empty list
#returns nothing
"""
friends_records = FriendsRecord()
friends_record.records # => []

"""
Given a name and a date 
#update the records list
"""
friends_records = FriendsRecord()
friends_record.add_friend("Ali", "01/01/2000")
friends_record.records # => ["Ali", "01/01/2000"]

"""
Given two names and a dates  
#update the records list in order
"""
friends_records = FriendsRecord()
friends_record.add_friend("Ali", "01/01/2000")
friends_record.add_friend("Lisa", "02/02/2001")
friends_record.records # => ["Ali" "01/01/2000", "Lisa", "02/02/2001"]
"""
Ammend a date 
#update the date on records list
"""
friends_records = FriendsRecord()
friends_record.add_friend("Ali", "01/01/2000")
friends_record.ammend_birthdate("Ali", "02/01/2000")
friends_record.records # => ["Ali", "02/01/2000"]

"""
Ammend a name
#update the name on records list
"""
friends_records = FriendsRecord()
friends_record.add_friend("Ali", "01/01/2000")
friends_record.ammend_name("Ali", "William")
friends_record.records # => ["William", "01/01/2000"]

"""
Check earliest birthdate, so we can send a card
#returns the person with the earliest birthdate
"""
friends_records = FriendsRecord()
friends_record.add_friend("Ali", "19/07/2002")
friends_record.add_friend("Lisa", "24/07/2002")
friends_record.check_earliest_birthdate() # => ["Ali"]

"""
Calculate age
#returns the age of the name given 
"""
friends_records = FriendsRecord()
friends_record.add_friend("Ali", "19/07/2002")
friends_record.calculate_age() # => 22



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
