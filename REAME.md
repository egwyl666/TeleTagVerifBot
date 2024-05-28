# TeleTagVerifBot

TeleTagVerifBot is an asynchronous Telegram bot designed to verify the existence of user tags within the Telegram environment. It utilizes the Telethon library to interact with the Telegram API efficiently.

## Features

- **Asynchronous Tag Checking**: Utilizes asynchronous programming to check multiple tags without blocking operations, improving performance.
- **Versatile Tag Input**: The bot can handle various types of identifiers including Telegram user IDs (e.g., `id123123`), usernames (e.g., `nickname`), or phone numbers (e.g., `+12300000000`).
- **Logging**: Comprehensive logging for monitoring the tag verification process and debugging.
- **Configurable**: Uses external configuration for API credentials, enhancing security and flexibility.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the bot, you need to install Python 3.6+ and set up a Telegram API key. Also, make sure you have `pip` installed to handle Python dependencies.

### Installing

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/TeleTagVerifBot.git
   cd TeleTagVerifBot
    ```

2. **Install the required packages**

    ```python
    pip install -r requirements.txt
    ```

3. **Configure your API credentials in `config.json`**

   ```json
    {
    "api_id": "your_api_id",
    "api_hash": "your_api_hash",
    "phone_number": "your_phone_number"
    }
    ```

**Replace your_api_id, your_api_hash, and your_phone_number with your actual Telegram API credentials.**

### Usage
**To run the bot, execute:**

```python
python3 CheckerBot.py
```
```The bot will start, and it will begin checking tags based on the list provided in startcheck.txt. It can accept user IDs, usernames, or phone numbers as input formats.```

# Contributing

### **Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.**

> Fork the Project
> 
> Create your Feature Branch (git checkout -b feature/AmazingFeature)
> 
> Commit your Changes (git commit -m 'Add some AmazingFeature')
> 
> Push to the Branch (git push origin feature/AmazingFeature)
> 
> Open a Pull Request

# License
This project is licensed under the [MIT License](https://github.com/egwyl666/TeleTagVerifBot?tab=MIT-1-ov-file) - see the LICENSE.md file for details.

# Acknowledgments

+ Thanks to the Telethon library for making Telegram bot development easier.