

# EmailSparkAI
AI Email Generation Tool - live link - https://email-spark-ai.streamlit.app/

![Python](https://img.shields.io/badge/python-v3.10-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-v3.5-blue)
![LangChain](https://img.shields.io/badge/LangChain-Icon-green)
![Streamlit](https://img.shields.io/badge/streamlit-v1.0.0-green)

This Streamlit application generates various types of emails with different styles such as formal, appreciating, not satisfied, neutral. It uses the OpenAI GPT-3.5 Turbo model to generate email content based on user inputs.
## Features

- **Email Types**: Provides templates for different types of job-related emails.
- **Customization**: Allows users to input the email topic, sender name, recipient name, writing style, and signature.
- **Interactive Interface**: Provides an interactive user interface for easy email generation.
- **Response Generation**: Uses the OpenAI GPT-3.5 Turbo model to generate responses based on user inputs.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your environment**:

   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:

     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

2. **Use the application**:

   - Enter the email topic, sender name, recipient name, writing style, and signature.
   - Click the "Generate" button to generate the email response.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to open a pull request or an issue.

## License

This project is licensed under the MIT License.
