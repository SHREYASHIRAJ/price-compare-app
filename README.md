PricePulse - Price Comparison App

PricePulse is a full-stack web application that allows users to compare prices of any product across multiple Indian e-commerce platforms such as Flipkart, Amazon, Snapdeal, Croma, Nykaa, Ajio, and Myntra.

Built with:
- Flask for the backend with real-time scraping using Selenium and BeautifulSoup
- HTML, CSS, and JavaScript for a responsive frontend with pastel styling
- Optional Dark Mode for user comfort

---

Features

- Search and compare prices across 7+ e-commerce platforms
- Realistic pricing data and product links
- Toggle between light and dark mode
- Clean, animated user interface with a pastel color palette

---

Tech Stack

| Frontend   | Backend       | Scraping     |
|------------|---------------|--------------|
| HTML/CSS   | Flask         | Selenium     |
| JavaScript | Flask-CORS    | BeautifulSoup|
|            | REST API      | Requests     |

---
How to Run the App
1. Clone the Repository

```bash
git clone https://github.com/your-username/price-compare-app.git
cd price-compare-app
```
2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
```
3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```
4. Start the Backend Server

```bash
python app.py
```

The backend server will be available at: `http://127.0.0.1:5000`

 5. Launch the Frontend

- Go back to the root folder:
  ```bash
  cd ..
  ```
- Open `frontend/index.html` in a browser
- Enter a product name and click "Compare"

Note: The backend server must be running for the app to fetch live data.

---

Project Structure

```
price-compare-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── scrapers/
│       ├── flipkart.py
│       └── (other scraper files)
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│
└── README.md
```
