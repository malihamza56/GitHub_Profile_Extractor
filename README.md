# 🚀 GitHub Profile Extractor

A professional **GitHub Profile Extractor** built with **Python** and **Playwright** that automatically visits any public GitHub profile, extracts useful information, and exports the data into multiple formats.

The project follows a clean modular architecture with separate modules for browser management, navigation, extraction, exporting, logging, and screenshots.

---

# ✨ Features

## 👤 Profile Information

Extracts:

* Full Name
* Username
* Bio
* Profile Picture URL
* Email (if public)
* Social Links (if public)
* Followers Count
* Following Count

---

## 📂 Repository Information

Extracts every public repository including:

* Repository Title
* Description
* Visibility
* Programming Language

Also provides:

* Total Repository Count

---

## 📸 Automatic Screenshot

Captures a **full-page screenshot** of the GitHub profile for documentation and verification.

---

## 📄 Export Formats

The extracted data is exported into:

* JSON
* CSV

---

## 📜 Logging System

A professional logging system records:

* Browser Launch
* Navigation
* Data Extraction
* Export Status
* Errors
* Browser Closing

All logs are stored inside:

```text
logs/github_extractor.log
```

---

# 🏗️ Project Structure

```text
GitHub_Profile_Extractor/

│
├── browser.py          # Browser management
├── navigator.py        # Profile navigation
├── extractor.py        # Data extraction
├── exporter.py         # JSON & CSV export
├── screenshot.py       # Full page screenshots
├── config.py           # Project configuration
├── logger.py           # Logging configuration
├── main.py             # Main workflow
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

* Python 3
* Playwright
* Pandas
* Logging
* JSON
* CSV

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/GitHub_Profile_Extractor.git
```

Move into the project:

```bash
cd GitHub_Profile_Extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install
```

---

# ▶️ Usage

Run the project:

```bash
python main.py
```

Enter any GitHub username:

```text
Enter Your GitHub Username:

malihamza56
```

The extractor will automatically:

* Launch Browser
* Visit Profile
* Extract Data
* Save JSON
* Save CSV
* Capture Screenshot
* Generate Logs

---

# 📦 Sample JSON Output

```json
{
    "name": "CodeWithAli",
    "username": "malihamza56",
    "followers": "0",
    "following": "1"
}
```

---

# 📌 Current Features

* Modular Architecture
* Browser Automation
* Automatic Navigation
* Profile Extraction
* Repository Extraction
* JSON Export
* CSV Export
* Screenshot Capture
* Logging
* Error Handling

---

# 🚀 Future Improvements

Planned features for upcoming versions:

* Excel Export (.xlsx)
* Repository Stars
* Fork Count
* License Information
* Repository Topics
* Last Updated Date
* Pinned Repositories
* Contribution Statistics
* Organization Details
* Company
* Location
* Website
* CLI Arguments

Example:

```bash
python main.py malihamza56
```

instead of interactive input.

Additional plans:

* Multi-threaded Extraction
* Progress Bar
* Configuration File
* Docker Support
* GitHub API Integration
* Unit Testing
* Automated CI/CD Pipeline

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

* Browser Automation
* Web Scraping
* Playwright
* Python Project Structure
* Error Handling
* Logging
* Data Processing
* JSON Handling
* CSV Export
* Modular Programming

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Muhammad Ali Hamza**

Python Developer • Computer Science Student

Building real-world Python projects focused on:

* Automation
* Web Scraping
* APIs
* AI
* Open Source

⭐ If you found this project useful, consider giving it a star!
