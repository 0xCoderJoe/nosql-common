import pytest as pytest
from datetime import datetime
from dotenv import load_dotenv
from nosql_common.nosql_cloudant import NoSQLCommCloudant

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
    


