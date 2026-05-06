# Nova - AI Chatbot

Nova is a simple yet powerful AI chatbot powered by OpenAI's GPT-3.5-turbo model. Have natural conversations with an intelligent assistant!

## Features

✨ **Intelligent Conversations** - Chat naturally with an AI powered by OpenAI

💬 **Conversation Memory** - Nova remembers your conversation history within a session

⚡ **Easy to Use** - Simple command-line interface

🔐 **Secure** - Your API key stays private in a `.env` file

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (free trial available)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Karasamir2013/Nova.git
cd Nova
```

### Step 2: Get Your OpenAI API Key

1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key

### Step 3: Create `.env` File

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in a text editor and replace `your_api_key_here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-proj-your_actual_key_here
   ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

If you're on Mac or Linux and `pip` doesn't work, try:
```bash
pip3 install -r requirements.txt
```

### Step 5: Run Nova!

```bash
python chatbot.py
```

Or on Mac/Linux:
```bash
python3 chatbot.py
```

## Usage

Once Nova starts, you can:

- **Ask questions**: "What is Python?"
- **Have conversations**: "Tell me about machine learning"
- **Get help**: "How do I learn to code?"
- **Quit**: Type `quit` or `exit` to stop chatting

## Example

```
==================================================
Welcome to Nova - Your AI Chatbot!
==================================================
Type 'quit' or 'exit' to end the conversation
==================================================

You: Hello Nova!

Nova: Hello! I'm Nova, your AI assistant. How can I help you today?

You: What can you do?

Nova: I can help you with a wide range of tasks including...

You: exit

Nova: Goodbye! Thanks for chatting with me!
```

## Troubleshooting

### Error: "command not found: pip"
- Use `pip3` instead of `pip`

### Error: "Could not open requirements file"
- Make sure you're in the Nova folder
- Check that `requirements.txt` exists in the folder

### Error: "No module named 'openai'"
- Run `pip3 install -r requirements.txt` again

### Error: "OPENAI_API_KEY not found"
- Make sure your `.env` file exists and has your API key
- Check that the file is named `.env` (not `.env.txt`)

## Technologies Used

- **Python 3** - Programming language
- **OpenAI API** - AI model (GPT-3.5-turbo)
- **python-dotenv** - Environment variable management

## Cost

OpenAI API usage is not free, but they offer:
- **$5 free trial credit** for new users (expires after 3 months)
- **Pay as you go** - Typically a few cents per conversation

Check [OpenAI Pricing](https://openai.com/pricing) for current rates.

## License

This project is open source and available under the MIT License.

## Author

Created by Karasamir2013

## Support

If you encounter issues:

1. Check the Troubleshooting section above
2. Make sure your API key is valid
3. Ensure all dependencies are installed
4. Check that Python 3.7+ is installed

---

**Happy chatting with Nova! 🚀**
