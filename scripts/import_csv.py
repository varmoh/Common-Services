import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL of the webpage with file links
WEBPAGE_URL = "https://www.emta.ee/ariklient/amet-uudised-ja-kontakt/uudised-pressiinfo-statistika/statistika-ja-avaandmed"
# Directory to save the downloaded file
DOWNLOAD_DIR = "./services/companies/unprocessed"  # Updated directory path
# File to store the last downloaded file URL
LAST_FILE_URL_FILE = "./last_file_url.txt"  # Local file for testing
# List of search terms
SEARCH_TERMS = ['tasutud_maksud']  # Add more terms as needed

def get_last_file_url(file_path):
    """Retrieve the URL of the last downloaded file from the given file path."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read().strip()
    return None

def set_last_file_url(file_path, file_url):
    """Store the URL of the last downloaded file in the given file path."""
    with open(file_path, 'w') as f:
        f.write(file_url)

def download_file(url, download_path):
    """Download a file from the given URL to the specified path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        logging.info(f"File downloaded successfully: {download_path}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download file: {e}")
        return False

def scrape_for_latest_csv_url(webpage_url, year, search_terms):
    """Scrape the webpage for the latest CSV file URL containing the given year and any of the search terms."""
    try:
        response = requests.get(webpage_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        csv_files = []

        for link in links:
            href = link['href']
            if (href.lower().endswith('.csv') and 
                str(year) in href and 
                any(term in href for term in search_terms)):
                file_url = urljoin(webpage_url, href)
                csv_files.append(file_url)
        
        if not csv_files:
            logging.info(f"No CSV files containing '{year}' and any of the search terms found.")
            return None
        
        # Improved logic: Prioritize files based on search terms and filename
        csv_files.sort(key=lambda x: (
            any(term in x for term in search_terms),  # Prioritize files with search terms
            os.path.basename(x)  # Secondary sort by filename (e.g., date/version)
        ), reverse=True)
        
        logging.info(f"Found CSV files: {csv_files}")
        return csv_files[0] if csv_files else None
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve the webpage: {e}")
        return None

def main():
    # Ensure the directory exists
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    
    # Get the current year
    current_year = datetime.now().year
    logging.info(f"Current year: {current_year}")

    last_file_url = get_last_file_url(LAST_FILE_URL_FILE)
    logging.info(f"Last file URL: {last_file_url}")

    new_file_url = scrape_for_latest_csv_url(WEBPAGE_URL, current_year, SEARCH_TERMS)
    
    if new_file_url:
        logging.info(f"New file URL: {new_file_url}")
        if new_file_url == last_file_url:
            logging.info("The latest CSV file is already downloaded. All is up to date.")
        else:
            download_path = os.path.join(DOWNLOAD_DIR, os.path.basename(new_file_url))
            if download_file(new_file_url, download_path):
                set_last_file_url(LAST_FILE_URL_FILE, new_file_url)
                logging.info(f"Downloaded new file: {new_file_url}")
    else:
        logging.info(f"No new CSV file containing '{current_year}' and any of the search terms found.")

if __name__ == "__main__":
    main()
