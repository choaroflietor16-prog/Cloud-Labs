# Azure Lab 07

## Objective
Create a Virtual Machine (VM) inside MyVNet and MySubnet in Azure using the CLI.

## Commands Used
az vm create --name MyVM --resource-group MyResourceGroup --location eastus --image Ubuntu2204 --vnet-name MyVNet --subnet MySubnet --admin-username azureuser --generate-ssh-keys
az vm list --resource-group MyResourceGroup --output table

## Result
Virtual Machine successfully created inside MyResourceGroup.