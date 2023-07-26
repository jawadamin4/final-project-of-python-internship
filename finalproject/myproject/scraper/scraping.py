import requests
from bs4 import BeautifulSoup

def scrape_yahoo_finance_lookup():
    url = f"https://finance.yahoo.com/lookup/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data_rows = soup.find_all('tr', class_='data-row')

        if data_rows:

            all_data = []
            for row in data_rows:
                symbol = row.select_one('.data-col0 a').text
                name = row.select_one('.data-col1').text
                price = row.select_one('.data-col2').text
                price_change = row.select_one('.data-col3 span').text.strip('+-')
                percentage_change = row.select_one('.data-col4 span').text.strip('+-')

                # Append the data for this row as a dictionary to the all_data list
                all_data.append({
                    'symbol': symbol,
                    'name': name,
                    'price': price,
                    'price_change': price_change,
                    'percentage_change': percentage_change,
                })

            # Print all the extracted data
            for stock_data in all_data:
                print(stock_data)
        else:
         print("No data rows found on the page.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


scrape_yahoo_finance_lookup()