#Ευαγγελος Τσιμουρτος 2118123
#Διευθυνση του Data set https://www.kaggle.com/datasets/jennyzzhu/vancouver-house-prices-for-past-20-years
#Τρεχουμε το προγραμμα και βαζουμε την διευθυνση που βρισκεται το DataSet στον υπολογιστει μας , στο πεδιο που μας ζηταται 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Συνάρτηση: Φόρτωση δεδομένων από CSV
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Επιτυχής φόρτωση δεδομένων από {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Σφάλμα: Το αρχείο {file_path} δεν βρέθηκε.")
        return None
    except Exception as e:
        print(f"Σφάλμα κατά τη φόρτωση του αρχείου: {e}")
        return None

# Συνάρτηση: Πρόβλεψη μελλοντικής τιμής
def predict_future_price(data):
    # Δημιουργία χαρακτηριστικών (X) και τιμών στόχου (y)
    X = np.array(data[['Square Footage (House)', 'Bedrooms']])
    y = np.array(data['Market Price'])
    
    # Εκπαίδευση μοντέλου
    model = LinearRegression()
    model.fit(X, y)
    print("\nΜοντέλο εκπαίδευσης ολοκληρώθηκε.\n")

    # Εισαγωγή νέων δεδομένων για πρόβλεψη
    try:
        PROPERTYSQFT = float(input("Εισάγετε τ.μ. για πρόβλεψη: "))
        Bedrooms = int(input("Εισάγετε αριθμό δωματίων για πρόβλεψη: "))
        predicted_price = model.predict([[PROPERTYSQFT, Bedrooms]])
        print(f"Η προβλεπόμενη τιμή είναι: {predicted_price[0]:,.2f} €")
        return predicted_price[0]
    except ValueError:
        print("Σφάλμα: Μη έγκυρη είσοδος.")
        return None

# Συνάρτηση: Προβολή ιστορικών τιμών και γραφημάτων
def compare_prices(data, future_price=None):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Market Price'], label='Ιστορικές Τιμές', marker='o')
    if future_price:
        plt.axhline(y=future_price, color='red', linestyle='--', label='Προβλεπόμενη Τιμή')
    plt.title("Σύγκριση Τιμών Ακινήτου")
    plt.xlabel("Χρόνος")
    plt.ylabel("Τιμή (€)")
    plt.legend()
    plt.grid()
    plt.show()

# Κύριο Μενού
def main():
    print("Καλώς ήρθατε στο σύστημα παρακολούθησης τιμών ακινήτων!")
    file_path = input("Εισάγετε το όνομα του αρχείου δεδομένων (π.χ. real_estate_data.csv): ")
    data = load_dataset(file_path)

    if data is None:
        print("Δεν ήταν δυνατή η φόρτωση του dataset. Τερματισμός.")
        return

    while True:
        print("\n--- Μενού ---")
        print("1. Προβολή δεδομένων")
        print("2. Προβολή ιστορικών τιμών")
        print("3. Πρόβλεψη μελλοντικής τιμής")
        print("4. Έξοδος")
        choice = input("Επιλέξτε: ")

        if choice == "1":
            # Εμφάνιση δεδομένων
            print("\nΔεδομένα Ακινήτων:")
            print(data)
        elif choice == "2":
            # Προβολή ιστορικών τιμών
            compare_prices(data)
        elif choice == "3":
            # Πρόβλεψη μελλοντικής τιμής
            future_price = predict_future_price(data)
            if future_price:
                compare_prices(data, future_price=future_price)
        elif choice == "4":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή.")

if __name__ == "__main__":
    main()
