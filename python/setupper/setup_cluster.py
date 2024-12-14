import os
from rest import RestClient
from dotenv import load_dotenv

load_dotenv()

ES_URL = os.getenv("ES_URL")
ES_API_KEY = os.getenv("ES_API_KEY")
es = RestClient(ES_URL, api_key=ES_API_KEY)

def clean():
    es.delete("/_inference/text_embedding/e5-small-endpoint")

def es_connectivity_test():
    res = es.get("/")
    if res.status_code != 200:
        print("Elasticsearch is not running")
        exit(1)
    print(f"Connected: {res.json()['cluster_name']}: {res.json()['version']['number']}")

def deploy():
    # Create inference endpoints
    es.put_if_not_exists("/_inference/text_embedding/e5-small-endpoint", file="requests/inference_e5_small.json")

    # Create index templates
    es.put("/_index_template/dataset_wikipedia_template_ja", file="requests/index_template_wikipedia_ja.json")

    # Create searh applications
    es.put("/_application/search_application/my-app", file="requests/search_application.json")

def validate():
    pass

def setup():
    print("Setting up...")
    
    # Connectivity check
    es_connectivity_test()

    # clean()

    deploy()
    
    print("Setup complete")

if __name__ == "__main__":
    setup()