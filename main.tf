# variable "vault_azure_secret_backend_path" {}
# variable "vault_azure_secret_backend_role" {}
# variable "gitlab_jwt_token" {}
# variable "gitlab_jwt_role" {}
# variable "arm_subscription_id" {}
# variable "arm_tenant_id" {}
# variable "vault_addr" {}
# variable "vault_namespace" {}

terraform {
}

provider "vault" {
}

data "vault_azure_access_credentials" "creds" {
  backend                     = var.vault_azure_secret_backend_path
  role                        = var.vault_azure_secret_backend_role
  validate_creds              = true
  num_sequential_successes    = 48
  num_seconds_between_tests   = 7
  max_cred_validation_seconds = 1200 // 20 minutes
}


provider "azurerm" {
  features {}
  tenant_id = var.arm_tenant_id
  subscription_id = var.arm_subscription_id
  client_id = data.vault_azure_access_credentials.creds.client_id
  client_secret = data.vault_azure_access_credentials.creds.client_secret
}

resource "random_string" "random" {
  length           = 8
  special          = false
}

resource "azurerm_virtual_network" "example" {
  name                = "nw-sreenath-${random_string.random.result}"
  resource_group_name = var.resource_group_name
  location            = "WestEurope"
  address_space       = ["10.0.0.0/16"]
  tags = {
    pipeline = "gitlab"
  }
}

output "hello_world" {
  value = "Hello, World!"
}
