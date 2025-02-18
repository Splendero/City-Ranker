from Tools.costOfLiving import get_city_cost_data
from Tools.netIncome import calculate_net_income
from Tools.walkScore import get_walk_scores
from Tools.populationData import get_population_data

def get_location_data(country, province, city, income):
    """Get all the required data based on user input."""
    data = {}

    # Get Walk Score data
    scores = get_walk_scores(country, province, city)
    if scores:
        data["walk_scores"] = scores
    
    # Get Population data
    population_data = get_population_data(city, country, province)
    if population_data:
        data["population_data"] = population_data
    
    # Cost of Living Data
    city_data = get_city_cost_data(city)
    if city_data:
        data["city_data"] = city_data

    # Net income data for Canada
    if country == "CA":
        net_income = calculate_net_income(int(income), province.capitalize())
        data["net_income"] = net_income
    
    return data
