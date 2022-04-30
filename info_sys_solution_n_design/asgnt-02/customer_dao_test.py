# customer_dao_test.py

# Import the DAO
from customer_dao import CustomerDAO


def test_create():
        
    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()

    # 2. Set up the data to insert
    data = {
        'first_name':"juyeon",
        'lastname': "kim",
        'phone_num': "01234566789",
        'email': 's3741327@student.rmit.edu.au',
        'credit_card_num': "1111-1111-1111",
        'expiry_date': '02/22',
        'cvc_code': '000',
        'dob': '23/07'
    }

    # 3. Call the create() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = customer_dao.create(data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_by_id():

    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()

    # 2. Setup the ID to find
    customer_id = 1
    
    # 3. Call the find_by_id() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = customer_dao.find_by_id(customer_id)


    # 4. Do something with the results e.g. print it
    print(result)
   

def test_find_all():
   
    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()

    # 2. Call the find_all() method
    # And store the returned value somewhere
    result = customer_dao.find_all()

    # 4. Do something with the results e.g. print it
    print(result)

 
def test_find_by_lastname():
     
    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()
     
    # 2. Setup the lastname to find
    lastname = "juyeon"

    # 3. Call the find_by_lastname() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = customer_dao.find_by_lastname(lastname)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_ids():

    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()

    # 2. Call the find_ids() method on the DAO
    result = customer_dao.find_ids()

    # 3. Print the result
    print(result)


def test_update():

    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()

    # 2. Set up the data to update i.e. ID and data
    customer_id = 1
    data = {}
    data['first_name'] = "yeonny"
    data['lastname']  = "kim"
    data['phone_num']  = "11111111"
    data['email']  = "yeonny@gmail.com"
    data['credit_card_num']  = "2222-2222-2222"
    data['expiry_date']  = "02/23"
    data['cvc_code']  = "111"
    data['dob']  = "23/07"
        
    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = customer_dao.update(customer_id, data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_delete():

    # 1. Instantiate the customer DAO
    customer_dao = CustomerDAO()

    # 2. Set up the ID to update
    customer_id = 1

    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = customer_dao.delete(customer_id)

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
