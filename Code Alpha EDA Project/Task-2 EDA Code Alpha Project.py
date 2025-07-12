# Netflix Titles EDA Project – Task 2
# CodeAlpha Internship – Exploratory Data Analysis





import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Set Seaborn theme
sns.set_theme(style="whitegrid", palette="pastel")

# Load dataset
df = pd.read_csv("C:/Users/Sushant/Documents/Trae IDE/Internship Project/Code Alpha EDA Project/netflix_titles.csv")

# Data cleaning
df['director'] = df['director'].fillna("Not Specified")
df['country'] = df['country'].fillna("Unknown")
df.dropna(subset=['rating'], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year





# ---------- Visualization 1: Type Distribution ----------

plt.figure(figsize=(6, 4))
colors = sns.color_palette("Set2")
ax = df['type'].value_counts().plot(kind='bar', color=colors)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + 0.25, p.get_height() + 50))
plt.title("Netflix: Movies vs TV Shows", fontsize=14, fontweight='bold', color='darkblue')
plt.xlabel("Content Type", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("type_distribution.png")
plt.show()







# ---------- Visualization 2: Top 10 Countries ----------

plt.figure(figsize=(8, 6))
ax2 = df['country'].value_counts().head(10).plot(kind='barh', color='coral')
for i in ax2.patches:
    ax2.text(i.get_width() + 10, i.get_y() + 0.1, str(int(i.get_width())), fontsize=10)
plt.title("Top 10 Countries on Netflix", fontsize=14, fontweight='bold', color='darkgreen')
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.show()





# ---------- Visualization 3: Most Common Genres ----------

all_genres = ','.join(df['listed_in']).split(',')
genre_list = [g.strip() for g in all_genres]
genre_count = Counter(genre_list)
top_genres = dict(genre_count.most_common(10))

plt.figure(figsize=(10, 5))
ax3 = plt.bar(top_genres.keys(), top_genres.values(), color='mediumpurple')
plt.title("Most Common Genres on Netflix", fontsize=14, fontweight='bold', color='purple')
plt.ylabel("Count")
plt.xticks(rotation=45)
for i, v in enumerate(top_genres.values()):
    plt.text(i, v + 5, str(v), ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig("common_genres.png")
plt.show()





# ---------- Visualization 4: Content Added Per Year ----------

plt.figure(figsize=(12, 6))
year_counts = df['year_added'].value_counts().sort_index()
ax4 = year_counts.plot(kind='bar', color='teal')
plt.title("Content Added to Netflix by Year", fontsize=14, fontweight='bold', color='teal')
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
for p in ax4.patches:
    ax4.annotate(str(p.get_height()), (p.get_x() + 0.1, p.get_height() + 10), fontsize=9)
plt.tight_layout()
plt.savefig("content_added_per_year.png")
plt.show()
