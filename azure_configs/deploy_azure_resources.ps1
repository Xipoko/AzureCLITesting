# Azure CLI PowerShell Commands
# Generated automatically - customize as needed

# Login to Azure (uncomment if needed)
# az login

# Set default subscription (uncomment and update)
# az account set --subscription 'your-subscription-id'

# Create Resource Group from rg_my-project-rg.json
$rgConfig = Get-Content 'rg_my-project-rg.json' | ConvertFrom-Json
az group create --name $rgConfig.name --location $rgConfig.location --tags $($rgConfig.tags | ConvertTo-Json -Compress)

# Create Storage Account from storage_mystorageaccount123.json
$storageConfig = Get-Content 'storage_mystorageaccount123.json' | ConvertFrom-Json
az storage account create --name $storageConfig.storageAccountName --resource-group $storageConfig.resourceGroup --location $storageConfig.location --sku $storageConfig.sku.name

# Create Virtual Machine from vm_my-dev-vm.json
$vmConfig = Get-Content 'vm_my-dev-vm.json' | ConvertFrom-Json
az vm create --resource-group $vmConfig.resourceGroup --name $vmConfig.vmName --image UbuntuLTS --admin-username $vmConfig.adminUsername --generate-ssh-keys --size $vmConfig.vmSize
