import pandas as pd
from sklearn.linear_model import LinearRegression
import os

FILE_NAME = "utility_usage.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Month", "Usage"])
        df.to_csv(FILE_NAME, index=False)


def load_data():
    try:
        return pd.read_csv(FILE_NAME)
    except Exception as e:
        print("Error loading data:", e)
        return pd.DataFrame(columns=["Month", "Usage"])


def save_data(df):
    try:
        df.to_csv(FILE_NAME, index=False)
    except Exception as e:
        print("Error saving data:", e)


def add_usage():
    try:
        month = int(input("Enter Month: "))
        usage = float(input("Enter Usage: "))

        df = load_data()

        new_row = pd.DataFrame({
            "Month": [month],
            "Usage": [usage]
        })

        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)

        print("Data added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print("Error:", e)


def update_usage():
    try:
        month = int(input("Enter Month to Update: "))

        df = load_data()

        if month not in df["Month"].values:
            print("Month not found!")
            return

        new_usage = float(input("Enter New Usage: "))

        df.loc[df["Month"] == month, "Usage"] = new_usage

        save_data(df)

        print("Data updated successfully!")

    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print("Error:", e)


def view_data():
    try:
        df = load_data()

        if df.empty:
            print("No data available.")
        else:
            print("\nUtility Usage Records")
            print(df)

    except Exception as e:
        print("Error:", e)


def predict_usage():
    try:
        df = load_data()

        if len(df) < 2:
            print("Not enough data for prediction.")
            return

        X = df[["Month"]]
        y = df["Usage"]

        model = LinearRegression()
        model.fit(X, y)

        future_month = int(input("Enter Future Month: "))

        prediction = model.predict([[future_month]])

        print(
            f"Predicted Usage for Month {future_month}: "
            f"{prediction[0]:.2f}"
        )

    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print("Prediction Error:", e)


def menu():
    while True:
        print("\n===== Utility Usage Prediction Tool =====")
        print("1. Add Usage Data")
        print("2. Update Usage Data")
        print("3. View Usage Data")
        print("4. Predict Future Usage")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_usage()

        elif choice == "2":
            update_usage()

        elif choice == "3":
            view_data()

        elif choice == "4":
            predict_usage()

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    initialize_file()
    menu()