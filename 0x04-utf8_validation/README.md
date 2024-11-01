# UTF-8 Validation

## Description

This project contains a method to determine if a given data set represents a valid UTF-8 encoding. A character in UTF-8 can be 1 to 4 bytes long. The data set can contain multiple characters and is represented by a list of integers, where each integer represents 1 byte of data. The method only handles the 8 least significant bits of each integer.

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS
- PEP 8 style guide (version 1.7.x)

## Installation

1. Ensure you have Python 3.4.3 or later installed on your system.
2. Clone the repository to your local machine.

```sh
git clone https://github.com/your_username/utf8-validation.git
cd utf8-validation

