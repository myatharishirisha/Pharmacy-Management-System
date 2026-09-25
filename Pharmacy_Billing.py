from datetime import datetime
import csv
import os

#print("Current folder:", os.getcwd())
print("CSV files will be created in:")
print(os.getcwd())

# ============================================================
# LISTS
# ============================================================

medicines = []
suppliers = []
sales = []


# ============================================================
# CSV FILE NAMES
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MEDICINE_FILE = os.path.join(BASE_DIR, "medicines.csv")
SUPPLIER_FILE = os.path.join(BASE_DIR, "suppliers.csv")
SALES_FILE = os.path.join(BASE_DIR, "sales.csv")


# ============================================================
# CREATE CSV FILES IF THEY DO NOT EXIST
# ============================================================

def create_csv_files():

    if not os.path.exists(MEDICINE_FILE):
        with open(MEDICINE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Id",
                "Name",
                "Price",
                "Quantity",
                "Expiry_date"
            ])

    if not os.path.exists(SUPPLIER_FILE):
        with open(SUPPLIER_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "supplier_id",
                "supplier_name",
                "contact_number",
                "company_name"
            ])

    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "medicine_id",
                "quantity",
                "total",
                "date"
            ])


# ============================================================
# LOAD DATA FROM CSV
# ============================================================

def load_data():

    # ---------------- MEDICINES ----------------

    with open(MEDICINE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            medicine = {
                "Id": int(row["Id"]),
                "Name": row["Name"],
                "Price": float(row["Price"]),
                "Quantity": int(row["Quantity"]),
                "Expiry_date": datetime.strptime(
                    row["Expiry_date"],
                    "%Y-%m-%d"
                ).date()
            }

            medicines.append(medicine)


    # ---------------- SUPPLIERS ----------------

    with open(SUPPLIER_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            supplier = {
                "Id": row["supplier_id"],
                "Name": row["supplier_name"],
                "Contact Number": row["contact_number"],
                "Company Name": row["company_name"]
            }

            suppliers.append(supplier)


    # ---------------- SALES ----------------

    with open(SALES_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            sale = {
                "medicine_id": int(row["medicine_id"]),
                "quantity": int(row["quantity"]),
                "total": float(row["total"]),
                "date": datetime.strptime(
                    row["date"],
                    "%Y-%m-%d"
                ).date()
            }

            sales.append(sale)


# ============================================================
# SAVE MEDICINES TO CSV
# ============================================================

def save_medicines():

    with open(MEDICINE_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Id",
            "Name",
            "Price",
            "Quantity",
            "Expiry_date"
        ])

        for medicine in medicines:

            writer.writerow([
                medicine["Id"],
                medicine["Name"],
                medicine["Price"],
                medicine["Quantity"],
                medicine["Expiry_date"].strftime("%Y-%m-%d")
            ])


# ============================================================
# SAVE SUPPLIERS TO CSV
# ============================================================

def save_suppliers():

    with open(SUPPLIER_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "supplier_id",
            "supplier_name",
            "contact_number",
            "company_name"
        ])

        for supplier in suppliers:

            writer.writerow([
                supplier["Id"],
                supplier["Name"],
                supplier["Contact Number"],
                supplier["Company Name"]
            ])


# ============================================================
# SAVE SALES TO CSV
# ============================================================

def save_sales():

    with open(SALES_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "medicine_id",
            "quantity",
            "total",
            "date"
        ])

        for sale in sales:

            writer.writerow([
                sale["medicine_id"],
                sale["quantity"],
                sale["total"],
                sale["date"].strftime("%Y-%m-%d")
            ])


# ============================================================
# ADD MEDICINE
# ============================================================

def add_medicine():

    print("\n========== ADD MEDICINE ==========")

    medicine_Id = int(input("Enter a Medicine ID: "))
    name = input("Enter a Medicine Name: ")
    price = float(input("Enter Price of Medicine: "))
    quantity = int(input("Enter Quantity of Medicine: "))

    while True:

        expiry_Date = input(
            "Enter Expiry Date (YYYY-MM-DD): "
        )

        try:

            expiry_Date = datetime.strptime(
                expiry_Date.strip(),
                "%Y-%m-%d"
            ).date()

            break

        except ValueError:

            print(
                "Invalid date. "
                "Please enter date in YYYY-MM-DD format."
            )


    medicine_details = {
        "Id": medicine_Id,
        "Name": name,
        "Price": price,
        "Quantity": quantity,
        "Expiry_date": expiry_Date
    }

    medicines.append(medicine_details)

    save_medicines()

    print("Medicine", name, "added successfully!")


# ============================================================
# SEARCH MEDICINE
# ============================================================

def search_medicine():

    print("\n========== SEARCH MEDICINE ==========")

    search = input(
        "Enter a Medicine ID or Medicine Name: "
    )

    for medicine in medicines:

        if (
            str(medicine["Id"]) == search
            or
            medicine["Name"].lower() == search.lower()
        ):

            print("\nMedicine found")

            print("ID:", medicine["Id"])
            print("Name:", medicine["Name"])
            print("Price:", medicine["Price"])
            print("Quantity:", medicine["Quantity"])

            print(
                "Expiry Date:",
                medicine["Expiry_date"]
            )

            if medicine["Quantity"] > 0:

                print(
                    "Stock Availability: Available"
                )

            else:

                print(
                    "Stock Availability: Out of Stock"
                )

            return

    print("Medicine Not Found")


# ============================================================
# UPDATE MEDICINE
# ============================================================

def update_medicine():

    print("\n========== UPDATE MEDICINE ==========")

    medicine_id = int(
        input("Enter a Medicine ID: ")
    )

    for medicine in medicines:

        if medicine["Id"] == medicine_id:

            print("Medicine Found")

            new_price = input(
                "Enter new Price (leave blank to skip): "
            )

            new_quantity = input(
                "Enter new Quantity (leave blank to skip): "
            )

            new_expirydate = input(
                "Enter new Expiry Date "
                "(YYYY-MM-DD, leave blank to skip): "
            )


            if new_price != "":

                medicine["Price"] = float(
                    new_price
                )


            if new_quantity != "":

                medicine["Quantity"] = int(
                    new_quantity
                )


            if new_expirydate != "":

                try:

                    new_expirydate = datetime.strptime(
                        new_expirydate.strip(),
                        "%Y-%m-%d"
                    ).date()

                    medicine["Expiry_date"] = (
                        new_expirydate
                    )

                except ValueError:

                    print(
                        "Invalid date. "
                        "Expiry date was not updated."
                    )

                    return


            save_medicines()

            print(
                "Medicine",
                medicine_id,
                "updated successfully!"
            )

            print("Updated Record:")
            print(medicine)

            return


    print(
        "Medicine",
        medicine_id,
        "not found"
    )


# ============================================================
# ADD SUPPLIER
# ============================================================

def add_supplier():

    print("\n========== ADD SUPPLIER ==========")

    supplier_id = input(
        "Enter Supplier ID: "
    )

    supplier_name = input(
        "Enter Supplier Name: "
    )


    while True:

        contact_number = input(
            "Enter Contact Number: "
        )

        if (
            contact_number.isdigit()
            and
            len(contact_number) == 10
        ):

            contact_number = (
                "+91 " + contact_number
            )

            break

        else:

            print(
                "Contact number must be exactly "
                "10 digits."
            )


    company_name = input(
        "Enter Company Name: "
    )


    supplier = {

        "Id": supplier_id,

        "Name": supplier_name,

        "Contact Number": contact_number,

        "Company Name": company_name
    }


    suppliers.append(supplier)

    save_suppliers()

    print(
        "Supplier",
        supplier_name,
        "added successfully!"
    )


# ============================================================
# SELL MEDICINE AND GENERATE BILL
# ============================================================

def generate_bill():
    customer_name = input("Enter Customer Name: ")

    number_of_medicines = int(
        input("Enter number of medicines to buy: ")
    )

    bill_items = []
    grand_total = 0

    for i in range(number_of_medicines):

        medicine_id = int(input("Enter Medicine ID: "))

        quantity = int(input("Enter Quantity: "))

        # Find medicine
        medicine_found = False

        for medicine in medicines:

            if medicine["Id"] == medicine_id:

                medicine_found = True

                # Check stock
                if quantity > medicine["Quantity"]:
                    print(
                        f"Insufficient stock. "
                        f"Available quantity: {medicine['Quantity']}"
                    )
                    return

                # Calculate total for this medicine
                total = quantity * medicine["Price"]

                # Deduct stock
                medicine["Quantity"] -= quantity

                # Add item to bill
                bill_items.append({
                    "name": medicine["Name"],
                    "quantity": quantity,
                    "price": medicine["Price"],
                    "total": total
                })

                grand_total += total

                # Record sale
                sales.append({
                    "medicine_id": medicine["Id"],
                    "quantity": quantity,
                    "total": total,
                    "date": datetime.now().date()
                })

                break

        if not medicine_found:
            print("Medicine not found.")
            return

    # Save updated inventory and sales
    save_medicines()
    save_sales()

    # Display bill
    print("\nCustomer Bill -", customer_name)
    print("-" * 50)

    print(
        f"{'Medicine':<20}"
        f"{'Qty':<8}"
        f"{'Price':<10}"
        f"{'Total':<10}"
    )

    print("-" * 50)

    for item in bill_items:

        print(
            f"{item['name']:<20}"
            f"{item['quantity']:<8}"
            f"₹{item['price']:<9}"
            f"₹{item['total']:<9}"
        )

    print("-" * 50)

    print(f"Grand Total: ₹{grand_total}")

    print("\nDiscount Options")
    print("1.Percentage Discount")
    print("2. Flat Discount")

    discount_type=input("enter a discount option(1/2) : ")

    if discount_type =="1":
        discount_percentage=float(input("enter a percentage : "))

        discount_amount = (grand_total*discount_percentage/100)

    elif discount_type=="2":
        discount_amount=float("enter a fllat discount amount ")

    else:
        print("Invalid discount type")
        discount_amount=0

    if discount_amount>grand_total:
        discount_amount=grand_total

    final_amount= grand_total-discount_amount

    print(f"Grand Total     : ₹{grand_total:.2f}")
    print(f"Discount        : ₹{discount_amount:.2f}")
    print(f"Final Payable   : ₹{final_amount:.2f}")

    print("-" * 50)

    print("Sale recorded successfully!")


    

# ============================================================
# CALCULATE MONTHLY SALE
# ============================================================

def calculate_monthlysale():

    print("\n========== MONTHLY SALE ==========")

    month_date = input(
        "Enter Month (MM-YYYY): "
    )


    try:

        month_date = datetime.strptime(
            month_date.strip(),
            "%m-%Y"
        )

    except ValueError:

        print(
            "Invalid month. "
            "Please enter MM-YYYY."
        )

        return


    total_salevalue = 0


    for sale in sales:

        sale_month = sale["date"].strftime(
            "%m-%Y"
        )


        if (
            sale_month
            ==
            month_date.strftime("%m-%Y")
        ):

            total_salevalue += sale["total"]


    print(
        "Total sale for",
        month_date.strftime("%m-%Y"),
        ":",
        total_salevalue
    )


# ============================================================
# CREATE FILES AND LOAD EXISTING DATA
# ============================================================

create_csv_files()

load_data()


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n========================================")
    print("     PHARMACY INVENTORY SYSTEM")
    print("========================================")

    print("1. Add Medicine")
    print("2. Search Medicine")
    print("3. Update Medicine")
    print("4. Add Supplier")
    print("5. Sell Medicines & Generate Bill")
    print("6. Calculate Monthly Sale")
    print("7. Exit")

    print("========================================")


    choice = input(
        "Enter your choice: "
    )


    if choice == "1":

        add_medicine()


    elif choice == "2":

        search_medicine()


    elif choice == "3":

        update_medicine()


    elif choice == "4":

        add_supplier()


    elif choice == "5":

        generate_bill()


    elif choice == "6":

        calculate_monthlysale()


    elif choice == "7":

        print(
            "Exiting Pharmacy Inventory System. "
            "Goodbye!"
        )

        break


    else:

        print(
            "Invalid choice. Please try again."
        )