from bs4 import BeautifulSoup
import requests

def get_population_data(city, country,province):
    """Get population data from World Population Review"""
    formatted_city = city.lower().replace(' ', '-')
    formatted_provience = province.lower().replace(' ', '-')
    if(country == "US"):
        url = f"https://worldpopulationreview.com/us-cities/{formatted_provience}/{formatted_city}"
    if(country == "CA" or country == "Canada"):
         url = f"https://worldpopulationreview.com/canadian-cities/{formatted_city}-population"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract population - look for the specific div structure
        population_div = soup.find('div', class_='text-center text-4xl')
        population = population_div.get_text(strip=True) if population_div else 'N/A'
        
        # Extract growth rate - search in the content section
        content_div = soup.find('div', class_='content')
        growth_span = content_div.find('span', style='color:green') if content_div else None
        growth_rate = growth_span.get_text(strip=True) if growth_span else 'N/A'
        
        return {
            'Current Population': population,
            'Annual Growth Rate': growth_rate
        }
    
    except Exception as e:
        print(f"Error getting population data: {str(e)}")
        return None
