from db.main import get_from_db, post_to_db

def test_get_from_db():
    table =  "degrees"
    row = "info"

    expected_response = 'https://www.uab.cat/doc/Horari_GEI_Curs1_Sem1'

    response = get_from_db(table, row)
    print(response)

    assert  response['schedule']['1r']['1r Semestre'] == expected_response


def test_post_to_db():
    post_to_db('bot/data/upload_db.json', 'degrees', 'info')