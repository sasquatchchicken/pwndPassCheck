# pwndPassCheck

## Overview

This script provides a simple yet effective way to enhance password security by checking if a given password has been compromised using the "Have I Been Pwned" service. It utilizes the k-Anonymity model to ensure the password is not sent in its entirety, thus maintaining user privacy.

## Features

- Passwords are never sent in full to external services, ensuring user privacy.
- Utilizes the "Have I Been Pwned" API to check if a password has been compromised.
- Easy-to-use script that prompts users to enter a password securely.

## Requirements

- Python 3.x
- Requests library (pip install requests)

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/sasquatchchicken/pwndPassCheck.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pwndPassCheck
    ```

3. Run the script:

    ```bash
    python pwdpasswds.py
    ```

4. Enter a new password when prompted.

5. The script will check if the password has been compromised and provide feedback.

## Example

```bash
Enter a new password: H3LL0world
Password has been compromised.

Enter a new password: username@!#%00
Password is not compromised
