# BanKing Application

BanKing is a simple banking application built using Python and Tkinter. It allows users to sign up, log in, and manage their accounts.

## Features

- User Signup
- User Login
- Account Management
- Secure Password Handling

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Anaconda (optional, for managing dependencies)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/adamlaw669/BanKing
    cd Banking
    ```

2. (Optional) Create a virtual environment using Anaconda:
    ```sh
    conda create -n banking_env python=3.x
    conda activate banking_env
    ```

3. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python page.py
    ```

2. Follow the on-screen instructions to sign up or log in.

## Project Structure

- [page.py](http://_vscodecontentref_/1): Contains the main application logic and UI for signup and login.
- `bank.py`: Contains the user management logic, including signup and login functions.
- `users.csv`: Stores user data in CSV format.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [Python](https://www.python.org/) for the programming language.