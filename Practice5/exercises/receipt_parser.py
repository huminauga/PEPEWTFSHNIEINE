import re
import json

def parse_receipt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    result = {}

    # task 1: Prices
    price_pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
    prices = re.findall(price_pattern, text)

    # Convert prices to float
    prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

    result["all_prices"] = prices_clean

    # task 2: Extract profuct names
    product_pattern = r"\d+\.\n(.+)"
    products = re.findall(product_pattern, text)

    result["products"] = [p.strip() for p in products]

    # task 3: Extract total amount
    total_pattern = r"ИТОГО:\n([\d\s]+,\d{2})"
    total_match = re.search(total_pattern, text)

    if total_match:
        total = float(total_match.group(1).replace(" ", "").replace(",", "."))
    else:
        total = None

    result["total"] = total

    # task 4: Extract date and time
    datetime_pattern = r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}"
    datetime_match = re.search(datetime_pattern, text)

    result["datetime"] = datetime_match.group(0) if datetime_match else None

    # task 5: Extract payment method
    payment_pattern = r"(Банковская карта|Наличные)"
    payment_match = re.search(payment_pattern, text)

    result["payment_method"] = payment_match.group(0) if payment_match else None

    # task 6: Calculate total from products
    result["calculated_sum"] = sum(prices_clean)

    return result


if __name__ == "__main__":
    parsed = parse_receipt("/Users/mac/Python/work/PEPEWTFSHNIEINE/Practice5/exercises/raw.txt")

    print(json.dumps(parsed, indent=4, ensure_ascii=False))