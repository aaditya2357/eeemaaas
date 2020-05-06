import sqlite3
from datetime import datetime
from selenium.webdriver import Chrome


# Inserting all data to database
def insert(price, price_p):
    tanggal = datetime.today().strftime('%d-%m-%Y')
    buy_price = price[0]
    buy_before = price_p[0]
    sale_price = price[1]
    sale_before = price_p[1]
    buy_change = ((buy_price - buy_before)/abs(buy_before))*100
    sale_change = ((sale_price - sale_before) / abs(sale_before)) * 100
    sql = "INSERT INTO emas(last_update, buy_price, buy_b, buy_c, sale_price, sale_b, sale_c ) " \
          "VALUES ( \"{}\", {}, {}, {}, {}, {}, {})"\
        .format(str(tanggal), str(buy_price), str(buy_before), str(buy_change), str(sale_price), str(sale_before), str(sale_change))
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


# Get Current Gold Price before current time
# (Yesterday Price) to insert it into Current time
def getVal():
    price_before = "SELECT buy_price, sale_price FROM emas ORDER BY id DESC"
    cur = conn.cursor()
    cur.execute(price_before)
    result = cur.fetchall()
    conn.commit()
    return result[0]


# Get Current Value Of Gold
def updater():
    browser = Chrome()
    browser.get('https://www.tokopedia.com/emas/harga-hari-ini/')
    buy_price = browser.find_elements_by_xpath('//*[@class="main-price"]')
    price = []
    for i in buy_price:
        price.append(i.text)

    price = [x[2:] for x in price]
    price = [x.replace(".", "") for x in price]
    price = [int(x) for x in price]

    browser.close()
    return price


if __name__ == '__main__':
    conn = sqlite3.connect('mydatabase.db')
    price = updater()
    price_p = getVal()
    insert(price, price_p)
    print("=== Scrape Done ===")
