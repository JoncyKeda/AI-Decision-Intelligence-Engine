from app.simulation_engine import SimulationEngine
from app.risk_analyzer import RiskAnalyzer
from app.explainability import ExplainabilityEngine
from app.utils import generate_confidence_score

class DecisionEngine:

    def __init__(self):

        self.simulator = SimulationEngine()

        self.risk_analyzer = RiskAnalyzer()

        self.explainer = ExplainabilityEngine()

    def evaluate_decision(self, scenario):

        revenue_growth = self.simulator.simulate(
            scenario
        )

        risk = self.risk_analyzer.calculate_risk(
            scenario
        )

        explanations = self.explainer.explain(
            scenario
        )

        confidence = generate_confidence_score()

        return {
            "Predicted Revenue Growth (%)": revenue_growth,
            "Risk Level": risk,
            "Confidence Score": confidence,
            "Explanations": explanations
        }
