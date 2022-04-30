# booking_dao_test.py

# Import the DAO
from booking_dao import BookingDAO
# Import packages
from datetime import datetime

def test_create():
        
    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()

    # 2. Set up the data to insert
    data = {
        'check_in':"22/04/2022",
        'check_out': "27/04/2022",
        'extra_bed': "1",
        'adult_num': "2",
        'child_num': "1",
        'infant_num': "0",
        'total_price': "250",
        'booking_dtm': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'room_id': "1",
        'staff_id': "1",
        'customer_id': "1",
        'phone_num': "3333333333"
    }

    # 3. Call the create() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = booking_dao.create(data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_by_id():

    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()

    # 2. Setup the ID to find
    booking_id = 1
    
    # 3. Call the find_by_id() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = booking_dao.find_by_id(booking_id)

    # 4. Do something with the results e.g. print it
    print(result)
   

def test_find_all():
   
    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()

    # 2. Call the find_all() method
    # And store the returned value somewhere
    result = booking_dao.find_all()

    # 4. Do something with the results e.g. print it
    print(result)

 
def test_find_by_customer_id():
     
    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()
     
    # 2. Setup the lastname to find
    customer_id = "1"

    # 3. Call the find_by_customer_id() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = booking_dao.find_by_customer_id(customer_id)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_ids():

    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()

    # 2. Call the find_ids() method on the DAO
    result = booking_dao.find_ids()

    # 3. Print the result
    print(result)


def test_update():

    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()

    # 2. Set up the data to update i.e. ID and data
    booking_id = 1
    data = {}
    data['check_in'] = "23/04/2022"
    data['check_out']  = "27/04/2022"
    data['extra_bed']  = 1
    data['adult_num']  = "2"
    data['child_num']  = "1"
    data['infant_num']  = "0"
    data['total_price']  = "300"
    data['booking_dtm']  = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data['room_id']  = "1"
    data['staff_id']  = "1"
    data['customer_id']  = "1"
    data['phone_num']  = "0400 000 000"
        
    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = booking_dao.update(booking_id, data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_delete():

    # 1. Instantiate the booking DAO
    booking_dao = BookingDAO()

    # 2. Set up the ID to delete
    booking_id = 1

    # 3. Call the delete() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = booking_dao.delete(booking_id)

    # 4. Do something with the results e.g. print it
    print(result)


if __name__ == "__main__":

    test_create()

    test_find_by_id()

    test_find_all()

    test_find_by_customer_id()

    test_find_ids()

    test_update()

    test_delete()
