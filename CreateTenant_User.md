# Create a new user in your tenant
az ad user create `
    --display-name "Lab User" `
    --user-principal-name labuser@DallasBrown12345Gmail.onmicrosoft.com `
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


# Create resource group (if not exists)
az group create --name azureclitesting --location westus

# Create VM
az vm create `
    --resource-group azureclitesting `
    --name azureclitestingvm `
    --image "ubuntu2204" `
    --admin-username dallasbrown12345 `
    --generate-ssh-keys



    # Create a basic Azure VM with Ubuntu

    ```sh
    az vm create `
        --resource-group azclitesting `
        --name myUbuntuVM `
        --image UbuntuLTS `
        --admin-username Lab User `
        --generate-ssh-keys
    ```




