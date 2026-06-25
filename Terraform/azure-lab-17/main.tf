terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "tf_rg" {
  name     = "TerraformResourceGroup"
  location = "East US"
}

resource "azurerm_storage_account" "tf_storage" {
  name                     = "choarotfstorage"
  resource_group_name      = azurerm_resource_group.tf_rg.name
  location                 = azurerm_resource_group.tf_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}