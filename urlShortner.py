import pyshorteners

long_url = input("Enter the URL to shorten: ")

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(long_url)

print("Short URL:", short_url)
