import requests

def get_protein_details(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        protein_name = data.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "N/A")
        organism = data.get("organism", {}).get("scientificName", "N/A")
        sequence = data.get("sequence", {}).get("value", "N/A")
        length = data.get("sequence", {}).get("length", "N/A")

        print(f"Protein Name: {protein_name}")
        print(f"Organism: {organism}")
        print(f"Sequence Length: {length}")
        print(f"Sequence: {sequence}")
    else:
        print(f"Failed to retrieve data for {uniprot_id}. Status code: {response.status_code}")

# Example usage
get_protein_details("A0A0K8P6T7")
