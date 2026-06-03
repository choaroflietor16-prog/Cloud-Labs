# Azure Lab 04

## Objective
Create a Subnet inside MyVNet in Azure using the CLI.

## Commands Used
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.1.0/24
az network vnet subnet list --resource-group MyResourceGroup --vnet-name MyVNet --output table

## Result
Subnet successfully created inside MyVNet.