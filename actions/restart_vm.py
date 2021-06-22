from lib.base import AzureBaseAction


class RestartVM(AzureBaseAction):

    def run(self, group_name, vm_name):

        credentials, subscription_id = self.get_credentials()
        compute_client = ComputeManagementClient(credentials, subscription_id)

        try:
            # Restart the VM
            async_vm_start = compute_client.virtual_machines.start(
                group_name, vm_name)
            result = {"output": async_vm_start, "message": vm_name + "VM creation successful"}
        except CloudError:
            result = {"error": "A VM operation failed:\n" + traceback.format_exc()}
        else:
            result = {"message": "Start-VM operation completed successfully!"}

        return result
