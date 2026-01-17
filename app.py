import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

sns.set_style("whitegrid")
sns.set_palette("Set2")

# -----------------------------
# Title
# -----------------------------
st.markdown(
    "<h1 style='text-align: center;'>🚲 Bike Sharing Interactive Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Explore patterns in bike rentals using time and weather factors</p>",
    unsafe_allow_html=True
)
st.divider()

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("traindataset.csv")
df["datetime"] = pd.to_datetime(df["datetime"])

# -----------------------------
# Feature engineering
# -----------------------------
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour
df["day_of_week"] = df["datetime"].dt.day_name()

df["total_count"] = df["casual"] + df["registered"]

season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_map = {1: "Clear", 2: "Mist", 3: "Light Snow/Rain", 4: "Heavy Rain"}

df["season_name"] = df["season"].map(season_map)
df["weather_name"] = df["weather"].map(weather_map)

def day_period(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

df["day_period"] = df["hour"].apply(day_period)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("🎛 Filters")

metric = st.sidebar.selectbox(
    "Choose metric",
    ["total_count", "casual", "registered"]
)

year_filter = st.sidebar.multiselect(
    "Select Year",
    sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)

season_filter = st.sidebar.multiselect(
    "Select Season",
    df["season_name"].unique(),
    default=df["season_name"].unique()
)

hour_filter = st.sidebar.slider(
    "Hour Range",
    0, 23, (0, 23)
)

working_day_option = st.sidebar.selectbox(
    "Working day filter",
    ["All", "Working day only", "Weekend/Holiday only"]
)

filtered_df = df[
    (df["year"].isin(year_filter)) &
    (df["season_name"].isin(season_filter)) &
    (df["hour"] >= hour_filter[0]) &
    (df["hour"] <= hour_filter[1])
]

if working_day_option == "Working day only":
    filtered_df = filtered_df[filtered_df["workingday"] == 1]
elif working_day_option == "Weekend/Holiday only":
    filtered_df = filtered_df[filtered_df["workingday"] == 0]

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Rentals", f"{filtered_df['total_count'].sum():,}")
col2.metric("Average Hourly Rentals", int(filtered_df["total_count"].mean()))
col3.metric("Peak Hour", filtered_df.groupby("hour")["total_count"].mean().idxmax())

st.divider()

# -----------------------------
# Charts Row 1
# -----------------------------
col4, col5 = st.columns(2)

with col4:
    st.subheader("📈 Average by Hour")
    fig, ax = plt.subplots()
    filtered_df.groupby("hour")[metric].mean().plot(ax=ax)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Average")
    st.pyplot(fig)

with col5:
    st.subheader("🍩 Share by Season")
    season_data = filtered_df.groupby("season_name")[metric].sum()
    fig, ax = plt.subplots()
    ax.pie(
        season_data,
        labels=season_data.index,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"width": 0.4}
    )
    ax.axis("equal")
    st.pyplot(fig)

# -----------------------------
# Charts Row 2
# -----------------------------
col6, col7 = st.columns(2)

with col6:
    st.subheader("🌦 Average by Weather")
    fig, ax = plt.subplots()
    sns.barplot(
        x="weather_name",
        y=metric,
        data=filtered_df,
        errorbar=("ci", 95),
        ax=ax
    )
    ax.set_xlabel("Weather")
    ax.set_ylabel("Average")
    st.pyplot(fig)

with col7:
    st.subheader("🕒 By Day Period")
    fig, ax = plt.subplots()
    filtered_df.groupby("day_period")[metric].mean().plot(
        kind="bar", ax=ax
    )
    ax.set_xlabel("Day Period")
    ax.set_ylabel("Average")
    st.pyplot(fig)

# -----------------------------
# Chart A: Year comparison
# -----------------------------
st.subheader("📊 Year Comparison (2011 vs 2012)")
year_comparison = filtered_df.groupby(["year", "month"])[metric].mean().unstack()

fig, ax = plt.subplots(figsize=(10, 4))
year_comparison.plot(ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Average")
ax.legend(title="Year")
st.pyplot(fig)

# -----------------------------
# Stacked Bar
# -----------------------------
st.subheader("📌 Casual vs Registered by Season (Stacked)")
stack_data = filtered_df.groupby("season_name")[["casual", "registered"]].sum()

fig, ax = plt.subplots()
stack_data.plot(kind="bar", stacked=True, ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# -----------------------------
# Violin Plot
# -----------------------------
st.subheader("🎻 Distribution by Weather (Violin Plot)")
fig, ax = plt.subplots(figsize=(10, 4))
sns.violinplot(
    x="weather_name",
    y=metric,
    data=filtered_df,
    ax=ax
)
ax.set_xlabel("Weather")
ax.set_ylabel("Distribution")
st.pyplot(fig)

# -----------------------------
# Heatmap
# -----------------------------
st.subheader("🔥 Hour vs Day Heatmap")
pivot = filtered_df.pivot_table(
    values=metric,
    index="day_of_week",
    columns="hour",
    aggfunc="mean"
)

fig, ax = plt.subplots(figsize=(12, 4))
sns.heatmap(pivot, cmap="YlOrRd", ax=ax)
st.pyplot(fig)

# -----------------------------
# Rolling trend
# -----------------------------
st.subheader("📈 Trend Line (7-hour Rolling Average)")
trend = filtered_df.groupby("hour")[metric].mean().rolling(7).mean()

fig, ax = plt.subplots()
trend.plot(ax=ax)
ax.set_xlabel("Hour")
ax.set_ylabel("Rolling Avg")
st.pyplot(fig)

st.divider()

# -----------------------------
# Data Table
# -----------------------------
st.subheader("🧾 Data Table (Preview)")
st.dataframe(filtered_df.head(200))

# -----------------------------
# Download button
# -----------------------------
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_bike_data.csv",
    mime="text/csv"
)
