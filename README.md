# Zootopia Project with API Integration

## Overview
This project showcases the Zootopia application, where the goal is to fetch and display information about animals using an external API (Scryfall API or another API source you decide). The project is designed to help you get familiar with:

- Working with external APIs
- Making GET requests
- Handling JSON data
- Displaying dynamic content using a template

## Features
- **Fetching Animal Data**: This project retrieves information about animals (such as name, diet, type, etc.) based on user input.
- **Dynamic Content Rendering**: Using the provided data, the HTML content is dynamically generated and displayed to the user.
- **User-Friendly Interface**: The application allows users to search for animals by their name and displays details like diet, location, and more.

## Requirements
Before you start, make sure you have the following:

- Python 3.x
- `requests` library for making API requests
- `json` module to parse and handle the data
- An active internet connection to fetch data from the API

## Installation
1. **Clone the repository**:

    ```bash
    git clone https://github.com/Tez224/Zootopia.git
    cd Zootopia
    ```

2. **Install dependencies** (make sure you're in the project directory):

    If you have a `requirements.txt` file, use:

    ```bash
    pip install -r requirements.txt
    ```

    If you're using a virtual environment (`venv`), you can set it up with:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate   # On Windows
    pip install requests
    ```

3. **Add your API key**: Store your API key in a `.env` file or directly in your code (it's more secure to use `.env`).

4. **Run the application**:

    ```bash
    python app.py
    ```

## Functionality
1. **Search for Animals**: Enter the name of an animal to search for (e.g., "fox") and the application will show details like its diet, location, and skin type.
2. **HTML Generation**: The application uses a template HTML file and replaces a placeholder with the dynamically fetched data to generate an HTML page.
3. **Error Handling**: If no data is found or an error occurs during the API request, an appropriate message will be displayed to the user.

## Code Structure
- **app.py**: Main application file that handles user input, makes API requests, and generates the output.
- **data_fetcher.py**: Handles the logic for fetching animal data from the API.
- **template.html**: HTML template that will be filled with the animal data and saved as an HTML file.
- **.env**: (Optional) Stores your API key securely.

## API Integration
The application makes use of an external API to fetch data about animals. The query parameter used is the animal's name, and the response includes details such as:

- `name`
- `diet`
- `location`
- `type`
- `skin type`

## Example Usage
1. **Start the program**:

    ```bash
    python app.py
    ```

2. **Enter an animal name** when prompted:

    ```text
    Enter an animal you want to learn about: fox
    ```

3. **View the results** in the console or save them in an HTML file.

## Error Handling
- If no results are found for an animal, the user will be prompted with a friendly message suggesting they try again with a different animal.
- Errors like invalid API responses or missing data will also be handled gracefully.
