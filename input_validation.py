import re

def validate_input(input_url):
    """
    Validates and sanitizes user-supplied input URL to prevent SSRF attacks.
    """
    # Define a regular expression pattern for valid URLs
    url_pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')
    
    # Check if input matches the URL pattern
    if not url_pattern.match(input_url):
        raise ValueError('Invalid URL')
        
    # Check if input contains special characters or unexpected values
    if '://' in input_url or '//' in input_url or '#' in input_url:
        raise ValueError('Invalid input')
        
    # Sanitize input to remove any potentially dangerous characters
    sanitized_input_url = re.sub('[^a-zA-Z0-9:/?=&]+', '', input_url)
    
    return sanitized_input_url
