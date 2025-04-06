from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

def scrape_flipkart_prices(query):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
        driver.get(url)
        time.sleep(2)

        products = []
        product_elements = driver.find_elements(By.CSS_SELECTOR, 'div._1AtVbE')[:10]

        for elem in product_elements:
            try:
                name = elem.find_element(By.CSS_SELECTOR, 'div._4rR01T').text
                price = elem.find_element(By.CSS_SELECTOR, 'div._30jeq3').text
                link = elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
                products.append({
                    "name": name,
                    "price": price,
                    "link": "https://www.flipkart.com" + link
                })
                if len(products) == 3:
                    break
            except:
                continue

        return products if products else [{"name": "No product found", "price": "-", "link": "#"}]

    except Exception as e:
        return [{"name": "Error fetching Flipkart data", "price": str(e), "link": "#"}]
    finally:
        driver.quit()


def generate_dummy_data(site, query, base_url):
    prices = [random.randint(1800, 4500) for _ in range(3)]
    return [
        {
            "name": f"{site} {query.title()} - Model {i+1}",
            "price": f"₹{price}",
            "link": f"{base_url}/search?q={query.replace(' ', '+')}"
        }
        for i, price in enumerate(prices)
    ]

def scrape_amazon_prices(query):
    return generate_dummy_data("Amazon", query, "https://www.amazon.in")

def scrape_croma_prices(query):
    return generate_dummy_data("Croma", query, "https://www.croma.com")

def scrape_ajio_prices(query):
    return generate_dummy_data("Ajio", query, "https://www.ajio.com")

def scrape_snapdeal_prices(query):
    return generate_dummy_data("Snapdeal", query, "https://www.snapdeal.com")

def scrape_myntra_prices(query):
    return generate_dummy_data("Myntra", query, "https://www.myntra.com")

def scrape_nykaa_prices(query):
    return generate_dummy_data("Nykaa", query, "https://www.nykaa.com")

def scrape_reliance_prices(query):
    return generate_dummy_data("Reliance", query, "https://www.reliancedigital.in")


def get_price_comparison(query):
    return {
        "Flipkart": scrape_flipkart_prices(query),
        "Amazon": scrape_amazon_prices(query),
        "Croma": scrape_croma_prices(query),
        "Ajio": scrape_ajio_prices(query),
        "Myntra": scrape_myntra_prices(query),
        "Snapdeal": scrape_snapdeal_prices(query),
        "Nykaa": scrape_nykaa_prices(query),
        "Reliance": scrape_reliance_prices(query),
    }
