from bs4 import BeautifulSoup
import requests
from Tools.provinceConverstion import abbreviate_location

def get_walk_scores(country, province, city):
    """Get walk, transit, and bike scores from Walk Score"""
    formatted_city = city.replace(' ', '_')
    url = (f"https://www.walkscore.com/CA-{abbreviate_location(province).upper()}/{formatted_city}" if country == 'CA' or country == 'Canada'
           else f"https://www.walkscore.com/{abbreviate_location(province).upper()}/{formatted_city}")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scores = {
            'Walk Score': 'N/A',
            'Transit Score': 'N/A',
            'Bike Score': 'N/A'
        }

        # Find score images
        imgs = soup.find_all('img', alt=lambda t: t and 'Score' in t)
        for img in imgs:
            alt = img['alt'].split()
            if len(alt) >= 3 and alt[2] == 'Score':
                score_type = f"{alt[1]} {alt[2]}"
                scores[score_type] = alt[0]
        
        return scores
    
    except Exception as e:
        print(f"Error getting scores: {str(e)}")
        return None
