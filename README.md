
# E-Liquid Calculator

A comprehensive and customizable e-liquid calculator with an advanced graphical interface. This tool is designed for DIY e-liquid creators, offering precise calculations, recipe management, stock tracking, and personalized labeling.

---

## Features

### 🛠 Core Functionalities
- **PG/VG Ratio Adjustment**: Set your desired propylene glycol (PG) and vegetable glycerin (VG) proportions.
- **Nicotine Strength**: Calculate based on base nicotine strength and booster preferences.
- **Flavor Management**: Add multiple flavors with custom proportions, types, and steep times.

### 📊 Advanced Features
- **Graphical Analysis**: View proportions in interactive graphs (e.g., bar charts, pie charts).
- **Stock Management**: Track base, booster, and flavor stocks with low-stock alerts.
- **Recipe Comparison**: Compare multiple recipes side by side.

### 🏷 Personalized Labels
- Generate printable labels including:
  - QR Code linking to full recipe details.
  - Recipe creation date.
  - Steep time recommendations.

### 🌟 Additional Functionalities
- **Mode Selection**: Choose between beginner (simplified) and advanced (detailed) modes.
- **Favorites & History**: Manage recipe history and mark frequently used recipes as favorites.
- **Steep Time Tracker**: Get notifications for when your e-liquid is ready.

---

## Installation

### Prerequisites
- Python 3.8 or later
- Required libraries (install using `requirements.txt`)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/eliquid-calculator.git
   cd eliquid-calculator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

1. **Choose Base & Booster**:
   - Specify the PG/VG ratio and nicotine strength for your base and booster.
   - Select the desired total volume.

2. **Add Flavors**:
   - Specify flavor name, type, proportions, and brand.

3. **Calculate & Save**:
   - View results and save recipes to JSON format for later use.

4. **Generate Labels**:
   - Create a printable label with QR Code and recipe details.

---

## Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI framework for the interface.
- **Matplotlib**: Visualization library for graphs.
- **qrcode**: Library for generating QR codes.
- **Pillow**: Image processing for QR code generation.

---

## Contributing

Feel free to fork this repository and submit pull requests. All contributions are welcome!

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Screenshots

### Main Interface
![Main Interface](images/main_interface.png)

### Recipe Comparison
![Recipe Comparison](images/recipe_comparison.png)

### Printable Label
![Label](images/printable_label.png)
