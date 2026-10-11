import pandas as pd

import hw_4_1_classes


def creating_store_from_excel(file_path: str):
    stocks = hw_4_1_classes.Stock()
    products_list = []
    customers_list = []

    df_products = pd.read_excel(file_path, sheet_name="Товари")
    for _, row in df_products.iterrows():
        product = hw_4_1_classes.Product(
            prod_id=int(row["ID"]),
            name=str(row["Назва"]),
            price=float(row["Ціна"])
        )
        products_list.append(product)
        stocks.change_quantity(product, int(row["Кількість"]))

    df_customers = pd.read_excel(file_path, sheet_name="Клієнти")
    for _, row in df_customers.iterrows():
        customer = hw_4_1_classes.Customer(
            last_name=str(row["Прізвище"]),
            first_name=str(row["Ім'я"]),
            phone_number=str(row["Телефон"]),
            email=str(row["e-mail"]),
        )
        customers_list.append(customer)
    return stocks, products_list, customers_list


if __name__ == "__main__":
    stock, products, customers = creating_store_from_excel("shop_data_for_hw4.xlsx")

    customer_1 = customers[0]
    product_1 = products[0]

    print(customer_1)

    new_order = hw_4_1_classes.Order()
    new_order.add_order_to_cart(product_1, 2, stock)

    customer_1.add_order_to_history(new_order)

    print(customer_1)
