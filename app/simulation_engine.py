class SimulationEngine:

    def simulate(self, scenario):

        revenue_growth = (
            scenario["marketing_budget"] * 0.5
            - scenario["product_price"] * 0.2
            + scenario["employee_count"] * 0.3
        )

        return round(revenue_growth, 2)
