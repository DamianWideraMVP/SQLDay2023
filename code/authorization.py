from __future__ import annotations

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dataclasses import dataclass

from access_parameters import PARAMETERS

import os, uuid, sys



@dataclass
class Authorization:
    def get_blob_service_client_sas() -> BlobServiceClient:
        account_url = PARAMETERS.DATALAKE
        credential = PARAMETERS.SASKEY
        blob_service_client = BlobServiceClient(account_url, credential=credential)

        return blob_service_client

    

