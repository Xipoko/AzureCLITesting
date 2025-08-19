#!/usr/bin/env python3
"""
Azure CLI JSON Configuration Generator
Generates JSON files for use with Azure CLI commands in PowerShell
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class AzureJSONGenerator:
    def __init__(self, output_dir: str = "azure_configs"):
        self.output_dir = output_dir
        self.ensure_output_directory()
    
    def ensure_output_directory(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"Created output directory: {self.output_dir}")
    
    def save_json(self, data: Dict[str, Any], filename: str) -> str:
        """Save dictionary as JSON file"""
        filepath = os.path.join(self.output_dir, f"{filename}.json")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Generated: {filepath}")
        return filepath
    
    def create_resource_group_config(self, name: str, location: str, tags: Dict[str, str] = None) -> str:
        """Generate JSON for creating a resource group"""
        config = {
            "name": name,
            "location": location,
            "tags": tags or {}
        }
        
        return self.save_json(config, f"rg_{name}")
    
    def create_vm_config(self, vm_name: str, resource_group: str, location: str, 
                        vm_size: str = "Standard_B2s", admin_username: str = "azureuser") -> str:
        """Generate JSON for creating a virtual machine"""
        config = {
            "vmName": vm_name,
            "resourceGroup": resource_group,
            "location": location,
            "vmSize": vm_size,
            "adminUsername": admin_username,
            "osType": "Linux",
            "imagePublisher": "Canonical",
            "imageOffer": "0001-com-ubuntu-server-focal",
            "imageSku": "20_04-lts-gen2",
            "imageVersion": "latest",
            "storageAccountType": "Standard_LRS",
            "networkSecurityGroup": {
                "rules": [
                    {
                        "name": "SSH",
                        "protocol": "Tcp",
                        "priority": 1001,
                        "access": "Allow",
                        "direction": "Inbound",
                        "sourceAddressPrefix": "*",
                        "sourcePortRange": "*",
                        "destinationAddressPrefix": "*",
                        "destinationPortRange": "22"
                    }
                ]
            }
        }
        
        return self.save_json(config, f"vm_{vm_name}")
    
    def create_storage_account_config(self, name: str, resource_group: str, 
                                    location: str, sku: str = "Standard_LRS") -> str:
        """Generate JSON for creating a storage account"""
        config = {
            "storageAccountName": name,
            "resourceGroup": resource_group,
            "location": location,
            "sku": {
                "name": sku
            },
            "kind": "StorageV2",
            "accessTier": "Hot",
            "allowBlobPublicAccess": False,
            "supportsHttpsTrafficOnly": True
        }
        
        return self.save_json(config, f"storage_{name}")
    
    def create_app_service_plan_config(self, name: str, resource_group: str, 
                                     location: str, sku: str = "B1") -> str:
        """Generate JSON for creating an App Service Plan"""
        config = {
            "name": name,
            "resourceGroup": resource_group,
            "location": location,
            "sku": sku,
            "isLinux": True
        }
        
        return self.save_json(config, f"asp_{name}")
    
    def create_web_app_config(self, name: str, resource_group: str, 
                            app_service_plan: str, runtime: str = "PYTHON|3.9") -> str:
        """Generate JSON for creating a Web App"""
        config = {
            "name": name,
            "resourceGroup": resource_group,
            "plan": app_service_plan,
            "runtime": runtime,
            "deployFromLocalGit": False,
            "appSettings": [
                {
                    "name": "WEBSITES_ENABLE_APP_SERVICE_STORAGE",
                    "value": "false"
                }
            ]
        }
        
        return self.save_json(config, f"webapp_{name}")
    
    def create_bulk_deployment_config(self, project_name: str, location: str) -> str:
        """Generate a comprehensive deployment configuration"""
        timestamp = datetime.now().strftime("%Y%m%d")
        
        config = {
            "deploymentInfo": {
                "projectName": project_name,
                "deploymentDate": datetime.now().isoformat(),
                "location": location
            },
            "resourceGroup": {
                "name": f"rg-{project_name}-{timestamp}",
                "location": location,
                "tags": {
                    "project": project_name,
                    "environment": "development",
                    "created": timestamp
                }
            },
            "storageAccount": {
                "name": f"st{project_name}{timestamp}",
                "sku": "Standard_LRS"
            },
            "appServicePlan": {
                "name": f"asp-{project_name}",
                "sku": "B1"
            },
            "webApp": {
                "name": f"webapp-{project_name}-{timestamp}",
                "runtime": "PYTHON|3.9"
            },
            "virtualMachine": {
                "name": f"vm-{project_name}",
                "size": "Standard_B2s",
                "adminUsername": "azureuser"
            }
        }
        
        return self.save_json(config, f"bulk_deployment_{project_name}")
    
    def create_powershell_commands(self, config_files: List[str]) -> str:
        """Generate PowerShell script that uses the JSON configurations"""
        ps_commands = [
            "# Azure CLI PowerShell Commands",
            "# Generated automatically - customize as needed",
            "",
            "# Login to Azure (uncomment if needed)",
            "# az login",
            "",
            "# Set default subscription (uncomment and update)",
            "# az account set --subscription 'your-subscription-id'",
            ""
        ]
        
        for config_file in config_files:
            filename = os.path.basename(config_file)
            name = os.path.splitext(filename)[0]
            
            if filename.startswith("rg_"):
                ps_commands.extend([
                    f"# Create Resource Group from {filename}",
                    f"$rgConfig = Get-Content '{filename}' | ConvertFrom-Json",
                    f"az group create --name $rgConfig.name --location $rgConfig.location --tags $($rgConfig.tags | ConvertTo-Json -Compress)",
                    ""
                ])
            
            elif filename.startswith("storage_"):
                ps_commands.extend([
                    f"# Create Storage Account from {filename}",
                    f"$storageConfig = Get-Content '{filename}' | ConvertFrom-Json",
                    f"az storage account create --name $storageConfig.storageAccountName --resource-group $storageConfig.resourceGroup --location $storageConfig.location --sku $storageConfig.sku.name",
                    ""
                ])
            
            elif filename.startswith("vm_"):
                ps_commands.extend([
                    f"# Create Virtual Machine from {filename}",
                    f"$vmConfig = Get-Content '{filename}' | ConvertFrom-Json",
                    f"az vm create --resource-group $vmConfig.resourceGroup --name $vmConfig.vmName --image UbuntuLTS --admin-username $vmConfig.adminUsername --generate-ssh-keys --size $vmConfig.vmSize",
                    ""
                ])
        
        # Save PowerShell script
        ps_script_path = os.path.join(self.output_dir, "deploy_azure_resources.ps1")
        with open(ps_script_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(ps_commands))
        
        print(f"Generated PowerShell script: {ps_script_path}")
        return ps_script_path

def main():
    """Example usage of the Azure JSON Generator"""
    generator = AzureJSONGenerator()
    
    print("Azure CLI JSON Configuration Generator")
    print("=" * 50)
    
    # Generate individual configurations
    config_files = []
    
    # Resource Group
    rg_file = generator.create_resource_group_config(
        name="my-project-rg",
        location="eastus",
        tags={"environment": "dev", "project": "demo"}
    )
    config_files.append(rg_file)
    
    # Storage Account
    storage_file = generator.create_storage_account_config(
        name="mystorageaccount123",
        resource_group="my-project-rg",
        location="eastus"
    )
    config_files.append(storage_file)
    
    # Virtual Machine
    vm_file = generator.create_vm_config(
        vm_name="my-dev-vm",
        resource_group="my-project-rg",
        location="eastus"
    )
    config_files.append(vm_file)
    
    # App Service Plan
    asp_file = generator.create_app_service_plan_config(
        name="my-app-service-plan",
        resource_group="my-project-rg",
        location="eastus"
    )
    config_files.append(asp_file)
    
    # Web App
    webapp_file = generator.create_web_app_config(
        name="my-web-app-123",
        resource_group="my-project-rg",
        app_service_plan="my-app-service-plan"
    )
    config_files.append(webapp_file)
    
    # Bulk deployment configuration
    bulk_file = generator.create_bulk_deployment_config(
        project_name="myproject",
        location="eastus"
    )
    config_files.append(bulk_file)
    
    # Generate PowerShell commands
    generator.create_powershell_commands(config_files)
    
    print(f"\nAll configurations generated in: {generator.output_dir}")
    print("\nNext steps:")
    print("1. Review the generated JSON files")
    print("2. Modify configurations as needed")
    print("3. Run the PowerShell script: .\\deploy_azure_resources.ps1")
    print("4. Or use individual JSON files with your own Azure CLI commands")

if __name__ == "__main__":
    main()