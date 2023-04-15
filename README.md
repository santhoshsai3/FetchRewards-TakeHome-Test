# HTTP Endpoint Availability Tester
This program tests the availability of HTTP endpoints defined in a YAML configuration file.

## Requirements
- Python 3.6 or higher
- requests library
- yaml library

You can install these libraries using pip. For example, run pip install requests pyyaml in the terminal.

## How to Run
- Create a YAML configuration file with a list of HTTP endpoints you want to test.
- Save the configuration file as endpoints.yml or any name you prefer in the location where script.py is saved.
- Open a terminal in the folder where you saved the configuration file/ script file.
- Run the program by typing the following command python script.py <name_of_the_endpoints_file.yaml>
- The program will continuously test the endpoints every 15 seconds and print the availability percentage of each domain in the configuration file.
- To stop the program, press CTRL+C in the terminal.
