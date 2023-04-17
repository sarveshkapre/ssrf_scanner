from urllib.parse import urlparse, urlunparse, urlencode, quote_plus, unquote_plus

def parse_url(input_url):
    """
    Parses the input URL and returns a dictionary of its components.
    """
    # Parse the input URL
    parsed_url = urlparse(input_url)
    
    # Extract the components of the parsed URL
    url_scheme = parsed_url.scheme
    url_netloc = parsed_url.netloc
    url_path = parsed_url.path
    url_params = parsed_url.params
    url_query = parsed_url.query
    url_fragment = parsed_url.fragment
    
    # Create a dictionary of the parsed URL components
    parsed_url_dict = {
        'scheme': url_scheme,
        'netloc': url_netloc,
        'path': url_path,
        'params': url_params,
        'query': url_query,
        'fragment': url_fragment
    }
    
    return parsed_url_dict

def manipulate_url(input_url, new_url_dict):
    """
    Manipulates the input URL based on the new_url_dict and returns the new URL.
    """
    # Parse the input URL
    parsed_url = urlparse(input_url)
    
    # Update the parsed URL with the new URL components
    updated_url = parsed_url._replace(**new_url_dict)
    
    # Reconstruct the updated URL
    new_url = urlunparse(updated_url)
    
    return new_url

def encode_url(input_url):
    """
    Encodes the input URL for safe usage in HTTP requests.
    """
    # Parse the input URL
    parsed_url = urlparse(input_url)
    
    # Encode the query string of the parsed URL
    encoded_query = urlencode(dict(parse_qsl(parsed_url.query)), quote_via=quote_plus)
    
    # Reconstruct the encoded URL
    encoded_url = urlunparse(parsed_url._replace(query=encoded_query))
    
    return encoded_url

def decode_url(input_url):
    """
    Decodes the input URL to restore its original form.
    """
    # Decode the query string of the input URL
    decoded_query = unquote_plus(urlparse(input_url).query)
    
    # Reconstruct the decoded URL
    decoded_url = input_url.replace(urlparse(input_url).query, decoded_query)
    
    return decoded_url
