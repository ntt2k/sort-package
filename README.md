# Package Sorting Utility

This project consists of a Python utility function for sorting packages into different stacks based on their dimensions and mass, as well as a set of pytest tests to ensure the utility functions as expected. The `sort_package` function classifies packages into STANDARD, SPECIAL, or REJECTED categories, facilitating automated handling in a robotic automation factory environment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/ntt2k/sort-package
   cd sort-package
   ```

2. **Install the required packages:**

   ```
   pip install pytest
   ```

## Running the Tests

To run the automated tests for the `sort_package` function, execute the following command from the project root directory:

```
pytest
```

This command will discover and run all tests defined in `test_sort_package.py`, reporting the outcomes to the console.

## Usage

The `sort_package` function can be imported and used in other Python scripts as follows:

```
python sort_package.py
```

Replace the `width`, `height`, `length`, and `mass` arguments with the actual dimensions and mass of the package you wish to classify.

