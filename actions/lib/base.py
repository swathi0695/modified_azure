import os
import traceback

from st2common.runners.base_action import Action

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption

from msrestazure.azure_exceptions import CloudError

from haikunator import Haikunator

haikunator = Haikunator()

# Azure Datacenter
LOCATION = 'westus'

# Resource Group
GROUP_NAME = 'azure-sample-group-virtual-machines'

# Network
VNET_NAME = 'azure-sample-vnet'
SUBNET_NAME = 'azure-sample-subnet'

# VM
OS_DISK_NAME = 'azure-sample-osdisk'
STORAGE_ACCOUNT_NAME = haikunator.haikunate(delimiter='')

IP_CONFIG_NAME = 'azure-sample-ip-config'
NIC_NAME = 'azure-sample-nic'
USERNAME = 'userlogin'
PASSWORD = 'Pa$$w0rd91'
VM_NAME = 'VmName'

VM_REFERENCE = {
	'linux': {
		'publisher': 'Canonical',
		'offer': 'UbuntuServer',
		'sku': '16.04.0-LTS',
		'version': 'latest'
	},
	'windows': {
		'publisher': 'MicrosoftWindowsServer',
		'offer': 'WindowsServer',
		'sku': '2016-Datacenter',
		'version': 'latest'
	}
}

class AzureBaseAction(Action):
	def __init__(self, config):
		super(AzureBaseAction, self).__init__(config=config)
		
	def get_credentials():
		
		subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
		credentials = ServicePrincipalCredentials(
			client_id=os.environ['AZURE_CLIENT_ID'],
			secret=os.environ['AZURE_CLIENT_SECRET'],
			tenant=os.environ['AZURE_TENANT_ID']
		)
		return credentials, subscription_id
