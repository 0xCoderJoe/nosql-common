import pytest as pytest
from dotenv import load_dotenv
from nosql_common.nosql_cloudant import NoSQLCommCloudant

DATABASE='dev-fantasy-football'
TEST_DOC_ID='94eeee8f1a1f37383cfa2d7b15bf927a'
TEST_VIEW='player_id'
TEST_DDOC='player_id'

@pytest.fixture()
def db():
    '''Provides our connection object to Cloudant'''
    load_dotenv()
    db = NoSQLCommCloudant()
    yield db

def test_db_availability(db):
    '''Test the connection to the CloudantDB'''
    print('WIN')
    if db.check_db_availability():
        pytest.fail
    
def test_get_all_docs(db):
    '''Test recieving all documents'''
    if db.get_all_docs(DATABASE):
        pytest.exit

def test_get_document(db):
    '''Test retrieving a document'''
    if db.get_document(database=DATABASE, doc_id=TEST_DOC_ID):
        pytest.exit

def test_update_document(db):
    '''Test updating a document'''
    test_doc = db.get_document(database=DATABASE, doc_id=TEST_DOC_ID)._to_dict()['result']
    test_doc['status'] = "test-executed"

    if db.update_document(database=DATABASE, doc=test_doc):
        pytest.exit

def test_get_view(db):
    '''Test retrieving a specified view'''
    test_view = db.get_view(database=DATABASE, ddoc=TEST_DDOC, limit=500, view=TEST_VIEW)
    if test_view:
        pytest.exit
