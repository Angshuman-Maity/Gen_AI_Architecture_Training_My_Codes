# Gen AI Architect Assignment - Real-Time Market Sentiment Analyzer

This project demonstrates how to use Azure OpenAI with LangChain and Langfuse to create a real-time market sentiment analyzer. It takes a company name as input, determines the corresponding stock ticker symbol using a GPT model, and sets up Langfuse tracing for observability.

## 🚀 Features

- Integrates with **Azure OpenAI** (`finance-gpt-v2`) to process financial prompts.
- Uses **LangChain** and **Langfuse** for prompt engineering and monitoring.
- Retrieves company stock ticker based on user input.
- Designed as part of a **Gen AI Architect Assignment**.

## 🛠️ Requirements

- Python 3.8+
- Azure OpenAI access
- Langfuse account (for tracing and prompt management)

### Python Packages

Install required packages:

```bash
pip install langfuse langchain_openai langchain_community
```

## 🔐 Environment Setup

Set the following environment variables in your notebook or `.env` file:

```python
os.environ["AZURE_OPENAI_API_KEY"] = "<your_api_key>"
os.environ["AZURE_OPENAI_ENDPOINT"] = "<your_endpoint>"
os.environ["LANGFUSE_PUBLIC_KEY"] = "<your_public_key>"
os.environ["LANGFUSE_SECRET_KEY"] = "<your_secret_key>"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"
```

## 🧠 How It Works

1. **Initialization**: Langfuse is initialized for prompt management and observability.
2. **User Input**: You provide a company name (e.g., `Apple`, `Meta`).
3. **Prompt Creation**: A prompt is generated to retrieve the company's stock ticker.
4. **Model Interaction**: Azure OpenAI's `finance-gpt-v2` processes the request.
5. **Monitoring**: Langfuse tracks the prompt and model interaction.

## 📂 File Structure

- `Gen_AI_Architect_Assignment_01.ipynb`: Main notebook implementing the flow.

## 📌 Notes

- Do **not** expose your API keys in the notebook. Use environment variables securely.
- You must have access to Azure OpenAI resources to use `finance-gpt-v2`.

## 📄 License

This project is for educational/demo purposes only. Do not distribute without permission.
