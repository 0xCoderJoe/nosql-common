import pytest as pytest
from dotenv import load_dotenv
from nosql_common.nosql_cloudant import NoSQLCommCloudant

DATABASE='dev-fantasy-football'

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
    if db.get_all_docs(DATABASE):
        pytest.exit

def test_get_document(db):
    print()

def test_update_document(db):
    print()

def test_check_doc_revision(db):
    print()


