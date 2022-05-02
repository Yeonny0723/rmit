# room_dao_test.py

# Import the DAO
from room_dao import RoomDAO

def test_create():
    """
    Test create method of RoomDAO

    Parameters: None

    Return: None
    """        
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()

    # 2. Set up the data to insert
    data = {
        'room_price':"200",
        'room_num': "101",
        'room_type_id': "1"
    }

    # 3. Call the create() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = room_dao.create(data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_by_id():
    """
    Test find_by_id method of RoomDAO

    Parameters: None

    Return: None
    """     
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()

    # 2. Setup the ID to find
    room_id = 1
    
    # 3. Call the find_by_id() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = room_dao.find_by_id(room_id)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_all():
    """
    Test find_all method of RoomDAO

    Parameters: None

    Return: None
    """        
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()

    # 2. Call the find_all() method
    # And store the returned value somewhere
    result = room_dao.find_all()

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_by_room_type():
    """
    Test find_by_room_type method of RoomDAO

    Parameters: None

    Return: None
    """          
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()
     
    # 2. Setup the lastname to find
    room_type_id = "1"

    # 3. Call the find_by_lastname() method on the DAO
    # Pass the data as param
    # And store the returned value somewhere
    result = room_dao.find_by_room_type(room_type_id)

    # 4. Do something with the results e.g. print it
    print(result)


def test_find_ids():
    """
    Test find_ids method of RoomDAO

    Parameters: None

    Return: None
    """     
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()

    # 2. Call the find_ids() method on the DAO
    result = room_dao.find_ids()

    # 3. Print the result
    print(result)


def test_update():
    """
    Test update method of RoomDAO

    Parameters: None

    Return: None
    """     
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()

    # 2. Set up the data to update i.e. ID and data
    room_id = 1
    data = {}
    data['room_price'] = "500"
    data['room_num']  = "1001"
    data['room_type_id']  = "1"
        
    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = room_dao.update(room_id, data)

    # 4. Do something with the results e.g. print it
    print(result)


def test_delete():
    """
    Test delete method of RoomDAO

    Parameters: None

    Return: None
    """     
    # 1. Instantiate the room DAO
    room_dao = RoomDAO()

    # 2. Set up the ID to update
    room_id = 1

    # 3. Call the update() method on the DAO
    # Pass the ID and data as params
    # And store the returned value somewhere
    result = room_dao.delete(room_id)

    # 4. Do something with the results e.g. print it
    print(result)


if __name__ == "__main__":

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_room_type()

    test_find_ids()

    test_update()

    test_delete()
