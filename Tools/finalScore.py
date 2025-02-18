import math

def finalScore(checkboxes, walk_scores, population_data, city_data, net_income,income):
    final_score = 0
    count = 0
    print(net_income)
    print(income)

    if checkboxes.get("Bike Score"):
        count += 1
        bike_score_value = int(walk_scores.get("Bike Score"))
        if bike_score_value >= 85:
            final_score += 100
        else:
            final_score += bike_score_value

    if checkboxes.get("Annual Growth Rate"):
        count += 1
        AGR = float(population_data.get("Annual Growth Rate").strip('%'))
        if AGR < 0:
            final_score += 50
        elif AGR >= 0 and AGR < 2:
            final_score += 50
        elif AGR >= 2 and AGR < 10:
            final_score += 75
        elif AGR >= 10:
            final_score += 100


    ## For the indexs we have 100 be set around New York City but since New York City is high
    ## we have set it to f(100)=4000/100 = 40 where we then steadly decay if higher and expontialy decrease if lower
    if checkboxes.get("Cost of Living Index"):
        count += 1
        final_score += 4000/float(city_data.get("Cost of Living Index")) 

    if checkboxes.get("Cost of Living Plus Rent Index"):
        count += 1
        final_score += 4000/float(city_data.get("Cost of Living Plus Rent Index"))

    if checkboxes.get("Groceries Index"):
        count += 1
        final_score += 4000/float(city_data.get("Groceries Index"))

    if checkboxes.get("Local Purchasing Power Index"):
        count += 1
        final_score += 4000/float(city_data.get("Groceries Index"))

    if checkboxes.get("Rent Index"):
        count += 1
        final_score += 4000/float(city_data.get("Rent Index"))

    if checkboxes.get("Restaurant Price Index"):
        count += 1
        final_score += 4000/float(city_data.get("Restaurant Price Index"))

    if checkboxes.get("Transit Score"):
        count += 1
        transit_score_value = int(walk_scores.get("Transit Score"))
        if transit_score_value >= 85:
            final_score += 100
        else:
            final_score += transit_score_value

    if checkboxes.get("Walk Score"):
        count += 1
        walk_score_value = int(walk_scores.get("Walk Score"))
        if walk_score_value >= 85:
            final_score += 100
        else:
            final_score += walk_score_value

    if checkboxes.get("Net Income"):
        count += 1
        tax_rate = (1-(float(net_income)/float(income)))*100
        final_score += int(400/(math.sqrt(float(tax_rate))))
    
    if count == 0:
        return 0
    
    return int(final_score/(count))