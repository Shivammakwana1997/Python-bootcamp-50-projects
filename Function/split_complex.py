'''

You're creating a complex report  for a cafe's sales.
instead of putting all logic in one place , break it down

task:
wrtie function generate_report() that calls:
 
 fetch_Sales()
 filter_valid_orders()
 summarize_data()

 '''

def fetch_sales():
    print("fetching the sales data")


def filter_valid_Sales():
    print("filtering the sales data")


def summarize_data():
    print("summarizing the sales data")


def generate_report():
    fetch_sales()
    filter_valid_Sales()
    summarize_data()

    print("Report is ready")

generate_report()
