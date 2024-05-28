import asyncio
from telethon.sync import TelegramClient
from telethon.errors import UsernameInvalidError
import logging
import json

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your values
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    api_id = config['api_id']
    api_hash = config['api_hash']
    phone_number = config['phone_number']

async def check_account_existence(client, username):
    try:
        user = await client.get_entity(username)
        logger.info(f"Tag {username} exists.")
        return True
    except ValueError as e:
        logger.error(f"Error checking tag {username}: {e}")
        return False
    except UsernameInvalidError as e:
        logger.warning(f"Exception while checking tag {username}: {e}")
        return False

async def main():
    # Initialization and connection to the Telegram server
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    with open('./startcheck.txt', 'r') as file:
        existing_tags = [line.strip() for line in file]

    new_tags = []
    for tag in existing_tags:
        logger.info(f'Checking tag: {tag}')
        try:
            if await check_account_existence(client, tag):
                logger.info(f'Tag {tag} passed verification and exists.')
                new_tags.append(tag)
            else:
                logger.info(f'Tag {tag} does not exist.')
        except Exception as e:
            logger.error(f"An error occurred while checking tag {tag}: {e}")

        await asyncio.sleep(5)  # Adding a 5-second delay

    # Ending work and closing session
    await client.disconnect()

    with open('./sorted.txt', 'w') as file:
        file.write('\n'.join(new_tags))

if __name__ == '__main__':
    # Start the asynchronous event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
