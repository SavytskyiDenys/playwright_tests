import pytest
from modules.common.database import Database



@pytest.mark.db
def test_db_connection():
    db = Database()
    db.test_connection()

@pytest.mark.db
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.db
def test_user_address_by_name():
    db = Database()
    address = db.get_user_address_by_name('Sergii')
    print(address)
    assert address[0][0] == 'Maydan Nezalezhnosti 1'
    assert address[0][1] == 'Kyiv'
    assert address[0][2] == '3127'
    assert address[0][3] == 'Ukraine'

@pytest.mark.db
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(2, 3)
    water_qnt = db.select_product_qnt_by_id(2)

    assert water_qnt[0][0] == 3

@pytest.mark.db
def test_product_insert():
    db = Database()
    db.add_new_product(4,'печиво','солодке',30)
    added_product = db.get_product_by_id(4)
    assert added_product[0][2] == 30

@pytest.mark.db
def test_delete_product():
    db = Database()
    db.add_new_product(99,'test', 'test desc',99)
    db.delete_product_by_id(99)
    product = db.get_product_by_id(99)
    assert len(product) == 0

@pytest.mark.db
def test_detailed_ordes():
    db = Database()
    orders = db.get_detailed_order()
    print("Замовлення", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
