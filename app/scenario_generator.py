class ScenarioGenerator:

    def generate(
        self,
        marketing_budget,
        product_price,
        employee_count
    ):

        return {
            "marketing_budget": marketing_budget,
            "product_price": product_price,
            "employee_count": employee_count
        }
