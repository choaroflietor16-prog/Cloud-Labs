# Azure Lab 12

## Objective
Create an Azure Storage Account and upload a file to Blob Storage.

## Commands Used
az storage account create --name choarostorage --resource-group MyResourceGroup --location eastus --sku Standard_LRS
az storage container create --name mycontainer --account-name choarostorage
az storage blob upload --account-name choarostorage --container-name mycontainer --name profile.jpeg --file ~/Cloud-Labs/Azure/profile.jpeg
az storage blob list --account-name choarostorage --container-name mycontainer --output table

## Result
Storage account created and file successfully uploaded to Blob Storage.