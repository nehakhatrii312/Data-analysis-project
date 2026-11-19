# 🚢 Titanic Data Analytics Project

## 📌 Project Overview

The **Titanic Data Analytics Project** is a Python-based data analysis project that explores the Titanic passenger dataset. It focuses on data collection, data cleaning, exploratory data analysis (EDA), and data visualization to identify patterns and insights related to passenger survival.

The project uses Python libraries such as Pandas, Seaborn, and Matplotlib to process data, calculate statistics, generate visualizations, and export reports.

## 🎯 Project Objectives

- Load and explore the Titanic dataset.
- Handle missing values and duplicate records.
- Perform data cleaning and preprocessing.
- Analyze passenger survival rates.
- Compare survival rates based on gender and passenger class.
- Visualize passenger age distribution.
- Generate an automated analysis report.
- Export the cleaned dataset into a CSV file.

## 🛠️ Technologies & Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| Seaborn | Statistical data visualization |
| Matplotlib | Creating charts and graphs |
| CSV | Exporting cleaned data |

## 📂 Project Structure

```text
Titanic-Data-Analytics/
│
├── main.py
├── report.txt
├── cleaned_titanic.csv
├── README.md
└── requirements.txt
```

## ⚙️ Project Workflow

### 1. Data Loading
- Loads the Titanic dataset using Seaborn.
- Displays the dataset dimensions.

### 2. Data Cleaning
- Removes the unnecessary `deck` column.
- Handles missing age values using the median.
- Removes rows with missing embarkation details.
- Removes duplicate records.
- Creates a new `family_size` feature.

### 3. Data Analysis
Calculates important statistics, including:
- Total number of passengers.
- Overall survival rate.
- Survival rate by gender.
- Survival rate by passenger class.
- Average passenger age.
- Average ticket fare.

### 4. Data Visualization

Creates three visualizations:

- **Survival by Passenger Class:** Compares survived and non-survived passengers across classes.
- **Survival Rate by Sex:** Compares survival rates between male and female passengers.
- **Age Distribution:** Displays the distribution of passenger ages using a histogram.

### 5. Report Generation
- Automatically generates a `report.txt` file.
- Saves the calculated analysis results.

### 6. Data Export
- Exports the cleaned dataset into `cleaned_titanic.csv`.
- Uses `index=False` to avoid saving an additional index column.

## 📊 Key Analysis Areas

- Passenger survival patterns.
- Gender-based survival comparison.
- Passenger class and survival relationship.
- Age distribution.
- Family size feature creation.

## 💻 Installation & Setup

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Navigate to the project folder**

```bash
cd Titanic-Data-Analytics
```

**Step 3: Install required libraries**

```bash
pip install -r requirements.txt
```

**Step 4: Run the project**

```bash
python main.py
```

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
pandas
seaborn
matplotlib
```

## 📁 Output Files

After successful execution, the project generates:

| File | Description |
|---|---|
| `report.txt` | Contains the analysis results |
| `cleaned_titanic.csv` | Contains the cleaned Titanic dataset |
| Charts | Displays three data visualizations |

## 📚 Learning Outcomes

Through this project, I practiced:

- Python functions and dictionaries.
- Data manipulation using Pandas.
- Handling missing and duplicate data.
- Grouping and statistical analysis.
- Data visualization using Seaborn and Matplotlib.
- File handling and report generation.
- Exporting datasets into CSV format.

## 👩‍💻 Author

**Neha Khatri**

BCA Student | Aspiring Software Developer

- GitHub: [nehakhatrii312](https://github.com/nehakhatrii312)
- LinkedIn: [Neha Khatri](https://www.linkedin.com/in/nehakhatri312)

---

⭐ If you find this project useful, feel free to explore the repository!

**Project developed for learning and practicing Python-based Data Analytics.**
