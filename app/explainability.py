class ExplainabilityEngine:

    def explain(self, scenario):

        explanations = []

        if scenario["marketing_budget"] > 10:

            explanations.append(
                "Higher marketing budget may improve customer acquisition."
            )

        if scenario["product_price"] > 10:

            explanations.append(
                "Higher pricing may reduce customer retention."
            )

        if scenario["employee_count"] > 5:

            explanations.append(
                "More employees may improve operational efficiency."
            )

        return explanations
