## Goalie Stat Tracker

This Python script monitors goalie stats (goals and assists) from hockey-reference.com during the NHL playoffs.
If a change is detected (such as a goalie scoring a goal or getting an assist), the script sends a Pushover notification.

#### **Features**

    - Scrapes playoff goalie stats using BeautifulSoup

    - Detects changes in goals and assists

    - Sends push notifications using Pushover

    - Logs all detected changes and errors to a log file

    - Supports a test mode for simulating stat changes

#### Setup Instructions

##### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/goalie-tracker.git
cd goalie-tracker
```

###### **2. Set Up a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

##### **3. Install Required Packages**

```bash
pip install -r requirements.txt
```

##### **4. Configure Pushover Credentials**

Create a .env file in the project root and add your credentials:

```bash
PUSHOVER_USER_KEY=your_user_key_here
PUSHOVER_API_TOKEN=your_api_token_here
```

##### **5. Run the Script**

```bash
python main.py
```

**Optional**: Run in test mode to simulate a stat change:

```bash
python main.py --test
```
