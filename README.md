### Check-ASN for Burp Suite

**Check-ASN** is a Burp Suite extension that identifies the organization name associated with the IP address of each HTTP request in the HTTP history tab. It uses the `ipinfo.io` API to retrieve ASN and extracts the organization name for annotation.

---
<img width="1438" alt="image" src="https://github.com/user-attachments/assets/bc8e42b0-51f3-4e1a-a236-31c872c7ad62" />
---

### Features
- Resolves domain names from HTTP requests to IP addresses.
- Retrieves and displays the organization name associated with the IP using the `ipinfo.io` API.
- Annotates HTTP history entries with the organization name for easy identification.
- Lightweight and easy to integrate into your Burp Suite workflow.

---

### Installation

1. **Prerequisites**
   - Ensure you have Jython installed. You can download it from [jython.org](http://www.jython.org/).
   - Add the Jython standalone JAR file to Burp Suite under `Extender > Options > Python Environment`.

2. **Download the Extension**
   - Clone this repository or download the `extn.py` script.

3. **Load the Extension**
   - Open Burp Suite and navigate to `Extender > Extensions`.
   - Click `Add` and select the following options:
     - Extension type: **Python**
     - Extension file: Select the downloaded `extn.py` script.

4. **Verify Installation**
   - Once loaded, you should see `Check-ASN` listed as a loaded extension in the `Extender` tab.
   - Make HTTP requests and observe the HTTP history tab for organization annotations in the **Notes** column.

---

### Usage
- This extension runs automatically when loaded.
- The organization name for each HTTP request is added as a comment in the HTTP history tab.
  - Example: If a request is made to `www.amazon.com`, the comment might show `Organization: Amazon.com, Inc.`.
  
---

### Troubleshooting
- **No Comments Appearing**: 
  - Ensure the target domain resolves to a valid IP address.
  - Verify your network connection to the `ipinfo.io` API.

- **Error Logs**:
  - Check the Extender `Output` tab for detailed error messages.
  - Common issues include DNS resolution errors or network restrictions.

---

### API Note
- This extension uses the free `ipinfo.io` API. For high-volume use or additional features, consider obtaining an API key from [ipinfo.io](https://ipinfo.io/).

---

### Contribution
Feel free to contribute by:
- Submitting pull requests for new features or bug fixes.
- Reporting issues in the [GitHub Issues](https://github.com/avicoder/burp-asn/issues) section.

---

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
