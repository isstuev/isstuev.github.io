import json

def extract_explorer_urls():
    # Read the chains.json file
    with open('chains.json', 'r') as f:
        chains = json.load(f)
    
    # List to store all explorer URLs
    urls = []
    
    # Iterate through each chain
    for chain_id, chain_data in chains.items():
        # Check if the chain has explorers
        if 'explorers' in chain_data:
            # Add each explorer URL to the list
            for explorer in chain_data['explorers']:
                if 'url' in explorer:
                    urls.append(explorer['url'])
    
    # Write URLs to a file
    with open('explorer_urls.txt', 'w') as f:
        for url in urls:
            f.write(f"{url}\n")
    
    return urls

if __name__ == "__main__":
    urls = extract_explorer_urls()
    print(f"Extracted {len(urls)} explorer URLs to explorer_urls.txt") 