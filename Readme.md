## Setting Up the Environment

Follow these steps to set up your Python virtual environment and install the necessary dependencies:

1. **Create a Virtual Environment**:
    Run the following command to create a Python virtual environment named `CopaAgents`:

    ```sh
    python3 -m venv CopaAgents
    ```

2. **Activate the Virtual Environment**:
    Once the environment is created, activate it by running:

    ```sh
    source CopaAgents/bin/activate
    ```

3. **Install Dependencies**:
    Install all required dependencies listed in the `requirements.txt` file by running:

    ```sh
    pip install -r requirements.txt
    ```

    Alternatively, you can install the dependencies individually:

    ```sh
    pip install langgraph langchain openai langchain_openai langchain_community pyowm crewai
    ```

## Setting Up the Credentials

To run the application correctly, you need to set up your OpenAI API key. Follow these steps to add your API key to the environment:

1. **Add API Key to `iNode.py`**:
    Open the file `app/Nodes/iNode.py` and add your OpenAI API key:

    ```python
    import os
    os.environ['OPENAI_API_KEY'] = "your-openai-api-key"
    ```

    Replace `"your-openai-api-key"` with your actual OpenAI API key.

2. **Run the Application**:
    Execute the following command to start the application:

    ```sh
    python api.py
    ```

This will set the `OPENAI_API_KEY` environment variable required for the application to function properly and start the application.
