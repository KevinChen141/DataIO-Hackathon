import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import FastMarkerCluster

jan = pd.read_csv("January.csv")
feb = pd.read_csv("February.csv")
mar = pd.read_csv("March.csv")
may = pd.read_csv("May.csv")
jun = pd.read_csv("June.csv")
jul = pd.read_csv("July.csv")
aug = pd.read_csv("August.csv")
sep = pd.read_csv("September.csv")
oct = pd.read_csv("October.csv")
nov = pd.read_csv("November.csv")
dec = pd.read_csv("December.csv")
apr = pd.read_csv("April.csv")

# df = apr;
# df.info();
df = pd.concat([jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec])

### FREQUENCIES OF START TIMES THROUGHOUT THE DAY
# df['started_at'] = pd.to_datetime(df['started_at'])

# Extract the hour component
df["hour"] = df["started_at"].dt.hour

# Group by hour and count occurrences
hourly_counts = df.groupby("hour").size()

plt.figure(figsize=(10, 6))
hourly_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Frequencies of Start Times Within Each Hour of the Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Frequency")
plt.xticks(
    range(24),
    [
        "12AM",
        "1AM",
        "2AM",
        "3AM",
        "4AM",
        "5AM",
        "6AM",
        "7AM",
        "8AM",
        "9AM",
        "10AM",
        "11AM",
        "12PM",
        "1PM",
        "2PM",
        "3PM",
        "4PM",
        "5PM",
        "6PM",
        "7PM",
        "8PM",
        "9PM",
        "10PM",
        "11PM",
    ],
    rotation=45,
)
plt.grid(axis="y", alpha=0.75)
plt.show()


###RUSH HOUR LOCATIONS
df.dropna(subset=["start_lat", "started_at", "start_station_name"], inplace=True)
df["started_at"] = pd.to_datetime(df["started_at"])
station_counts = df["start_station_name"].value_counts()
print(station_counts.nlargest().head())

# rush hour map
rush_hour_df = df[(df["started_at"].dt.hour >= 16) & (df["started_at"].dt.hour < 18)]
chicago_lat, chicago_lng = 41.8781, -87.6298
m = folium.Map(location=[chicago_lat, chicago_lng], zoom_start=5)
start_cluster = FastMarkerCluster(
    rush_hour_df[["start_lat", "start_lng"]].values.tolist()
).add_to(m)

m.save("rush_hour.html")
