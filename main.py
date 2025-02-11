import requests
import selectorlib
from sendemail import Email
import time
import sqlite3





URL ='https://programmer100.pythonanywhere.com/tours/'
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# INSERT INTO events VALUES ('tigers','alappuzha','2025.10.14')
# SELECT * FROM events WHERE date = "2025.10.14"
# DELETE FROM events WHERE band = "tigers"

class Event:
    def scrape(self,url):
        #scrape the source from the url
        response = requests.get(url)
        source = response.text
        return source

    def extract(self,source):
        extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value



class Database:

    def __init__(self):
        self.connection = sqlite3.connect("data.db")

    def store(self,extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self,extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",(band,city,date))
        rows = cursor.fetchall()
        print(row)
        return rows

if __name__ == "__main__":
    while True:
        event = Event()
        scraped=event.scrape(URL)
        extracted=event.extract(scraped)
        print(extracted)


        if extracted != "No upcoming tours":
            database=Database()
            content = database.read(extracted)
            if not content:
                database.store(extracted)
                print(extracted)
                email=Email()
                email.send(extracted)
                print(extracted)
                print(type(extracted))
        time.sleep(3)