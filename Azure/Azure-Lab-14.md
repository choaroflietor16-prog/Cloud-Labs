# Azure Lab 14

## Objective
Create an Azure Key Vault and store a secret securely.

## Commands Used
az keyvault create --name choaro-keyvault --resource-group MyResourceGroup --location eastus
az keyvault secret set --vault-name choaro-keyvault --name MySecret --value "MySecretPassword123"
az keyvault secret show --vault-name choaro-keyvault --name MySecret
az keyvault secret list --vault-name choaro-keyvault --output table

## Result
Key Vault created and secret successfully stored and retrieved.