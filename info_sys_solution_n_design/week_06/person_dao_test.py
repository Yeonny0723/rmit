# person_dao_test.py

# Import the DAO
from full_dao import PersonDAO

def test_create():
        
    # 1. Instantiate the person DAO
    person_dao = PersonDAO()

    # 2. Set up the data to insert
    data = {
        'firstname':"Hamish",
        'lastname': "Pollard"
    }

    # 3. Call the create() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = person_dao.create(data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_by_id():

    # 1. Instantiate the person DAO
    person_dao = PersonDAO()

    # 2. Setup the ID to find
    person_id = 1
    
    # 3. Call the find_by_id() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = person_dao.find_by_id(person_id)

    # 4. Do something with the results e.g. print it
    print(result)
   

def test_find_all():
   
    # 1. Instantiate the person DAO
    person_dao = PersonDAO()

    # 2. Call the find_all() method
    # And store the returned value somewhere
    result = person_dao.find_all()

    # 4. Do something with the results e.g. print it
    print(result)

 
def test_find_by_lastname():
     
    # 1. Instantiate the person DAO
    person_dao = PersonDAO()
     
    # 2. Setup the lastname to find
    lastname = "Pollard"

    # 3. Call the find_by_lastname() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = person_dao.find_by_lastname(lastname)

    # 4. Do something with the results e.g. print it
    print(result)

def test_find_ids():

    # 1. Instantiate the person DAO
    person_dao = PersonDAO()

    # 2. Call the find_ids() method on the DAO
    result = person_dao.find_ids()

    # 3. Print the result
    print(result)


def test_update():

    # 1. Instantiate the person DAO
    person_dao = PersonDAO()

    # 2. Set up the data to update i.e. ID and data
    person_id = 1
    data = {}
    data['firstname'] = "Joe"
    data['lastname']  = "Pollard"
        
    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = person_dao.update(person_id, data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_delete():

    # 1. Instantiate the person DAO
    person_dao = PersonDAO()

    # 2. Set up the ID to update
    person_id = 1

    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = person_dao.delete(person_id)

    # 4. Do something with the results e.g. print it
    print(result)


if __name__ == "__main__":

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_lastname()

    test_find_ids()

    test_update()

    test_delete()
