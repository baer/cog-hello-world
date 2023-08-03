from cog import BasePredictor, Input


class Predictor(BasePredictor):
    def predict(self, text: str = Input(description="Text to print")) -> str:
        return text
