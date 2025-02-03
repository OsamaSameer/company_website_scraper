import requests
import pandas as pd
import time
import random

# Replace with your actual Google API Key and Search Engine ID
API_KEY = "YOUR_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

def get_company_website(company_name):
    """
    Fetches the company website from the Google Custom Search API with basic rate limiting.

    Args:
        company_name (str): The name of the company to search for.

    Returns:
        str: The company website URL, "Not Found", "API Error", or "Request Failed".
    """
    search_url = f"https://www.googleapis.com/customsearch/v1?q={company_name} official company website&key={API_KEY}&cx={SEARCH_ENGINE_ID}"

    while True:
        try:
            response = requests.get(search_url)
            response_data = response.json()

            if response.status_code == 200:
                if "items" in response_data:
                    website = response_data["items"][0].get("link", "Not Found")
                    print(f"✅ Found: {company_name} → {website}")
                    return website
                else:
                    print(f"❌ No website found for: {company_name}")
                    return "Not Found"
            elif response.status_code == 429:  # Handle 429 Too Many Requests
                print(f"⚠ Rate Limit Exceeded. Waiting for {random.uniform(5, 10)} seconds.")
                time.sleep(random.uniform(5, 10))  # Wait for a random interval
            else:
                print(f"⚠ API Error: {response.status_code} - {response_data}")
                return "API Error"

        except requests.exceptions.RequestException as e:
            print(f"⚠ Request Failed: {e}")
            return "Request Failed"

if __name__ == "__main__":
    # Load and clean CSV
    input_file = "Companies.csv"
    df = pd.read_csv(input_file)
    df.columns = df.columns.str.strip()

    # Check if 'Company Name' exists
    if "Company Name" not in df.columns:
        print("❌ Column 'Company Name' not found! Please check your CSV headers.")
        print("📌 Available columns:", df.columns)
        exit()

    # Apply function to get websites
    df["Company Website"] = df["Company Name"].apply(get_company_website)

    # Save results to CSV
    output_file = "company_websites.csv"
    df.to_csv(output_file, index=False)

    print(f"✅ Scraping complete! Results saved in {output_file}")