import requests
import time

def trigger_terraform_run(api_token, workspace_id):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/vnd.api+json",
    }

    payload = {
        "data": {
            "attributes": {
            "message": "Triggered from Python"
            },
            "type":"runs",
            "relationships": {
            "workspace": {
                "data": {
                "type": "workspaces",
                "id": workspace_id
                }
            }   
            }
            }
        }

    url = f"https://app.terraform.io/api/v2/runs"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Terraform run triggered successfully!")
    else:
        print(f"Failed to trigger Terraform run. Status code: {response.status_code}")
        print(response.text)

def trigger_destroy_run(api_token, workspace_id):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/vnd.api+json",
    }

    payload = {
        "data": {
            "attributes": {
            "message": "Triggered from Python",
            "is-destroy": True
            },
            "type":"runs",
            "relationships": {
            "workspace": {
                "data": {
                "type": "workspaces",
                "id": workspace_id
                }
            }   
            }
            }
        }

    url = f"https://app.terraform.io/api/v2/runs"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Terraform run triggered successfully!")
    else:
        print(f"Failed to trigger Terraform run. Status code: {response.status_code}")
        print(response.text)

def main():
    api_token = "<TFC-API-TOKEN>"
    workspace_id = "<WS-ID>"
    count = 0

    while count < 20:
        trigger_terraform_run(api_token, workspace_id)
        trigger_destroy_run(api_token, workspace_id)
        count = count + 1

if __name__ == "__main__":
    main()
