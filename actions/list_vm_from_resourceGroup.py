from lib.base import AzureBaseAction


class ListVM_ResourceGroup(AzureBaseAction):

    def run(self, group_name):

        credentials, subscription_id = self.get_credentials()
        compute_client = ComputeManagementClient(credentials, subscription_id)

        try:
            # print('\nList VMs in Resource Group')
            list_vm = []
            for vm in compute_client.virtual_machines.list_all(group_name):
                # print("\tVM: {}".format(vm.name))
                list_vm.append(vm.name)
            result = {"output": list_vm, "message": "VM listing from " + group_name+" successful"}
        except CloudError:
            result = {"error": "A VM operation failed:\n" + traceback.format_exc()}
        else:
            result = {"message": "listing VMs from resource group operation completed successfully!"}

        return result
