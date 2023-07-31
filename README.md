## Test Setup for JWT integration between TFC and HCP Vault

Based on the instructions [here](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/vault-configuration)

### Changes from the original doc

1. Token TTL for JWT role increased to 36h
2. Additional access rights in the policy
```
# Configure the actual secrets the token should have access to
path "azure/creds/edu-app" {
  capabilities = ["read"]
}

# Configure access to the azure secrets engine
path "azure/config" {
  capabilities = ["read"]
}
```

### Test Results
I used a python script to issue simultaneos 40 runs (20 applies and 20 destroys) to test the setup. The results are as follows:

Success:
Error:
Success Rate: