# StopSharingMyGoogleDrive

A script to remove a specified user/email from all shared files and folders in Google Drive in bulk.

## Overview

**StopSharingMyGoogleDrive** is a Python script that automates the process of removing a specific user's access from all files and folders shared with them in your Google Drive. This can be particularly useful for managing permissions and ensuring that only authorized users have access to your documents specially if you have a large number of files shared.

## Features

- **Automated Access Removal**: Remove a specified user from all files they have access to in your Google Drive.
- **Batch Processing**: Efficiently handles large numbers of files.
- **Simple Configuration**: Easily set up and configure the script with your Google API credentials.

## Prerequisites

- Python 3.6 or higher
- Google API credentials (OAuth 2.0 Client ID)
- Google Drive API enabled

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/junaidtitan/StopSharingMyGoogleDrive.git
    cd StopSharingMyGoogleDrive
    ```

2. **Create a virtual environment (optional but recommended)**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:

    ```sh
    pip install --upgrade pip
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

4. **Set up Google API credentials**:

    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing one.
    - Enable the Google Drive API for your project.
    - Create OAuth 2.0 credentials and download the `credentials.json` file.
    - Place the `credentials.json` file in the root directory of this project.

## Adding Test Users on Google Cloud

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to "APIs & Services" > "OAuth consent screen".
3. Scroll down to the "Test users" section.
4. Add the email addresses of the users who need to access the application (including your own).
5. Save the changes.

## Usage

1. **Run the script**:

    ```sh
    python3 stop.py
    ```

2. **Follow the authentication prompts** to authorize the script to access your Google Drive.

3. **Enter the email address of the user** you want to remove when prompted.

## Usage Example

Here is an example of how to use the script:

```sh
$ python3 stop.py
Enter the email of the user to remove: user@example.com
Removing user@example.com from file1
Removing user@example.com from file2
...
```

## Support

If you encounter any issues or have questions, please open an issue on GitHub. Here are some common troubleshooting tips:

### Environment Issues

- Ensure that you are using the correct Python environment. Use `python3` and `pip3` to ensure compatibility.
- If you encounter issues with package installation, make sure to upgrade `pip`:

    ```sh
    pip install --upgrade pip
    ```

- Verify the installed packages:

    ```sh
    pip3 list | grep google
    ```

### Common Errors

- **ModuleNotFoundError: No module named 'google'**: Ensure you have installed the required packages with:

    ```sh
    pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- [Google Auth Library](https://github.com/googleapis/google-auth-library-python)
