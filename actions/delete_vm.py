from lib.base import AzureBaseAction


class DeleteVM(AzureBaseAction):

    def run(self, group_name, vm_name):

        credentials, subscription_id = self.get_credentials()
        compute_client = ComputeManagementClient(credentials, subscription_id)

        try:
            # Start the VM
            async_vm_delete = compute_client.virtual_machines.delete(
                group_name, vm_name)
            result = {"output": async_vm_delete, "message": vm_name + "VM creation successful"}
        except CloudError:
            result = {"error": "A VM operation failed:\n" + traceback.format_exc()}
        else:
            result = {"message": "Delete-VM operation completed successfully!"}

        return result
