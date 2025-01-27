# Financial Disclosures Automation Tool

This project is an automated tool designed to download, extract, and analyze financial disclosure files from a public source, and notify important updates via Telegram.

## Features

1. **Automatic Download:**  
   Downloads a ZIP file containing financial disclosures from a predefined URL.

2. **Extraction and Analysis:**  
   Unzips the downloaded file, processes its content by analyzing XML files, and associates relevant information with members.

3. **Telegram Notifications:**  
   Sends a Telegram message to notify recent updates, avoiding duplicates using a tracking file (`output.txt`).

4. **Automatic Cleanup:**  
   Deletes downloaded and extracted files after each cycle to optimize disk space.

5. **Automated Cycle:**  
   Executes the process every 10 seconds to ensure data is always up to date.

---

## Prerequisites

### 1. Python
Make sure Python 3.7+ is installed on your machine.

### 2. Required Python Libraries
Install the dependencies using the following command:
```bash
pip install requests pyTelegramBotAPI schedule
```

---

## Project Structure

```plaintext
.
├── data/
│   ├── output.txt           # File to track already sent notifications
│   ├── 2024FD.xml           # Extracted XML file (temporary, deleted after execution)
│   ├── 2024.zip             # Downloaded ZIP file (temporary, deleted after execution)
├── main.py                  # Main script managing the automation cycle
├── Representative_Member.py # Handles members and associated files
├── read.py                  # Reads and processes the XML file
├── telegram.py              # Manages Telegram notifications
├── README.md                # Project documentation
```

---

## How to Run the Project?

1. Clone this repository to your working environment:
   ```bash
   git clone https://github.com/0eagledev0/analyse_Fondamentale_XMl.git
   cd analyse_Fondamentale_XMl
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

The script will run in a loop, automatically downloading, processing, and cleaning up files.

---

## Key Points

- **Telegram Configuration:**  
  In the `Representative_Member.py` file, replace the `API_TOKEN` and `CHAT_ID` with your Telegram bot information. Ensure your bot is properly set up and has access to the specified chat.

- **Security:**  
  Do not include sensitive information, such as the `API_TOKEN`, directly in the code. Use environment variables to handle sensitive data securely.

- **`output.txt` File:**  
  This file is used to track file IDs that have already been notified, ensuring no duplicate messages are sent.

---

## Possible Improvements

- Add a configuration file to customize the URL, time intervals, and other parameters.
- Handle network or download errors with retry mechanisms.
- Implement logging to track executions and errors.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.

---

## Disclaimer

This project is for educational or professional purposes. Ensure you have the necessary permissions to interact with the data being downloaded and sent via Telegram.
