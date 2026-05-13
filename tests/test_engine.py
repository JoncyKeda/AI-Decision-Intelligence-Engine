from app.decision_engine import DecisionEngine

def test_decision_engine():

    engine = DecisionEngine()

    scenario = {
        "marketing_budget": 20,
        "product_price": 10,
        "employee_count": 5
    }

    result = engine.evaluate_decision(
        scenario
    )

    assert "Risk Level" in result
