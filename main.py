from wikipedia_scraper import WikipediaScraper

def main():
    # Create an instance of the WikipediaScraper
    scraper = WikipediaScraper()

    
    try:
        countries = scraper.get_countries()
        print("Supported countries:", countries)
    except Exception as e:
        print(e)
        return

   
    if countries:
        selected_country = countries[0]  # Get the first country in the list
        print(f"Fetching leaders for: {selected_country}")

        try:
            
            scraper.get_leaders(selected_country)
            print(f"Leaders data for {selected_country}:")
            print(scraper.leaders_data[selected_country])
        except Exception as e:
            print(e)
            return

        
        wikipedia_url = "https://en.wikipedia.org/wiki/Albert_Einstein"  # Example Wikipedia page
        first_paragraph = scraper.get_first_paragraph(wikipedia_url)
        print("First paragraph from Wikipedia:", first_paragraph)

        
        try:
            scraper.to_json_file(f"{selected_country}_leaders.json")
            print(f"Leaders data saved to {selected_country}_leaders.json")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
