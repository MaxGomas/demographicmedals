import pandas as pd
import matplotlib.pyplot as plt


def plot_medals_tally(df):
    # Assuming df has columns 'Country', 'Gold', 'Silver', 'Bronze'
    countries = df['Country']
    gold = df['Gold']
    silver = df['Silver']
    bronze = df['Bronze']

    # Creating the stacked bar chart
    plt.bar(countries, gold, label='Gold', color='gold')
    plt.bar(countries, silver, bottom=gold, label='Silver', color='silver')
    plt.bar(countries, bronze, bottom=gold+silver, label='Bronze', color='#cd7f32')

    # Add the number of medals in the center of each bar
    for i, (g, s, b) in enumerate(zip(gold, silver, bronze)):
        plt.text(i, g/2, str(g), ha='center', va='center', color='black')
        plt.text(i, g + s/2, str(s), ha='center', va='center', color='black')
        plt.text(i, g + s + b/2, str(b), ha='center', va='center', color='black')

    plt.xlabel('Country')
    plt.ylabel('Medals')
    plt.title('Medals Tally')
    plt.legend()

    plt.xticks(rotation=90, ha='right')  # Rotate country names for better readability and align them to the right
    plt.tight_layout()  # Adjust the spacing between subplots to prevent overlapping
    plt.show()

def plot_medals_vs_medals_per_million(df):
    # Create the scatter plot
    plt.figure(figsize=(10, 6))  # Optional: Adjust figure size for better readability
    plt.scatter(df['medal per million inhabitants'], df['Total'], color='blue')

    # Annotate each point with the country name
    for i, txt in enumerate(df['Country']):
        plt.annotate(txt, 
                     (df['medal per million inhabitants'].iat[i], df['Total'].iat[i]),
                     xytext=(5, 5),  # Offset the text by 5 points right and 5 points up
                     textcoords='offset points')

    plt.xlabel('Medal per Million Inhabitants')
    plt.ylabel('Total Medals')
    plt.title('Total Medals vs. Medal per Million Inhabitants')
    plt.grid(True)  # Optional: Add grid for better readability
    plt.show()


def main():
    # Assuming "medalsTally.csv" is in the current working directory
    df = pd.read_csv("medalsTally.csv")

    # Ensure 'Total' and 'Population (2023)' are numeric
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce')
    df['Population (2023)'] = pd.to_numeric(df['Population (2023)'].str.replace(',', ''), errors='coerce')
    # Assuming the DataFrame has columns 'Total' for total medals and 'Population (2023)' for population
    df['medal per million inhabitants'] = (df['Total'] / df['Population (2023)']) * 1_000_000
    print(df)
    plot_medals_tally(df)
    plot_medals_vs_medals_per_million(df)

if __name__ == "__main__":
    main()
