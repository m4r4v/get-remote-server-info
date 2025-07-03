# Get Remote Server Info

A simple yet powerful Python tool to retrieve web server information and HTTP headers. Designed with security best practices for IT operations and cybersecurity professionals.

## Features

- [SECURE] **Secure by default** - SSL certificate verification enabled
- [SMART]  **Smart URL handling** - Automatically detects HTTP/HTTPS schemes
- [FAST]   **Performance monitoring** - Shows response times
- [COLOR]  **Colored output** - Easy-to-read terminal interface
- [SAFE]   **Input validation** - Prevents malformed requests
- [GUARD]  **Timeout protection** - Prevents hanging connections
- [ERROR]  **Comprehensive error handling** - Clear error messages

## Security Features

- SSL certificate verification by default
- Graceful fallback for self-signed certificates (with warnings)
- Input validation to prevent injection attacks
- Timeout protection against slow/malicious servers
- Clear security warnings when SSL verification is disabled

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/m4r4v/get-remote-server-info.git
cd get-remote-server-info
```

### 2. Create Virtual Environment

Creating a virtual environment is **highly recommended** to avoid dependency conflicts:

#### On Linux/macOS:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### On Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

### 3. Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

Test the installation by running:

```bash
python main.py
```

## Usage

### Basic Usage

1. **Activate your virtual environment** (if not already active):
   ```bash
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **Enter a domain** when prompted:
   ```
   Domain: example.com
   ```

### Supported Input Formats

The tool accepts various domain formats:

- `example.com` - Automatically tries HTTPS first, then HTTP
- `https://example.com` - Forces HTTPS
- `http://example.com` - Forces HTTP
- `subdomain.example.com` - Works with subdomains

### Example Output

```
>>> WEBSITE SERVER INFORMATION <<<
Type the website address to get information from
example: example.com or https://example.com

Domain: github.com

Looking up information for: https://github.com

Results for: https://github.com
IP Address: 140.82.112.4
Response Time: 0.234s
Status Code: 200

HTTP Headers:
--------------------------------------------------
Server: GitHub.com
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
Vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame
...
```

## IT Operations & Cybersecurity Use Cases

### Security Assessment
- **SSL/TLS Configuration**: Check if HTTPS is properly configured
- **Server Headers**: Identify web server software and versions
- **Security Headers**: Verify presence of security headers (HSTS, CSP, etc.)
- **Response Times**: Monitor server performance

### Network Troubleshooting
- **DNS Resolution**: Verify domain resolves to correct IP
- **Connectivity**: Test if services are accessible
- **Response Analysis**: Check HTTP status codes and headers

### Reconnaissance (Ethical/Authorized)
- **Server Fingerprinting**: Identify server technologies
- **Header Analysis**: Discover server configurations
- **Performance Baseline**: Establish response time baselines

## Troubleshooting

### Common Issues

#### SSL Certificate Errors
```
SSL Error: [SSL: CERTIFICATE_VERIFY_FAILED]
```
**Solution**: The tool will automatically retry without SSL verification and display a warning. This is common with self-signed certificates.

#### Connection Timeout
```
Request timeout
```
**Solution**: The server may be slow or unreachable. Try again or check your internet connection.

#### Invalid Domain Format
```
Error: Invalid domain format. Please try again.
```
**Solution**: Ensure you're using a valid domain format (e.g., `example.com`, not `example`).

#### Module Not Found Error
```
ModuleNotFoundError: No module named 'requests'
```
**Solution**: 
1. Ensure your virtual environment is activated
2. Install dependencies: `pip install -r requirements.txt`

### Virtual Environment Issues

#### Virtual Environment Not Activated
If you see packages installing globally or import errors:

1. **Check if activated**: Your terminal prompt should show `(venv)` at the beginning
2. **Reactivate**: Run the activation command again
3. **Verify Python path**: `which python` should point to your venv directory

#### Dependencies Not Installing
```bash
# Upgrade pip first
pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

## Development

### Project Structure
```
get-remote-server-info/
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── venv/              # Virtual environment (created by you)
```

### Code Quality Features
- **Type hints** for better code documentation
- **Docstrings** for all functions
- **Error handling** for network and SSL issues
- **Modular design** with separate functions
- **Security-first approach** with SSL verification

## Dependencies

- **requests** (2.31.0): HTTP library for making web requests
- **termcolor** (2.3.0): Colored terminal output
- **urllib3** (2.0.7): HTTP client library (used by requests)
- **validators** (0.22.0): Input validation for URLs and domains

## Security Considerations

1. **SSL Verification**: Always enabled by default for HTTPS
2. **Input Validation**: All user inputs are validated
3. **Timeout Protection**: Prevents hanging on slow servers
4. **Error Handling**: Graceful handling of network errors
5. **No Data Storage**: Tool doesn't store or log sensitive information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the repository for license details.

## Author

**m4r4v** - [GitHub Profile](https://github.com/m4r4v)

---

## Quick Start Commands

```bash
# Complete setup in one go
git clone https://github.com/m4r4v/get-remote-server-info.git
cd get-remote-server-info
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

**Remember**: Always activate your virtual environment before running the tool!
