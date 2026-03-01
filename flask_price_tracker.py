from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
import pandas as pd

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_prices():

    products = [
        "Shakespeare's Sonnets",
        "Tipping the Velvet",
        "Soumission",
        "Sharp Objects",
        "Libertarianism for Beginners",
        "The Requiem Red",
        "Set Me Free",
        "Olio",
        "It's Only the Himalayas",
        "The Black Maria"
    ]

    product_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://books.toscrape.com/")

        for product in products:
            search_results = page.locator(f"text='{product}'")

            if search_results.count() > 0:
                search_results.nth(0).click()
                price_text = page.locator("div.product_main p.price_color").inner_text()
                price = float(price_text.replace("£", ""))
                product_data.append({
                    "Product Name": product,
                    "Price": price
                })
                page.goto("https://books.toscrape.com/")
            else:
                product_data.append({
                    "Product Name": product,
                    "Price": None
                })

        browser.close()

    df = pd.DataFrame(product_data)
    df = df.sort_values(by="Price", na_position='last')

    file_path = r"C:\Users\Neha\OneDrive\Desktop\ppyautogui\Retail_Price_Report.csv"
    df.to_csv(file_path, index=False)

    return jsonify({
        "status": "success",
        "message": "Report generated successfully",
        "file_path": file_path,
        "data": product_data
    })


if __name__ == '__main__':
    app.run(debug=True)

    #http://127.0.0.1:5000/scrape
    # ---browser url,client request