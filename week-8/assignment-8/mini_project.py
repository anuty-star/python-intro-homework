
import csv

clean_data = []
skipped_rows = []
rows_attempted = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            
            if None in row:
                skipped_rows.append(
                    f"Row {row_number}: extra column detected — skipped"
                )
                continue

            try:
                name = row["name"]
                category = row["category"]
                amount = float(row["amount"])

                if not name or not category:
                    raise ValueError("missing name or category")

                clean_data.append({
                    "name": name,
                    "category": category,
                    "amount": amount
                })

            except ValueError as error:
                skipped_rows.append(
                    f"Row {row_number}: ValueError — {error}"
                )

            except KeyError as error:
                skipped_rows.append(
                    f"Row {row_number}: KeyError — missing column {error}"
                )

            except TypeError as error:
                skipped_rows.append(
                    f"Row {row_number}: TypeError — {error}"
                )

except FileNotFoundError:
    print('Error: "messy_data.csv" was not found.')
else:
    print("=== CSV Report ===")
    print(f"Rows attempted:  {rows_attempted}")
    print(f"Rows parsed:     {len(clean_data)}")
    print(f"Rows skipped:    {len(skipped_rows)}")

    print("\nSkipped rows:")
    for skipped in skipped_rows:
        print(f"  {skipped}")

    print("\nClean data:")
    for item in clean_data:
        print(
            f"  {item['name']} | {item['category']} | "
            f"${item['amount']:.2f}"
        )
