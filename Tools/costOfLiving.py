import csv

def get_city_cost_data(city_name, file_path='numbeo_cost_of_living.csv'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Split CSV city entry into parts and compare first segment
                csv_city = row['City'].split(',')[0].strip().lower()
                input_city = city_name.strip().lower()
                
                if csv_city == input_city:
                    return dict(row)
            
            print(f"No data found for {city_name}")
            return None
            
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    city_data = get_city_cost_data(city)
    
    if city_data:
        print("\nCity Found!")
        print("--------------")
        print(f"Full Entry: {city_data['City']}")
        for key, value in city_data.items():
            if key != 'City':  # Already displayed
                print(f"{key}: {value}")