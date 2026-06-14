# URL Safety Analyzer

## Project Overview

This project analyzes URLs and determines whether they are:

- Safe
- Suspicious
- Dangerous

The application checks different URL characteristics such as:

- HTTPS usage
- IP addresses in URLs
- Suspicious keywords
- URL length
- Number of subdomains
- Special characters

and then generates a risk score with explanations.

---

## Technologies Used

- Python 3.11+
- Tkinter (GUI)
- UV Package Manager

---

## Project Structure

```text
QR-PROJECT/

├── analyzer.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## Setup Instructions

### 1. Install UV

Open PowerShell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```powershell
uv --version
```
```
if does not show version then restart the terminal or PC 
```

---

### 2. Move to Project Folder

```powershell
cd QR-PROJECT
```

---

### 3. Create Virtual Environment

```powershell
uv venv
```

---

### 4. Activate Virtual Environment

```powershell
.venv\Scripts\activate
```

You should now see:

```text
(.venv)
```

at the beginning of your terminal line.

---

### 5. Install Dependencies

```powershell
uv sync
```

---

### 6. Run the Application

```powershell
uv run python main.py
```

---

## How to Use

1. Launch the application.
2. Enter a URL.
3. Click **Analyze URL**.
4. View:
   - Verdict
   - Risk Score
   - Security Reasons

---

## Example

Input:

```text
http://192.168.1.1/login/verify/account
```

Output:

```text
Verdict: DANGEROUS

Risk Score: 40/100

Reasons:
- URL is not using HTTPS
- Using IP address instead of domain name
- Contains suspicious words: login, verify
```

---

## Future Improvements

- VirusTotal API Integration
- Google Safe Browsing API
- WHOIS Lookup
- SSL Certificate Validation
- Machine Learning Detection
- Scan History Database
- PDF Report Generation

---

## Author

Cybersecurity Mini Project using Python.