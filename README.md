# Temperature Conversion Script

This Python script allows users to convert temperatures between Celsius and Fahrenheit. It prompts the user to choose the conversion direction and then asks for the appropriate temperature input before displaying the converted value.

## Features

- **Dual Conversion:** Convert from Celsius to Fahrenheit and vice versa.
- **User-Friendly Interface:** Clear prompts guide the user through the conversion process.
- **Error Handling:** Displays an error message if an invalid option is selected.

## Requirements

- Python 3.x installed on your system.

## Usage

1. **Run the Script**

   Open your terminal or command prompt and navigate to the directory where the script is saved. Then execute:
   ```bash
   python temperature_conversion.py
   ```

2. **Follow the Prompts**

   - The script will prompt you to choose the conversion type:
     - **Celsius to Fahrenheit:** Enter `c` or `C`
     - **Fahrenheit to Celsius:** Enter `f` or `F`
   - Depending on your selection, the script will ask for the temperature input.
   - The converted temperature is then displayed on the screen.

## Code Overview

- **User Input:** The script begins by asking the user to select a conversion direction.
- **Conditional Logic:** Depending on the input, it performs the appropriate calculation:
  - Celsius to Fahrenheit: Uses the formula `(Celsius * 9/5) + 32`.
  - Fahrenheit to Celsius: Uses the formula `(Fahrenheit - 32) * 5/9`.
- **Output:** It then prints the converted temperature in a formatted string.

## Customization

Feel free to modify the script to add more features, such as:
- Rounding off the conversion result to a desired number of decimal places.
- Handling invalid numeric inputs more gracefully.
- Creating a graphical user interface (GUI) for a more interactive experience.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Author

Laiba Khan
