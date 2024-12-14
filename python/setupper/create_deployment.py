import os
from rest import RestClient
from dotenv import load_dotenv

load_dotenv()

# for Elastic Cloud
EC_API_KEY = os.getenv("EC_API_KEY")
ec = RestClient("https://api.elastic-cloud.com", api_key=EC_API_KEY)

def deploy_cluster():
    ec.post(
        "/api/v1/deployments?validate_only=false",
        file="requests/ec_deployment.json"
    )

def setup():
    print("Setting up...")

    deploy_cluster()
    
    print("Setup complete")

if __name__ == "__main__":
    setup()