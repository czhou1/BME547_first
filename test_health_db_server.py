# have to import global variables, changes will stay (must clear)
from health_db_server import db


def test_add_database_entry():
    from health_db_server import add_database_entry
    answer = add_database_entry('David', 1, 'O+')
    expected = [{'name': 'David', 'id': 1, 'blood_type': 'O+', 'tests': []}]
    assert db == expected


def test_find_patient():
    from health_db_server import find_patient
    from health_db_server import add_database_entry
    # clear database
    db.clear()
    expected = {'name': 'David', 'id': 1, 'blood_type': 'O+', 'tests': []}
    # repopulate database with info you need
    add_database_entry('David', 1, 'O+')
    answer = find_patient(1)

    assert answer == expected