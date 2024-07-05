"""
This module provides functionality to generate 
a population dictionary from a CSV file 
and visualize the data using matplotlib.
"""
import csv
import matplotlib.pyplot as plt
import mplcursors


def generate_population_dictionary(filename):
    """
    Generate dictionary from csv file.

    Returns a dictionary following the structure:
    {
        "Africa": { 
            "population": [100, 200, 300, ...], 
            "years": [1990, 2000, 2010, ...]
        }, 
        ...
    }
    """
    output_dictionary = {}
    try:
        with open(filename, "r", encoding="utf-8")  as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                continent = line["continent"]
                year = int(line["year"])
                population = int(line["population"])

                if continent not in output_dictionary:
                    output_dictionary[continent] = {'population': [], 'year': []}
                output_dictionary[continent]['population'].append(population)
                output_dictionary[continent]['year'].append(year)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return {}
    return output_dictionary


def generate_chart_from_dictionary(population_dictionary):
    """
    Generates line chart with data from a dictionary.
    One plot per continent.
    """
    for continent in population_dictionary:
        years = population_dictionary[continent]['year']
        population = population_dictionary[continent]['population']

        plt.plot(years, population, label=continent, marker="o", alpha=0.6)

    plt.style.use('fivethirtyeight')

    plt.title("Number of people using the Internet", size=16, fontweight='bold')
    plt.xlabel("Year")
    plt.ylabel("Population in billions")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    # Add mplcursors for interactive tooltips
    cursor = mplcursors.cursor(hover=True)
    cursor.connect(
        "add", lambda sel: sel.annotation.set_text(
            f'Year: {int(sel.target[0])}\nPopulation: {int(sel.target[1]):,}'))

    plt.show()


if __name__ == "__main__":
    # Store Internet users per country
    FILE_NAME = "data.csv"

    # Transform csv data
    population_per_continent = generate_population_dictionary(FILE_NAME)

    # Generate chart if data is successfully loaded
    if population_per_continent:
        generate_chart_from_dictionary(population_per_continent)
