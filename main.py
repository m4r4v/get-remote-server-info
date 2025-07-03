#!/usr/bin/env python3
"""
Get Remote Server Info
A simple tool to retrieve web server information and headers.
Author: m4r4v
"""

import sys
import time
import socket
import requests
import validators
from termcolor import colored
from urllib.parse import urlparse
import urllib3


def print_banner():
    """Display the application banner."""
    print(colored('\n>>> WEBSITE SERVER INFORMATION <<<', 'cyan', attrs=['bold', 'underline']))
    print(colored('Type the website address to get information from', 'light_yellow'))
    print(colored('example: example.com or https://example.com', 'dark_grey'))


def validate_domain(domain):
    """
    Validate and normalize domain input.
    
    Args:
        domain (str): User input domain
        
    Returns:
        tuple: (is_valid, normalized_url, scheme)
    """
    if not domain or not domain.strip():
        return False, None, None
    
    domain = domain.strip()
    
    # If no scheme provided, try to detect or default to https
    if not domain.startswith(('http://', 'https://')):
        # Try https first (more secure)
        test_url = f'https://{domain}'
        if validators.url(test_url):
            return True, test_url, 'https'
        # Fallback to http
        test_url = f'http://{domain}'
        if validators.url(test_url):
            return True, test_url, 'http'
        return False, None, None
    
    # URL already has scheme
    if validators.url(domain):
        parsed = urlparse(domain)
        return True, domain, parsed.scheme
    
    return False, None, None


def get_ip_address(domain):
    """
    Get IP address for a domain.
    
    Args:
        domain (str): Domain name without scheme
        
    Returns:
        str: IP address or None if failed
    """
    try:
        # Remove scheme if present
        parsed = urlparse(domain)
        hostname = parsed.netloc if parsed.netloc else domain
        # Remove port if present
        hostname = hostname.split(':')[0]
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None


def fetch_server_info(url, verify_ssl=True, timeout=10):
    """
    Fetch server information from URL.
    
    Args:
        url (str): Full URL to fetch
        verify_ssl (bool): Whether to verify SSL certificates
        timeout (int): Request timeout in seconds
        
    Returns:
        tuple: (success, response_or_error, response_time)
    """
    start_time = time.time()
    
    try:
        # Disable SSL warnings only if verification is disabled
        if not verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        response = requests.get(
            url,
            verify=verify_ssl,
            timeout=timeout,
            allow_redirects=True
        )
        
        response_time = time.time() - start_time
        return True, response, response_time
        
    except requests.exceptions.SSLError as e:
        response_time = time.time() - start_time
        return False, f"SSL Error: {str(e)}", response_time
    except requests.exceptions.Timeout:
        response_time = time.time() - start_time
        return False, "Request timeout", response_time
    except requests.exceptions.ConnectionError as e:
        response_time = time.time() - start_time
        return False, f"Connection Error: {str(e)}", response_time
    except requests.exceptions.RequestException as e:
        response_time = time.time() - start_time
        return False, f"Request Error: {str(e)}", response_time


def display_results(url, ip_address, response, response_time):
    """
    Display the server information results.
    
    Args:
        url (str): The URL that was queried
        ip_address (str): IP address of the server
        response: HTTP response object
        response_time (float): Response time in seconds
    """
    print(f"\n{colored('Results for:', 'light_cyan')} {colored(url, 'light_blue')}")
    
    if ip_address:
        print(f"{colored('IP Address:', 'light_cyan')} {colored(ip_address, 'light_blue')}")
    else:
        print(f"{colored('IP Address:', 'light_cyan')} {colored('Unable to resolve', 'red')}")
    
    print(f"{colored('Response Time:', 'light_cyan')} {colored(f'{response_time:.3f}s', 'light_blue')}")
    print(f"{colored('Status Code:', 'light_cyan')} {colored(str(response.status_code), 'light_blue')}")
    
    print(f"\n{colored('HTTP Headers:', 'light_cyan', attrs=['bold'])}")
    print("-" * 50)
    
    for key, value in response.headers.items():
        print(f"{colored(key, 'light_cyan')}: {colored(value, 'light_blue')}")


def main():
    """Main application function."""
    try:
        print_banner()
        
        # Get domain input
        domain = input(f"\n{colored('Domain:', 'light_green')} ")
        
        # Validate domain
        is_valid, url, scheme = validate_domain(domain)
        if not is_valid:
            print(f"{colored('Error:', 'red')} Invalid domain format. Please try again.")
            return 1
        
        print(f"\n{colored('Looking up information for:', 'light_cyan')} {colored(url, 'light_blue')}")
        
        # Get IP address
        ip_address = get_ip_address(url)
        
        # Determine SSL verification strategy
        verify_ssl = True
        if scheme == 'https':
            # First try with SSL verification
            success, response, response_time = fetch_server_info(url, verify_ssl=True)
            
            if not success and "SSL" in str(response):
                print(f"{colored('Warning:', 'yellow')} SSL verification failed. Retrying without SSL verification...")
                print(f"{colored('Security Note:', 'yellow')} This connection may not be secure.")
                verify_ssl = False
                success, response, response_time = fetch_server_info(url, verify_ssl=False)
        else:
            # HTTP doesn't need SSL verification
            success, response, response_time = fetch_server_info(url, verify_ssl=False)
        
        if not success:
            print(f"{colored('Error:', 'red')} {response}")
            return 1
        
        # Display results
        display_results(url, ip_address, response, response_time)
        
        print(f"\n{colored('Author: m4r4v', 'light_yellow')}")
        return 0
        
    except KeyboardInterrupt:
        print(f"\n\n{colored('Process interrupted by user', 'red', attrs=['bold'])}")
        return 1
    except Exception as e:
        print(f"\n{colored('Unexpected error:', 'red')} {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
