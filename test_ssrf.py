import urllib.request
from urllib.parse import urljoin
target = urljoin('https://github.com/Hardonian/Hardonian/blob/main/', 'file:///etc/passwd')
print("Target:", target)
