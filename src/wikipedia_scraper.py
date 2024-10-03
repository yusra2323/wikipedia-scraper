import requests
import json
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_url = "https://country-leaders.onrender.com/countries"
        self.leaders_url = "https://country-leaders.onrender.com/leaders"
        self.cookies_url = "https://country-leaders.onrender.com/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie() 

    def refresh_cookie(self):
        
        response = requests.get(f"{self.base_url}{self.cookies_url}")
        if response.status_code == 200:
            self.cookie = response.cookies
        else:
            raise Exception("Failed to refresh cookie")
        return self.cookie

    def get_countries(self):


 
        """
        Retrieves a list of supported countries from the API.
        """
        response = requests.get(f"{self.base_url}{self.country_url}", cookies=self.cookie)
        if response.status_code == 200:
            return response.json()  
        else:
            raise Exception("Failed to retrieve countries")

    def get_leaders(self, country):
        """
        Populates the leaders_data object with leaders for a specific country.
        """
        response = requests.get(f"{self.base_url}{self.leaders_url}/{country}", cookies=self.cookie)
        if response.status_code == 200:
            self.leaders_data[country] = response.json()  # Store the retrieved data in leaders_data
        else:
            raise Exception(f"Failed to retrieve leaders for {country}")

    def get_first_paragraph(self, wikipedia_url):
        """
        Retrieves the first meaningful paragraph from a Wikipedia URL.
        """
        print(wikipedia_url)  # Keep this for debugging purposes
        response = requests.get(wikipedia_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        paragraphs = soup.find_all('p')

        
        def is_valid_paragraph(p):
            text = p.get_text(strip=True)
            if not text or len(text) < 50:
                return False
            return True
        
        # Loop to find the first valid paragraph
        for p in paragraphs:
            if is_valid_paragraph(p):
                return p.get_text(strip=True)

        return None  # Return None if no valid paragraph is found

    def to_json_file(self, filepath):
       
        with open(filepath, 'w') as f:
            json.dump(self.leaders_data, f, indent=4)
