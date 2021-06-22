from lib.base import AzureBaseAction


class StopVM(AzureBaseAction):

    def run(self, group_name, vm_name):

        credentials, subscription_id = self.get_credentials()
        compute_client = ComputeManagementClient(credentials, subscription_id)

        try:
            # Stop the VM
            async_vm_stop = compute_client.virtual_machines.power_off(
                group_name, vm_name)
            result = {"output": async_vm_stop, "message": vm_name + "VM creation successful"}
        except CloudError:
            result = {"error": "A VM operation failed:\n" + traceback.format_exc()}
        else:
            result = {"message": "Stop-VM operation completed successfully!"}

        return result
