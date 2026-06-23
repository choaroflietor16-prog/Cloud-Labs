# Azure Lab 18

## Objective
Set up Azure Backup to protect MyVM with automated backups.

## Commands Used
az backup vault create --name MyBackupVault --resource-group MyResourceGroup --location eastus
az backup protection enable-for-vm --resource-group MyResourceGroup --vault-name MyBackupVault --vm MyVM --policy-name DefaultPolicy
az backup job list --resource-group MyResourceGroup --vault-name MyBackupVault --output table

## Result
Backup vault created and VM backup policy successfully applied.
MyVM is now protected with automated daily backups.