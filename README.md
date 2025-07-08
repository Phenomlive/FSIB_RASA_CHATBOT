

# FSIB Rasa Chatbot

A conversational AI chatbot built using the Rasa framework, designed to handle banking-related queries such as account balance, transactions, and customer support for the First Security Islami Bank (FSIB).

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## About
The FSIB Rasa Chatbot is an open-source project leveraging the Rasa framework to create a contextual AI assistant for banking services. It uses natural language understanding (NLU) and dialogue management to provide meaningful responses to user queries related to banking operations, such as checking account balances, transaction history, and customer support. The chatbot is designed to be scalable and customizable for integration with various platforms.

## Features
- **NLU Capabilities**: Understands user intents and entities for accurate query processing.
- **Custom Actions**: Supports API calls and database queries for dynamic responses (e.g., fetching account details).
- **Web Integration**: Includes a web widget for seamless deployment on websites using SocketIO.
- **Extensible**: Easily customizable for additional banking features or integration with other channels like Slack or Telegram.

## Installation
Follow these steps to set up the FSIB Rasa Chatbot locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Phenomlive/FSIB_RASA_CHATBOT.git
   cd FSIB_RASA_CHATBOT
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.8 or 3.9 installed. Then, install the required packages:
   ```bash
   pip install rasa==3.6.0
   pip install -r requirements.txt
   ```

4. **Install Additional Dependencies**:
   For TensorFlow and other dependencies:
   ```bash
   pip install ujson tensorflow
   ```

5. **Train the Model**:
   Initialize and train the Rasa model:
   ```bash
   rasa init
   rasa train
   ```

## Usage
1. **Run the Rasa Server**:
   Start the Rasa server with the trained model:
   ```bash
   rasa run --enable-api --cors "*" --debug
   ```

2. **Run the Action Server**:
   In a separate terminal, start the action server for custom actions:
   ```bash
   rasa run actions
   ```

3. **Interact via Command Line**:
   Test the chatbot in the terminal:
   ```bash
   rasa shell
   ```

4. **Testing API Integration**:
   Test the chatbot’s REST API:
   ```bash
   curl -XPOST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user1", "message": "Check my account balance"}' -H "Content-type: application/json"
   ```

## Project Structure
- `data/nlu.yml`: Defines intents and entities for user queries (e.g., `check_balance`, `transfer_money`).
- `data/stories.yml`: Contains sample conversation flows for dialogue management.
- `data/rules.yml`: Specifies rule-based conversation paths.
- `domain.yml`: Lists intents, entities, responses, and actions.
- `actions/actions.py`: Custom actions for API calls or database queries.
- `credentials.yml`: Configuration for channel integrations (e.g., SocketIO).
- `endpoints.yml`: Defines endpoints for action servers and external services.
- `models/`: Stores trained Rasa models.
- `index.html`: Sample web interface for the chatbot widget.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Create a pull request.

Please follow the Rasa contribution guidelines for code formatting (using `black`) and testing.[](https://github.com/RasaHQ/rasa)

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

