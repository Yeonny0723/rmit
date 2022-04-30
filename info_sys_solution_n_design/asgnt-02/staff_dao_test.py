# staff_dao_test.py

# Import the DAO
from staff_dao import StaffDAO

def test_create():
        
    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()

    # 2. Set up the data to insert
    data = {
        'first_name':"Justin",
        'lastname': "Lee",
        'email': "justin@ahs.com",
        'title': "receptionist"
    }

    # 3. Call the create() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = staff_dao.create(data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_by_id():

    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()

    # 2. Setup the ID to find
    customer_id = 1
    
    # 3. Call the find_by_id() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = staff_dao.find_by_id(customer_id)

    # 4. Do something with the results e.g. print it
    print(result)
   

def test_find_all():
   
    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()

    # 2. Call the find_all() method
    # And store the returned value somewhere
    result = staff_dao.find_all()

    # 4. Do something with the results e.g. print it
    print(result)

 
def test_find_by_lastname():
     
    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()
     
    # 2. Setup the lastname to find
    lastname = "Lee"

    # 3. Call the find_by_lastname() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = staff_dao.find_by_lastname(lastname)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_ids():

    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()

    # 2. Call the find_ids() method on the DAO
    result = staff_dao.find_ids()

    # 3. Print the result
    print(result)


def test_update():

    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()

    # 2. Set up the data to update i.e. ID and data
    staff_id = 1
    data = {}
    data['firstname'] = "Joe"
    data['lastname']  = "Pollard"
        
    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = staff_dao.update(staff_id, data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_delete():

    # 1. Instantiate the staff DAO
    staff_dao = StaffDAO()

    # 2. Set up the ID to update
    customer_id = 1

    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = staff_dao.delete(customer_id)

    # 4. Do something with the results e.g. print it
    print(result)


if __name__ == "__main__":

    test_create()
    
    test_find_by_id()

    # test_find_all()

    # test_find_by_lastname()

    # test_find_ids()

    # test_update()

    # test_delete()
