import pyshorteners

try:
    link = input("Enter the link: ").strip()

    # Automatically add https:// if missing
    if not link.startswith("http://") and not link.startswith("https://"):
        link = "https://" + link

    shortener = pyshorteners.Shortener()
    shortened_link = shortener.tinyurl.short(link)
    print("Shortened link:", shortened_link)

except Exception as e:
    print("❌ Error shortening the URL:", e)
