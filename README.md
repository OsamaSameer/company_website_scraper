# Company Website Scraper

This Python script fetches company websites from the Google Custom Search API and saves the results to a CSV file. It incorporates basic rate limiting to handle potential API usage limits.

**Key Features:**

*   Fetches company websites using the Google Custom Search API.
*   Handles 429 (Too Many Requests) errors with basic rate limiting.
*   Reads company names from a CSV file.
*   Saves the extracted websites to a new CSV file.

**Installation**

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```

2.  **Install dependencies:**
    ```bash
    cd company_website_scraper
    pip install -r requirements.txt 
    ```

**Usage**

1.  **Prepare the input file:** Create a CSV file named "Companies.csv" with a single column named "Company Name" containing the list of companies.
2.  **Replace placeholders:** 
    *   Open the `scraper.py` file and replace:
        *   `YOUR_API_KEY` with your actual Google Cloud API Key.
        *   `YOUR_SEARCH_ENGINE_ID` with your actual Google Custom Search Engine ID.
3.  **Run the script:**
    ```bash
    python scraper.py
    ```

**Output**

The script will create a new CSV file named "company_websites.csv" with two columns: "Company Name" and "Company Website".

**Configuration**

*   **API Key:** Replace the placeholder in `scraper.py` with your actual Google Cloud API Key.
*   **Search Engine ID:** Replace the placeholder in `scraper.py` with your actual Google Custom Search Engine ID.
*   **Rate Limiting:** Adjust the `time.sleep()` duration in the `get_company_website` function to fine-tune the rate limiting behavior.

**API Usage**

This script utilizes the Google Custom Search API. Please refer to the API documentation for usage limits and terms of service: [Link to Google Custom Search API Documentation]

**License**

This project is licensed under the MIT License - see the LICENSE file for details.

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

**Disclaimer:**

This script is provided for educational and experimental purposes. Use it responsibly and within the limits of the Google Custom Search API's terms of service. 

**Note:**

This enhanced README provides more context, clarifies the purpose of the script, and includes a more detailed explanation of usage and configuration. 

I hope this improved version is helpful!
