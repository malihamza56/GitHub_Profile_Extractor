# 🚀 GitHub Profile Extractor

A modern **GitHub Profile Extractor** built with **Python, Playwright, Pandas, and Streamlit**.

The application automatically visits public GitHub profiles, extracts useful profile and repository information, processes the collected data, and provides downloadable **JSON and CSV exports** through both a CLI workflow and a web-based interface.

> 🔎 **CLI + Web Interface • Browser Automation • Data Extraction • CSV/JSON Export**

---

## 🌐 Live Demo

🚀 **Web App:** `ADD_YOUR_STREAMLIT_APP_URL_HERE`

The web interface allows you to enter a GitHub username and extract public profile information directly from your browser.

---

## ✨ Features

### 👤 Profile Information

Extracts available public profile information including:

* Full Name
* Username
* Bio
* Profile Picture URL
* Public Email
* Public Social Links
* Followers
* Following

### 📂 Repository Information

Extracts public repositories and collects:

* Repository Name
* Description
* Visibility
* Programming Language
* Total Repository Count

### 📸 Automatic Screenshot

Automatically captures a **full-page screenshot** of the target GitHub profile for documentation and verification.

### 📄 Data Export

Collected data can be exported into:

* 📄 JSON
* 📊 CSV

The Streamlit interface also provides direct download buttons for the generated data.

### 📜 Logging System

A dedicated logging system records important application events such as:

* Browser Launch
* Profile Navigation
* Repository Navigation
* Data Extraction
* Export Status
* Errors
* Browser Closing

Logs are stored inside:

```text
logs/github_extractor.log
```

---

# 🖥️ Web Interface

The project includes a Streamlit-powered web interface.

### Workflow

```text
Enter GitHub Username
        ↓
Launch Browser
        ↓
Visit GitHub Profile
        ↓
Extract Profile Information
        ↓
Extract Repository Information
        ↓
Process Data
        ↓
Generate JSON / CSV
        ↓
Display Results
        ↓
Download Data
```

### Interface Features

* Clean modern UI
* Username input
* One-click extraction
* Extraction status
* Profile information display
* Repository table
* CSV download
* JSON download
* Screenshot preview

---

# 🏗️ Project Architecture

The project follows a modular architecture where each responsibility is separated into its own module.

```text
GitHub_Profile_Extractor/
│
├── app.py                # Streamlit web interface
├── main.py               # Main workflow controller
│
├── browser.py            # Browser management
├── navigator.py          # GitHub navigation
├── extractor.py          # Profile & repository extraction
├── exporter.py           # JSON & CSV export
├── screenshot.py         # Screenshot generation
├── config.py             # Project configuration
├── logger.py             # Logging configuration
│
├── outputs/
│   ├── json/
│   ├── csv/
│   └── screenshots/
│
├── logs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| 🐍 Python         | Core programming language |
| 🎭 Playwright     | Browser automation        |
| 📊 Pandas         | Data processing           |
| 🌐 Streamlit      | Web interface             |
| 📄 JSON           | Structured data export    |
| 📑 CSV            | Tabular data export       |
| 📝 Logging        | Application monitoring    |
| 🧩 Modular Python | Project architecture      |

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/malihamza56/GitHub_Profile_Extractor.git
```

Move into the project directory:

```bash
cd GitHub_Profile_Extractor
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright Browser

```bash
playwright install chromium
```

---

# ▶️ Usage

## 💻 CLI Mode

Run:

```bash
python main.py
```

Enter a GitHub username:

```text
Enter Your GitHub Profile Username: malihamza56
```

The application will:

```text
Launch Browser
      ↓
Visit Profile
      ↓
Visit Repositories
      ↓
Extract Information
      ↓
Build Profile Data
      ↓
Export JSON
      ↓
Export CSV
      ↓
Capture Screenshot
      ↓
Generate Logs
```

---

# 🌐 Web Application

Run the Streamlit interface:

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

Enter a GitHub username and click:

```text
🔍 Extract Profile
```

The extracted information will then be displayed through the web interface.

---

# 📦 Output

After a successful extraction, the project generates:

```text
outputs/
│
├── json/
│   └── profile.json
│
├── csv/
│   └── repositories.csv
│
└── screenshots/
    └── profile.png
```

---

# 📄 Example JSON

```json
{
    "name": "CodeWithAli",
    "username": "malihamza56",
    "followers": "0",
    "following": "1"
}
```

> The exact output depends on the public information available on the target GitHub profile.

---

# 🧠 How It Works

The extractor uses **Playwright** to automate a Chromium browser and navigate through GitHub.

```text
                 GitHub
                    │
                    ▼
             Playwright Browser
                    │
                    ▼
              Navigator Module
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Profile Page        Repository Pages
          │                   │
          └─────────┬─────────┘
                    ▼
             Extractor Module
                    │
                    ▼
             Profile Data
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
        JSON                 CSV
          │                   │
          └─────────┬─────────┘
                    ▼
              Streamlit UI
```

---

# 🧩 Modular Architecture

One of the main goals of this project is to keep the code maintainable and scalable.

### `browser.py`

Responsible for:

* Launching the browser
* Creating browser context
* Managing browser instances

### `navigator.py`

Responsible for:

* Opening GitHub profiles
* Navigating through repositories

### `extractor.py`

Responsible for:

* Extracting profile information
* Extracting statistics
* Extracting repository information
* Building structured profile data

### `exporter.py`

Responsible for:

* JSON generation
* CSV generation

### `screenshot.py`

Responsible for:

* Capturing full-page screenshots

### `logger.py`

Responsible for:

* Application logs
* Error logs
* Workflow tracking

### `main.py`

Acts as the central workflow controller.

### `app.py`

Provides the Streamlit-based web interface and connects the UI with the extraction workflow.

---

# 🔐 Data & Privacy

This project is designed to work with **publicly available GitHub profile information**.

It does not require a user's GitHub password or private account credentials.

Only information publicly accessible through the target profile is intended to be collected.

Users should use the project responsibly and respect GitHub's applicable terms, policies, and rate limits.

---

# 🚀 Future Improvements

Planned improvements include:

### 📊 More Repository Data

* ⭐ Repository Stars
* 🍴 Fork Count
* 📜 License Information
* 🏷️ Repository Topics
* 🕒 Last Updated Date
* 📌 Pinned Repositories

### 👤 More Profile Data

* 📍 Location
* 🏢 Company
* 🌐 Website
* 🏛️ Organizations
* 📈 Contribution Statistics

### 📦 Export Improvements

* Excel `.xlsx`
* Advanced CSV reports
* Downloadable profile reports

### ⚡ Performance

* Multi-threaded extraction
* Better loading indicators
* Progress tracking
* Caching

### 🛠️ Developer Improvements

* GitHub API integration
* Unit testing
* Docker support
* Configuration management
* Automated CI/CD pipeline

### 🖥️ CLI Improvements

Current:

```bash
python main.py
```

Future:

```bash
python main.py malihamza56
```

---

# 📚 Learning Objectives

This project demonstrates practical experience with:

* Python Programming
* Object-Oriented / Modular Project Structure
* Browser Automation
* Playwright
* Web Scraping
* Data Extraction
* Data Processing
* Pandas
* JSON
* CSV
* Logging
* Error Handling
* Streamlit
* Web Application Development
* Git & GitHub

---

# 🎯 Project Goals

The main goal of this project is to transform a simple Python scraping script into a **complete, modular, reusable data extraction application**.

It combines:

```text
Python
+
Browser Automation
+
Web Scraping
+
Data Processing
+
Exporting
+
Logging
+
Web UI
```

into a single practical project.

---

# 👨‍💻 Author

## Muhammad Ali Hamza

**Python Developer • Computer Science Student**

Interested in building practical projects focused on:

* 🐍 Python
* 🤖 Automation
* 🌐 Web Scraping
* 🔌 APIs
* 🧠 AI
* 💻 Software Development
* 🚀 Open Source

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ **Star** on GitHub.

Every star helps support the project and motivates further development. 🚀

---

# 📄 License

This project is licensed under the **MIT License**.
