import ollama


class AIInsights:

    @staticmethod
    def generate(df):

        sample = df.head(20).to_string()

        prompt = f"""
        You are a Senior Data Scientist.

        Analyze this dataset sample.

        {sample}

        Provide:

        1. Dataset overview
        2. Missing value observations
        3. Potential correlations
        4. Data quality issues
        5. ML suggestions

        Keep it concise and practical.
        """

        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]