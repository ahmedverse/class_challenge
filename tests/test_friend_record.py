from lib.friend_record import *

def test_give_empty_list():

    friend_record = FriendsRecord()
    assert friend_record.records == []

def test_if_name_and_birthdate_given_update_list():

    friend_record = FriendsRecord()
    friend_record.add_friend("Ali", "01/01/2000")
    assert friend_record.records == [{"name":"Ali", "birthdate":"01/01/2000"}]

def test_if_two_names_and_two_birthdates_given_update_list():

    friend_record = FriendsRecord()
    friend_record.add_friend("Ali", "01/01/2000")
    friend_record.add_friend("Lisa", "02/02/2001")
    assert friend_record.records == [{"name":"Ali", "birthdate":"01/01/2000"}, {"name":"Lisa", "birthdate":"02/02/2001"}]

def test_if_birthdate_is_ammended():

    friend_record = FriendsRecord()
    friend_record.add_friend("Ali", "01/01/2000")
    friend_record.ammend_birthdate("Ali", "02/01/2000")
    assert friend_record.records == [{"name":"Ali", "birthdate":"02/01/2000"}]

def test_if_name_is_ammended():

    friend_record = FriendsRecord()
    friend_record.add_friend("Ali", "01/01/2000")
    friend_record.ammend_name("Ali", "William")
    friend_record.records # => ["William", "01/01/2000"]
    assert friend_record.records == [{"name":"William", "birthdate":"01/01/2000"}]

def test_returns_person_with_earliest_birthday():

    friends_record = FriendsRecord()
    friends_record.add_friend("Ali", "19/07/2002")
    friends_record.add_friend("Lisa", "24/07/2002")
    assert friends_record.check_earliest_birthdate() == "Ali"

"""
Calculate age
#returns the age of the name given 
"""
def test_calculate_age_returns_friend_age():
    friends_record = FriendsRecord()
    friends_record.add_friend("Ali", "19/07/2002")
    assert friends_record.calculate_age("Ali") == 23