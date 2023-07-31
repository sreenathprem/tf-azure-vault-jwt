variable "vault_azure_secret_backend_role" {
    description = "Role for getting creds from Azure"  
}

variable "arm_tenant_id" {
    description = "Tenant id in Azure"  
}

variable "arm_subscription_id" {
    description = "Subscription id in Azure"  
}

variable "vault_azure_secret_backend_path" {
    description = "Backend path in Vault for reading secrets"  
}

variable "resource_group_name" {
}