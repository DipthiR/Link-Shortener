# Link-Shortener
# 🔗 URL Shortener using Python

This is a simple command-line URL shortener built with Python using the `pyshorteners` library. It uses the TinyURL service to convert long URLs into short and shareable ones.

---

## 🚀 Features

- Easy-to-use terminal interface
- Automatically fixes missing `https://` if needed
- Error handling for invalid or unreachable URLs
- Uses the reliable [TinyURL](https://tinyurl.com) shortening service

---

## 🧰 Requirements

- Python 3.6 or higher
- Internet connection
- `pyshorteners` library

---

## 📦 Installation

1. Clone the repository or download the `.py` file.

2. Install the required library:

```bash
pip install pyshorteners
```
## 💡 Usage
Run the script:

python Link-Shortener.py
Then enter a long URL like:

en.wikipedia.org/wiki/Artificial_intelligence
The script will output:

Shortened link: https://tinyurl.com/xxxxx
## 🛠 Code Example

import pyshorteners

try:
    link = input("Enter the link: ").strip()

    if not link.startswith("http://") and not link.startswith("https://"):
        link = "https://" + link

    shortener = pyshorteners.Shortener()
    shortened_link = shortener.tinyurl.short(link)
    print("Shortened link:", shortened_link)

except Exception as e:
    print("❌ Error shortening the URL:", e)
## 📎 Example Links to Try
https://en.wikipedia.org/wiki/Artificial_intelligence

https://www.google.com

https://github.com


