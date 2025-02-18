from flask import Flask, request, jsonify
from flask_cors import CORS
from Tools.costOfLiving import get_city_cost_data
from Tools.netIncome import calculate_net_income
from Tools.walkScore import get_walk_scores
from Tools.populationData import get_population_data
from Tools.finalScore import finalScore

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get-location-data', methods=['POST'])
def get_location_data():
    try:
        data = request.json
        print("Received Data:", data)  # Debugging: Print received data

        country = data.get('country')
        province = data.get('province')
        city = data.get('city')
        income = data.get('income')
        checkboxes = data.get('checkboxes', {})

        if not all([country, province, city, income]):
            return jsonify({"error": "Missing required fields"}), 400
        scores = get_walk_scores(country, province, city)
        population_data = get_population_data(city, country, province)
        city_data = get_city_cost_data(city)
        

        result = {
            'walk_scores': scores,
            'population_data': population_data,
            'city_data': city_data
        }

        if country == "CA" or country == "Canada":
            net_income = calculate_net_income(float(income), province.capitalize())
            result['net_income'] = net_income
        else:
            net_income = None

        print(income)
        print(net_income)
        result['final_score'] = finalScore(checkboxes, scores, population_data, city_data, net_income,income)



        return jsonify(result)
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)