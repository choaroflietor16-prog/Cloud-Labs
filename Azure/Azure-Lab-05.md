# Azure Lab 05

## Objective
Create a Network Security Group (NSG) in Azure using the CLI.

## Commands Used
az network nsg create --name MyNSG --resource-group MyResourceGroup --location eastus
az network nsg list --resource-group MyResourceGroup --output table

## Result
Network Security Group successfully created inside MyResourceGroup.