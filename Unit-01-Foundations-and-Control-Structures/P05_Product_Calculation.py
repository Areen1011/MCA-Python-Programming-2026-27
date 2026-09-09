price1 = float(input("Enter the price of the first product: "))
quantity1 = int(input("Enter the quantity of the first product: "))

price2 = float(input("Enter the price of the second product: "))
quantity2 = int(input("Enter the quantity of the second product: "))

price3 = float(input("Enter the price of the third product: "))
quantity3 = int(input("Enter the quantity of the third product: "))

subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
discount = subtotal * 0.10
gst = (subtotal - discount) * 0.18
total_amount = subtotal - discount + gst

print("Subtotal: ", subtotal)
print("Discount (10%): ", discount)
print("GST (18%): ", gst)
print("Total Amount to be paid: ", total_amount)