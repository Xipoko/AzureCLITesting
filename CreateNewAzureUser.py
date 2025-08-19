# Create a new Azure AD user using Azure CLI
# Replace the values below with your desired user details
from datetime import datetime


DisplayName = input("Enter the display name for the new user: ")
UserPrincipalName = input("Enter the full name for the new user with no spaces: (ex. xipokobeats)")
Password = input("Enter a strong password: ") # Set a strong password

filename = f"{UserPrincipalName}_AzureUser"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename2 = f"All_AzureUsers"
filename3 = f"UserDatabase"
filename4 = f"testing"

content = f'''az ad user create `
              --display-name "{DisplayName}" `
              --password "{Password}" `
              --user-principal-name "{UserPrincipalName}@DallasBrown12345Gmail.onmicrosoft.com"
'''

with open(filename, "w") as file:
    file.write(content)
print(f"File Saved: {filename}")

with open(filename2, "a") as file:
    file.write(content)
print(f"File Saved: {filename2}")


#for filename in [filename3, filename4]:
#    with open(filename, "w") as file:
#        file.write(content)
#    print(f"File saved: {filename}")

print(f"Command saved to file: {filename}")
print(f"Command saved to file: {filename2}")

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