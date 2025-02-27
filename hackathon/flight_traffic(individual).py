import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Hackathon\DGCA_DATA.csv')

df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
df = df.sort_values('Month')
df = df.dropna()

def compare_weight_load_factor_with_other_factors(df):
    """
    Compares the Weight Load Factor % with other factors over time.

    Args:
    - df (pd.DataFrame): DataFrame containing the data.

    Returns:
    - None: Displays the comparison plot.
    """
    # Default columns
    time_column = 'Month'
    target_column = 'Weight Load Factor %'
    
    if time_column not in df.columns or target_column not in df.columns:
        print("Error: Required columns are missing.")
        return
    
    other_columns = [col for col in df.columns if col != target_column and col != time_column]

    # Convert time column to datetime
    df[time_column] = pd.to_datetime(df[time_column], errors='coerce')
    
    # Drop rows with NaN values
    df_clean = df.dropna(subset=[target_column] + other_columns + [time_column])

    # Group by time (month) and calculate the mean
    df_resampled = df_clean.groupby(df_clean[time_column].dt.to_period('M')).agg({target_column: 'mean', **{col: 'mean' for col in other_columns}})
    
    # Plot the trends
    plt.figure(figsize=(12, 8))
    plt.plot(df_resampled.index.astype(str), df_resampled[target_column], label=target_column, color='b')
    
    for col in other_columns:
        plt.plot(df_resampled.index.astype(str), df_resampled[col], label=col)
    
    plt.title(f'Comparison of {target_column} with Other Factors Over Time')
    plt.xlabel('Month')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def compare_cargo_vs_passengers(df):
    """
    Compares trends in Total Cargo (CC) versus Total Passengers over time.
    """
    cargo_column = 'Total CC'
    passenger_column = 'No Carried(P)'
    time_column = 'Month'
    
    if not all(col in df.columns for col in [cargo_column, passenger_column, time_column]):
        print("Error: Required columns are missing.")
        return
    
    df[time_column] = pd.to_datetime(df[time_column], errors='coerce')
    df_clean = df.dropna(subset=[cargo_column, passenger_column, time_column])
    df_resampled = df_clean.groupby(df_clean[time_column].dt.to_period('M')).agg({cargo_column: 'sum', passenger_column: 'sum'})
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_resampled.index.astype(str), df_resampled[cargo_column], label='Total Cargo', color='b')
    plt.plot(df_resampled.index.astype(str), df_resampled[passenger_column], label='Total Passengers', color='g')
    plt.title('Comparison of Total Cargo and Passengers Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total (Cargo / Passengers)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def compare_flight_delays_with_load_factor(df):
    """
    Compares trends in Flight Delays with Load Factor over time.
    If delay data isn't available, only plots Load Factor trends.
    """
    load_factor_column = 'Weight Load Factor %'
    time_column = 'Month'
    
    # Check if necessary columns exist
    if load_factor_column not in df.columns or time_column not in df.columns:
        print("Error: Required columns are missing.")
        return

    # Convert the 'Month' column to datetime
    df[time_column] = pd.to_datetime(df[time_column], errors='coerce')
    df_clean = df.dropna(subset=[load_factor_column, time_column])

    # Resample data by month
    df_resampled = df_clean.groupby(df_clean[time_column].dt.to_period('M')).agg({load_factor_column: 'mean'})

    # Plotting Load Factor
    plt.figure(figsize=(10, 6))
    plt.plot(df_resampled.index.astype(str), df_resampled[load_factor_column], label='Load Factor (%)', color='b')
    plt.title('Load Factor Over Time')
    plt.xlabel('Month')
    plt.ylabel('Load Factor (%)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def display_menu():
    print("\nAviation Data Analysis Menu:")
    print("1. Compare Weight Load Factor with Other Factors")
    print("2. Compare Cargo vs Passengers Trends")
    print("3. Compare Flight Delays with Load Factor")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        match choice:
            case '1':
                compare_weight_load_factor_with_other_factors(df)
            case '2':
                compare_cargo_vs_passengers(df)
            case '3':
                compare_flight_delays_with_load_factor(df)
            case '0':
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please select a number between 0 and 15.")

if __name__ == "__main__":
    main()

