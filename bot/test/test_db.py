from db.main import get_from_db

def test_get_from_db():
    table =  "degrees"
    row = "info"

    expected_response = ''

    response = get_from_db(table, row)

    assert  response == expected_response