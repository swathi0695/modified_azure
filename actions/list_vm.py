from lib.base import AzureBaseAction


class ListVM(AzureBaseAction):

    def run(self):

        credentials, subscription_id = self.get_credentials()
        compute_client = ComputeManagementClient(credentials, subscription_id)

        try:
            # print('\nList VMs in subscription')
            list_vm = []
            for vm in compute_client.virtual_machines.list_all():
                # print("\tVM: {}".format(vm.name))
                list_vm.append(vm.name)
            result = {"output": list_vm, "message": "VM listing successful"}
        except CloudError:
            result = {"error": "A VM operation failed:\n" + traceback.format_exc()}
        else:
            result = {"message": "listing VMs operation completed successfully!"}

        return result
