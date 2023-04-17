import requests

def send_request(url, method='GET', headers=None, data=None):
    """
    Sends a request to the specified URL and returns the response object.
    """
    # Send the request using the requests library
    response = requests.request(method, url, headers=headers, data=data)
    
    return response

def analyze_response(response):
    """
    Analyzes the server response and returns a dictionary of its components.
    """
    # Extract the components of the response
    response_status_code = response.status_code
    response_headers = response.headers
    response_body = response.text
    
    # Create a dictionary of the response components
    response_dict = {
        'status_code': response_status_code,
        'headers': response_headers,
        'body': response_body
    }
    
    return response_dict

def detect_ssrf_vulnerabilities(response_dict):
    """
    Detects potential SSRF vulnerabilities in the server response.
    """
    # Check the response status code for potential SSRF vulnerabilities
    if response_dict['status_code'] in [400, 404, 500]:
        print('Potential SSRF vulnerability detected: {}'.format(response_dict['status_code']))
        
    # Check the response headers for potential SSRF vulnerabilities
    for header_name, header_value in response_dict['headers'].items():
        if 'localhost' in header_value or '127.0.0.1' in header_value:
            print('Potential SSRF vulnerability detected in header: {}'.format(header_name))
        
    # Check the response body for potential SSRF vulnerabilities
    if 'localhost' in response_dict['body'] or '127.0.0.1' in response_dict['body']:
        print('Potential SSRF vulnerability detected in response body')
