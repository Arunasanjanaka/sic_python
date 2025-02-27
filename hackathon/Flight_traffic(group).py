import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Hackathon\DGCA_DATA.csv')

# Convert 'Month' to datetime format
df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
df = df.sort_values('Month')
df = df.dropna()

# Function to plot ASK vs Passenger Demand
def plot_ask_vs_passenger_demand(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Month'], df['Avail Seats Km(millions)'], label='ASK (millions)', marker='o', linestyle='-')
    plt.plot(df['Month'], df['Km Performed(Millions)(P)'], label='Passenger Demand (millions)', marker='s', linestyle='--')
    plt.xlabel("Month")
    plt.ylabel("Millions of Kilometers")
    plt.title("Available Seat Kilometers (ASK) vs Passenger Demand Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Function to analyze flight hours vs passengers carried
def plot_flight_hours_vs_passengers(df):
    correlation = df[['Hours (AF)', 'No Carried(P)']].corr()
    print("Correlation Matrix (Flight Hours vs. Passengers):\n", correlation)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Hours (AF)'], y=df['No Carried(P)'])
    plt.xlabel("Flight Hours")
    plt.ylabel("Passengers Carried")
    plt.title("Correlation Between Flight Hours and Passengers Carried")
    plt.grid(True)
    plt.show()

# Function to analyze freight trends over time
def plot_freight_trends(df):
    df['Year'] = df['Month'].dt.year
    df['Month_Num'] = df['Month'].dt.month
    pivot_freight = df.pivot_table(values='Freight TON KM Performed', index='Year', columns='Month_Num', aggfunc='sum')
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_freight, cmap="coolwarm", annot=True, fmt=".0f")
    plt.title("Freight Transport Trends (Heatmap)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.show()

# Function to analyze flight kilometers vs load factor
def analyze_flight_kilometers_vs_load_factor(df):
    if 'Kms (Thousands)(AF)' in df.columns and 'PAX load %' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Kms (Thousands)(AF)'], df['PAX load %'])
        plt.title('Correlation Between Flight Kilometers and Load Factor')
        plt.xlabel('Flight Kilometers (Thousands)')
        plt.ylabel('Passenger Load Factor (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        correlation = df['Kms (Thousands)(AF)'].corr(df['PAX load %'])
        print(f"Correlation between Flight Kilometers and Load Factor: {correlation}")
    else:
        print("Error: 'Kms (Thousands)(AF)' or 'PAX load %' column not found in the dataset.")

# Function to analyze total ton kilometers
def analyze_total_ton_kilometers(df):
    if 'Avail TONNE KMS (Millions)' in df.columns and 'Month' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.plot(df['Month'], df['Avail TONNE KMS (Millions)'], marker='o')
        plt.title('Total Ton-Kilometers Performance Over Time')
        plt.xlabel('Month')
        plt.ylabel('Available Tonne-Kilometers (Millions)')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Error: 'Avail TONNE KMS (Millions)' or 'Month' column not found in the dataset.")

# Function to analyze freight ton kilometers by month
def analyze_freight_months(df):
    if 'Freight TON KM Performed' in df.columns and 'Month' in df.columns:
        highest = df.loc[df['Freight TON KM Performed'].idxmax()]
        lowest = df.loc[df['Freight TON KM Performed'].idxmin()]

        print(f"Highest Freight Ton KM: {highest['Month']}")
        print(f"Lowest Freight Ton KM: {lowest['Month']}")

        plt.figure(figsize=(12, 6))
        plt.plot(df['Month'], df['Freight TON KM Performed'], marker='o', linestyle='-')
        plt.scatter([highest['Month'], lowest['Month']], [highest['Freight TON KM Performed'], lowest['Freight TON KM Performed']], 
                    color=['red', 'blue'], s=100, label="High/Low Points")

        plt.xlabel("Month")
        plt.ylabel("Freight TON KM Performed")
        plt.title("Freight Ton Kilometers Over Time")
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
    else:
        print("Missing required columns.")

def plot_flight_departures(df):
    """Plots the trend of flight departures over time."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Month', y='No. Departure (AF)', marker='o', color='b', linewidth=2)

    plt.title('Trend of Flight Departures Over Time', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Departures', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_pax_load_vs_seat_kms(df):
    """Plots the relationship between Passenger Load Factor and Available Seat Kilometers."""
    plt.figure(figsize=(12, 6))
    sns.regplot(x=df["Avail Seats Km(millions)"], y=df["PAX load %"], 
                scatter_kws={'color':'blue', 'alpha': 0.7},  
                line_kws={'color':'red', 'linewidth':2})  

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title("Passenger Load Factor vs Available Seat Kilometers", fontsize=14, fontweight='bold')
    plt.xlabel("Available Seat Kilometers (Millions)", fontsize=12)
    plt.ylabel("Passenger Load Factor (%)", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()


def plot_weight_load_factor(df):
    """Plots the fluctuation of Weight Load Factor over time."""
    plt.figure(figsize=(14, 6))
    plt.plot(df['Month'], df['Weight Load Factor %'], marker='o', linestyle='-', color='b', label='Weight Load Factor (%)')

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title("Fluctuation of Weight Load Factor (%) Over Time", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Weight Load Factor (%)", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def seasonal_pattern_in_cargo(df):
    if 'Month' in df.columns and 'Freight TON KM Performed' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Month', y='Freight TON KM Performed', data=df)
        plt.title('Seasonal Pattern in Cargo Transportation')
        plt.xlabel('Month')
        plt.ylabel('Freight TON KM Performed')
        plt.tight_layout()
        plt.show()
    else:
        print("Error: 'Month' or 'Freight TON KM Performed' column not found. Check Dataset.")

# Analysis 8: Months with Peak Passenger Traffic
def peak_passenger_traffic(df):
    if 'No Carried(P)' in df.columns and 'Month' in df.columns:
        peak_month = df.loc[df['No Carried(P)'].idxmax()]
        print('*' * 100)
        print(f"Month with Peak Passenger Traffic: {peak_month['Month']}")
        print('*' * 100)

    else:
        print("Error: 'No Carried(P)' or 'Month' column not found. Check dataset.")

# Analysis 9: Efficiency of Available Tonne-Kilometers
def efficiency_of_tonne_kilometers(df):
    if 'Avail TONNE KMS (Millions)' in df.columns and 'Total TON KMS Performed' in df.columns and 'Month' in df.columns:
        df['Efficiency'] = (df['Total TON KMS Performed'] / df['Avail TONNE KMS (Millions)']) * 100
        plt.figure(figsize=(10, 6))
        plt.plot(df['Month'], df['Efficiency'], marker='o')
        plt.title('Efficiency of Available Tonne-Kilometers')
        plt.xlabel('Month')
        plt.ylabel('Efficiency (%)')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Error: Either 'Avail TONNE KMS (Millions)', 'Total TON KMS Performed', or 'Month' column not found. Check dataset.")

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

def load_data():
    df = pd.read_csv('Hackathon/DGCA_DATA.csv')
    df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
    df = df.sort_values('Month').dropna()
    return df

def display_menu():
    print("\nAviation Data Analysis Menu:")
    print("1. Plot ASK vs Passenger Demand")
    print("2. Analyze Flight Hours vs Passengers Carried")
    print("3. Analyze Freight Trends Over Time")
    print("4. Analyze Flight Kilometers vs Load Factor")
    print("5. Analyze Total Ton Kilometers")
    print("6. Analyze Freight Ton Kilometers by Month")
    print("7. Plot Flight Departures Over Time")
    print("8. Plot Passenger Load Factor vs Available Seat Kilometers")
    print("9. Plot Weight Load Factor Over Time")
    print("10. Analyze Seasonal Patterns in Cargo")
    print("11. Identify Peak Passenger Traffic Month")
    print("12. Analyze Efficiency of Available Tonne-Kilometers")
    print("13. Compare Weight Load Factor with Other Factors")
    print("14. Compare Cargo vs Passengers Trends")
    print("15. Compare Flight Delays with Load Factor")
    print("0. Exit")

def main():
    df = load_data()
    while True:
        display_menu()
        choice = input("Enter your choice (0-15): ")
        
        match choice:
            case '1':
                plot_ask_vs_passenger_demand(df)
            case '2':
                plot_flight_hours_vs_passengers(df)
            case '3':
                plot_freight_trends(df)
            case '4':
                analyze_flight_kilometers_vs_load_factor(df)
            case '5':
                analyze_total_ton_kilometers(df)
            case '6':
                analyze_freight_months(df)
            case '7':
                plot_flight_departures(df)
            case '8':
                plot_pax_load_vs_seat_kms(df)
            case '9':
                plot_weight_load_factor(df)
            case '10':
                seasonal_pattern_in_cargo(df)
            case '11':
                peak_passenger_traffic(df)
            case '12':
                efficiency_of_tonne_kilometers(df)
            case '13':
                compare_weight_load_factor_with_other_factors(df)
            case '14':
                compare_cargo_vs_passengers(df)
            case '15':
                compare_flight_delays_with_load_factor(df)
            case '0':
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please select a number between 0 and 15.")

if __name__ == "__main__":
    main()
