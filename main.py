import seaborn as sns
def load_data():
    df = sns.load_dataset("titanic")
    print("Data loaded:", df.shape)
    return df

def clean_data(df):
    df = df.drop(columns=["deck"])
    df["age"] = df["age"].fillna(df["age"].median())
    df = df.dropna(subset=["embarked", "embark_town"])
    df = df.drop_duplicates()
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    print("Data cleaned:", df.shape)
    return df

def analyze(df):
    results = {}
    results["Total passengers"] = len(df)
    results["Overall survival rate (%)"] = round(df["survived"].mean() * 100, 2)
    results["Survival by sex"] = df.groupby("sex")["survived"].mean().round(2).to_dict()
    results["Survival by class"] = df.groupby("pclass")["survived"].mean().round(2).to_dict()
    results["Average age"] = round(df["age"].mean(), 1)
    results["Average fare"] = round(df["fare"].mean(), 2)
    return results

import matplotlib.pyplot as plt
def make_charts(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="pclass", hue="survived", data=df)
    plt.title("Survival by Passenger Class")
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.barplot(x="sex", y="survived", data=df)
    plt.title("Survival Rate by Sex")
    plt.show()

    plt.figure(figsize=(6, 4))
    plt.hist(df["age"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Passengers")
    plt.show()


def save_report(results):
    with open("report.txt", "w") as f:
        f.write("TITANIC DATA ANALYSIS REPORT\n")
        f.write("=" * 30 + "\n")

        for key, value in results.items():
            f.write(f"{key}: {value}\n")

    print("Report saved as report.txt")

df = load_data()
df = clean_data(df)

results = analyze(df)

for key, value in results.items():
    print(key, ":", value)

make_charts(df)
save_report(results)

df.to_csv("cleaned_titanic.csv", index=False)

print("Project completed successfully!")