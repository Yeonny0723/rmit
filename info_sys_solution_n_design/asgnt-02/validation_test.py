# validation_test.py

# Import file/class to test
from validation import Validation


def test_is_numeric(validation):
    """
    A function to test if input contains only number

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n1.Testing is_numeric()") 
    
    # True
    assert (validation.is_numeric(10))

    # False
    assert (not validation.is_numeric(10.002))
    assert (not validation.is_numeric("abc"))
    assert (not validation.is_numeric("10abc"))


def test_is_alphabetic(validation):
    """
    A function to test if input contains only alphabet

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n2. Testing is_alphabetic()")

    # True
    assert (validation.is_alphabetic("abc"))

    # False
    assert (not validation.is_alphabetic(10))    
    assert (not validation.is_alphabetic(10.002)) 
    assert (not validation.is_alphabetic("10abc"))


def test_is_phone_number(validation):
    """
    A function to test if input follows phone number format of 0000-000-000 or 0000 000 000

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n4. Testing is_phone_number()")

    # True
    assert (validation.is_phone_number("0223 999 999")) 
    assert (validation.is_phone_number("0456-999-999"))

    # False
    assert (not validation.is_phone_number("(02) 9999 9999"))
    assert (not validation.is_phone_number("0299999999"))
    assert (not validation.is_phone_number("02.9999.9999"))
    assert (not validation.is_phone_number("+61 2 9999 9999"))


def test_is_email(validation):
    """
    A function to test if input follows typical email format

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n5. Testing is_email()")

    # True
    assert  (validation.is_email("xyz@abc.def")) 
    assert (validation.is_email("xyz@abcdef"))
    assert (validation.is_email("xyz@abcdef.com.com"))

    # False
    assert (not validation.is_email("xyzabcdef"))
    assert (not validation.is_email("@abcdef"))
    

def test_is_date(validation):
    """
    A function to test if input follows phone number format of dd/mm/yyyy

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n6. Testing is_date()")

     # True
    assert  (validation.is_date("23/07/1999")) 

    # False
    assert (not validation.is_date("123/022/1999"))
    assert (not validation.is_date("23-07-1999"))   
    assert (not validation.is_date("23-42-1999"))   
    

def test_is_expiry_date(validation):
    """
    A function to test if input follows phone number format of mm/yy

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n7. Testing is_expiry_date()")

     # True
    assert  (validation.is_expiry_date("07/23")) 

    # False
    assert (not validation.is_expiry_date("15/23"))
    assert (not validation.is_expiry_date("23-07"))   
    assert (not validation.is_expiry_date("2342/1999"))   
    

def test_is_credit_num(validation):
    """
    A function to test if input follows phone number format of 0000-0000-0000-0000 or 0000 0000 0000 0000

    Parameters: Data to validate. 

    Return: None
    """ 
    print("\n8. Testing is_credit_num()")

     # True
    assert  (validation.is_credit_num("1111-1111-1111-1111")) 
    assert  (validation.is_credit_num("1111 1111 1111 1111")) 

    # False
    assert (not validation.is_credit_num("1111/1111/1111/1111"))
    assert (not validation.is_credit_num("1111111111111111"))   


if __name__ == '__main__':
    
    print("\nTesting ...")

    # Instantiate a validation object
    validation = Validation()

    test_is_numeric(validation)

    test_is_alphabetic(validation)

    test_is_phone_number(validation)

    test_is_email(validation)

    test_is_date(validation)

    test_is_expiry_date(validation)
    
    test_is_credit_num(validation)

