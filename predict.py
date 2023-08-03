from cog import BasePredictor, Input


class Predictor(BasePredictor):
    def predict(
        self, text: str = Input(description="Text to print", default="Hello, World!")
    ) -> str:
        return text
