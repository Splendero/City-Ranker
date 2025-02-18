# City Ranker
This tools has a series of metrics that rank and inputted city.
## Inputs
- Bike Score
- Walk Score
- Transit Score
- Annual Growth Rate
- Cost of Living Index
- Cost of Living Plus Rent Index
- Groceries Index
- Local Purchasing Power Index
- Rent Index
- Restaurant Price Index
- Transit Score
- Walk Score
- Net Income
### Final Score Calculation Breakdown

The final score is calculated by averaging points from selected factors (via checkboxes). Here's how each factor contributes:

#### 1. **Bike Score / Transit Score / Walk Score**  
- **Score ≥ 85**: +100 points  
- **Score < 85**: +Raw score value (e.g., 70 → +70)  

---

#### 2. **Annual Growth Rate**  
- **Negative or 0–2%**: +50 points  
- **2–10%**: +75 points  
- **≥10%**: +100 points  

---

#### 3. **Cost Indices** (Cost of Living, Rent, Groceries, etc.)  
- **Formula**: `4000 / Index Value`  
  - Higher costs (larger index values) reduce contributions.  
  - Example: If Cost of Living Index = 200 → `4000 / 200 = +20 points`.  

---

#### 4. **Net Income**  
- **Tax Rate**: `(1 - net_income/income) * 100`  
- **Formula**: `400 / sqrt(Tax Rate)`  
  - Higher tax rates (lower net income) reduce points.  

---

#### Final Calculation  
- **Total Points** = Sum of all selected factor contributions.  
- **Final Score** = `Total Points / Number of Selected Factors`, rounded down to the nearest integer.  
- **No Factors Selected**: Returns **0**.  
