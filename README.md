# IntelliBot - AI Chat Bot

## Overview
IntelliBot is an AI-powered chat bot developed using Python. It integrates speech recognition and text-to-speech functionalities, allowing for seamless interaction through voice commands. The bot can respond to queries using OpenAI's GPT-3.5-turbo model and can perform various tasks like opening websites, playing music, telling the time, and saving responses to queries in text files.

## Features
- **Voice Recognition**: Converts spoken words into text using Google's Speech Recognition API.
- **Text-to-Speech**: Uses the `pyttsx3` library to convert text responses into speech.
- **Web Interaction**: Can open specified websites on command.
- **Time Announcement**: Tells the current time.
- **Chat History**: Maintains a log of the conversation.
- **File Creation**: Saves responses to queries involving artificial intelligence into text files.
- **Voice Command**: Executes various commands based on user input.

## Prerequisites
- Python 3.6 or later
- `speech_recognition` library
- `pyttsx3` library
- `openai` library
- `numpy` library
- A valid OpenAI API key

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/intellibot.git
   cd intellibot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your OpenAI API Key**
   Open the `config.py` file and add your OpenAI API key:
   ```python
   apikey = "your-openai-api-key"
   ```

## Usage
1. **Run the Bot**
   ```bash
   python main.py
   ```

2. **Interact with IntelliBot**
   - **Voice Commands**: Speak into the microphone to interact with IntelliBot.
   - **Open Websites**: Say "open YouTube" or "open Google" to launch the respective website.
   - **Play Music**: Say "open music" to play a predefined music file.
   - **Check Time**: Say "the time" to hear the current time.
   - **Use AI for Queries**: Include "using artificial intelligence" in your query to save the response in a text file.
   - **End Interaction**: Say "quit" to exit the program.

## File Structure
- `main.py`: Main script to run the IntelliBot.
- `config.py`: Configuration file to store the OpenAI API key.
- `openaitest.py`: Script to test OpenAI integration.

## Example Commands
- **Open Website**: "open YouTube"
- **Play Music**: "open music"
- **Check Time**: "the time"
- **AI Query**: "Explain quantum computing using artificial intelligence"
- **End Interaction**: "quit"
- **Reset Chat**: "reset chat"

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact
For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer at chandresh00rajpoot@gmail.com
