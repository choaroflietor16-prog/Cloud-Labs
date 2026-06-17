# Azure Lab 15

## Objective
Deploy Azure Bastion to securely connect to MyVM without exposing SSH to the internet.

## Commands Used
az network vnet subnet create --name AzureBastionSubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.2.0/24
az network public-ip create --name BastionPublicIP --resource-group MyResourceGroup --sku Standard --location eastus
az network bastion create --name MyBastion --resource-group MyResourceGroup --vnet-name MyVNet --public-ip-address BastionPublicIP --location eastus

## Result
Azure Bastion successfully deployed.
VM accessible securely through Azure Portal without exposing SSH port 22.