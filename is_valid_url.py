from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

if __name__ == "__main__":
    # Test the function with some example URLs
    print(is_valid_url("https://example.com"))   # True
    print(is_valid_url("example.com"))           # False