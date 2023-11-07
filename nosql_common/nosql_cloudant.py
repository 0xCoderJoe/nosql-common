from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
import os
import sys


class NoSQLCommCloudant:

    def __init__(self):
        self.cloudant_iam = os.environ.get('IAM_APIKEY')
        self.cloudant_url = os.environ.get('CLOUDANT_URL')
        self.authenticator = IAMAuthenticator(self.cloudant_iam)
        self.service = CloudantV1(authenticator=self.authenticator)
        self.service.set_service_url(self.cloudant_url)

    def check_db_availability(self):
        '''Will query the database and check for readiness'''
        try:
            self.service.get_server_information().get_result()
            return 0
        except:
            sys.exit(1)

    def get_all_docs(self, database):
        '''Gets all documents from a Cloudant database'''
        try:
            all_docs = self.service.post_all_docs(
                db=database,
                include_docs=True
            ).get_result()
            return all_docs
        
        except ApiException:
            sys.exit(1)

    def get_document(self, database, doc_id):
        '''Gets a specific document from the given database'''
        doc = self.service.get_document(db=database, doc_id=doc_id)
        return doc

    def update_document(self, database, doc):
        '''Update a specifc document in the database'''
        result = self.service.post_document(db=database, document=doc)
        return result
    
