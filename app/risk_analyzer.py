class RiskAnalyzer:

    def calculate_risk(self, scenario):

        risk_score = 0

        if scenario["product_price"] > 15:
            risk_score += 30

        if scenario["marketing_budget"] < 5:
            risk_score += 20

        if scenario["employee_count"] < 3:
            risk_score += 15

        if risk_score < 20:
            return "Low"

        elif risk_score < 50:
            return "Medium"

        return "High"
