import os
from datetime import datetime
import random
import string

# Function to generate unique transaction ID with payment method prefix and random code
def generate_transaction_id(payment_method):
    datetime_part = datetime.now().strftime('%Y%m%d%H%M%S')
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    prefix = payment_method.upper()[:3]  # Take first 3 letters of payment method
    return f"{prefix}{datetime_part}{random_part}"

# Function to get emoji based on payment method
def get_payment_emoji(payment_method):
    method = payment_method.lower()
    if method == 'cash':
        return '💵'
    elif method == 'card':
        return '💳'
    elif method == 'upi':
        return '📲'
    else:
        return '💰'  # default emoji

def generate_receipt():
    print("\n\033[96m=== Payment Receipt Generator ===\033[0m")

    # Collect payment details from the user
    payer_name = input("Enter Payer's Name            : ").strip()
    payment_amount = input("Enter Payment Amount (in ₹)   : ").strip()
    payment_method = input("Enter Payment Method (Cash/Card/UPI/Other): ").strip()

    # Automatically generate transaction ID based on payment method
    transaction_id = generate_transaction_id(payment_method)

    # Get emoji for payment method
    payment_emoji = get_payment_emoji(payment_method)

    # Get current date and time
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Create receipt content
    receipt_content = (
        f"------------------------------\n"
        f"         PAYMENT RECEIPT       \n"
        f"------------------------------\n"
        f"Date & Time     : {current_datetime}\n"
        f"Payer Name      : {payer_name}\n"
        f"Amount Paid     : ₹{payment_amount}\n"
        f"Payment Method  : {payment_method.upper()} {payment_emoji}\n"
        f"Transaction ID  : {transaction_id}\n"
        f"------------------------------\n"
        f"   THANK YOU FOR YOUR PAYMENT! 🎉\n"
        f"------------------------------\n"
    )

    # Display receipt on screen with color
    print("\n\033[93m" + receipt_content + "\033[0m")

    # Create 'receipts' folder if it doesn't exist
    if not os.path.exists("receipts"):
        os.makedirs("receipts")

    # Save receipt to a text file with timestamped filename inside 'receipts' folder
    filename = f"receipts/Receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(receipt_content)

    print(f"\033[92mReceipt has been saved as '{filename}'\033[0m\n")

if __name__ == "__main__":
    generate_receipt()
