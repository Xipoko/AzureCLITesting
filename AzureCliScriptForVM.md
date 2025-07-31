# Azure CLI script to create a new VM

# Variables
resourceGroup="myResourceGroup"
location="eastus"
vmName="myVM"
image="UbuntuLTS"
adminUsername="azureuser"

# Create resource group (if not exists)
az group create --name $resourceGroup --location $location

# Create VM
az vm create \
    --resource-group $resourceGroup \
    --name $vmName \
    --image $image \
    --admin-username $adminUsername \
    --generate-ssh-keys

# Output public IP
az vm show \
    --resource-group $resourceGroup \
    --name $vmName \
    --show-details \
    --query "publicIps" \
    --output tsv


    # Example: Configure VM size and attach a data disk
    az vm update \
        --resource-group $resourceGroup \
        --name $vmName \
        --set hardwareProfile.vmSize=Standard_DS2_v2

    az vm disk attach \
        --resource-group $resourceGroup \
        --vm-name $vmName \
        --name myDataDisk \
        --size-gb 128

        # Note: Creating a new Azure AD tenant cannot be done directly via Azure CLI.
        # You must use the Azure Portal for tenant creation.
        # However, you can manage subscriptions, users, and roles in an existing tenant via CLI.

        # Example: Create a new user in the current tenant
        az ad user create \
            --display-name "Lab User" \
            --user-principal-name labuser@$(az account show --query 'tenantId' -o tsv).onmicrosoft.com \
            --password "StrongPassword123!"

        # Example: List all tenants your account can access
        az account tenant list --output table

        # Example: Set the active tenant (if you have access to multiple)
        az account tenant set --tenant-id <tenant_id>

        # Example: Assign a role to a user in a subscription
        az role assignment create \
            --assignee labuser@<yourtenant>.onmicrosoft.com \
            --role "Contributor" \
            --subscription <subscription_id>

            # Create a new user in your tenant
            az ad user create \
                --display-name "Lab User" \
                --user-principal-name labuser@DallasBrown12345Gmail.onmicrosoft.com \
                --password "StrongPassword123!"

            # List all tenants your account can access
            az account tenant list --output table

            # Set the active tenant (if you have access to multiple)
            az account tenant set --tenant-id 1f634a08-6b7f-452e-bebc-2ae69189deb9

            # Assign Contributor role to the new user in your subscription
            az role assignment create \
                --assignee labuser@DallasBrown12345Gmail.onmicrosoft.com \
                --role "Contributor" \
                --subscription 965b2260-d6e6-4fc4-bf17-4dbd012e0ea7