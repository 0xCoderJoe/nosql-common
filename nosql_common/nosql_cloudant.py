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
        self.service.service_url(self.cloudant_url)

    def check_db_availability(self):
        '''Will query the database and check for readiness'''
        try:
            self.service.get_server_information().get_result()
            return 0
        except:
            sys.exit(1)