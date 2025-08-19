# Create a new Azure AD user using Azure CLI
# Replace the values below with your desired user details

DisplayName = input("Enter the display name for the new user: ")
UserPrincipalName = input("Enter the full name for the new user with no spaces: (ex. xipokobeats)")
Password = input("Enter a strong password: ") # Set a strong password
#user_object_id = input("Enter the user's object ID: ")
#role = input("Enter the role to assign (e.g., Contributor): ")
#resource_group = input("Enter the resource group name: ")
print(f"az ad user create --display-name {DisplayName} --password {Password} --user-principal-name {UserPrincipalName }@DallasBrown12345Gmail.onmicrosoft.com")
#print(f"az role assignment create --assignee {user_object_id} --role \"{role}\" --resource-group \"{resource_group}\"")
with open("NewAzureUser", "a") as file:
    file.write(f'''az ad user create `
              --display-name "{DisplayName}" `
              --password "{Password}" `
              --user-principal-name "{UserPrincipalName}@DallasBrown12345Gmail.onmicrosoft.com" `
              --mail-nickname "{UserPrincipalName}"''')
#            --user_object_id "{user_object_id}"
#             --role "{role}" `
#              resource-group "{resource_group}"''')

              # Example: Assign a role to the user in a resource group
              #resource_group = input("Enter the resource group name: ")
              #role = input("Enter the role to assign (e.g., Contributor): ")
              #user_object_id = input("Enter the user's object ID: ")

              #print(f"az role assignment create --assignee {user_object_id} --role \"{role}\" --resource-group \"{resource_group}\"")
              #with open("NewAzureUser", "a") as file:
              #  file.write(f'\naz role assignment create --assignee "{user_object_id}" --role "{role}" --resource-group "{resource_group}"\n')

# Ensure each entry is separated by a newline for clarity
with open("NewAzureUser", "a") as file:
  file.write("\n")

#az ad user create `
#  --display-name $DisplayName `
#  --password $Password `
#  --user-principal-name $UserPrincipalName@DallasBrown12345Gmail.onmicrosoft.com `



# Prompt for additional user details if needed
#$MailNickname = Read-Host "Enter a mail nickname for the new user"

# Create the user with the provided variables
#az ad user create `
#  --display-name $DisplayName `
#  --password $Password `
##  --user-principal-name "$UserPrincipalName@DallasBrown12345Gmail.onmicrosoft.com" `
 # --mail-nickname $MailNickname



  #az ad user create `
  #--display-name "Dallas Demo User" `
  #--user-principal-name "demo.user@DallasBrown12345Gmail.onmicrosoft.com" `
  #--password "StrongP@ssword123!" `
  #--mail-nickname "DallasDemo"
  # The code above creates a new Azure AD user using Azure CLI.
  # Make sure you are logged in to Azure CLI and have the necessary permissions.
  # You can run this script in PowerShell after installing Azure CLI.

  # Example usage:
  # 1. Open PowerShell.
  # 2. Run: az login
  # 3. Execute this script.

  # For more options, see: https://learn.microsoft.com/en-us/cli/azure/ad/user#az-ad-user-create



#  az ad user create --display-name newtest --password password123 --user-principal-name newtest@@DallasBrown12345Gmail.onmicrosoft.com