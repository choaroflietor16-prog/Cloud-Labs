# Azure Lab 03

## Objective
Create a Virtual Network (VNet) in Azure using the CLI.

## Commands Used
az network vnet create --name MyVNet --resource-group MyResourceGroup --location eastus --address-prefix 10.0.0.0/16
az network vnet list --output table

## Result
Virtual Network successfully created inside MyResourceGroup.