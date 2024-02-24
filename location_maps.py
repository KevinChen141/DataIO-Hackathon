import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

jan = pd.read_csv("Data-IO 2024 Dataset/January.csv")
feb = pd.read_csv("Data-IO 2024 Dataset/February.csv")
mar = pd.read_csv("Data-IO 2024 Dataset/March.csv")
apr = pd.read_csv("Data-IO 2024 Dataset/April.csv")
may = pd.read_csv("Data-IO 2024 Dataset/May.csv")
june = pd.read_csv("Data-IO 2024 Dataset/June.csv")
july = pd.read_csv("Data-IO 2024 Dataset/July.csv")
aug = pd.read_csv("Data-IO 2024 Dataset/August.csv")
sept = pd.read_csv("Data-IO 2024 Dataset/September.csv")
oct = pd.read_csv("Data-IO 2024 Dataset/October.csv")
nov = pd.read_csv("Data-IO 2024 Dataset/November.csv")
dec = pd.read_csv("Data-IO 2024 Dataset/December.csv")

combined_df = pd.concat([jan, feb, mar, apr, may, june, july, aug, sept, oct, nov, dec])
combined_df.dropna(subset=["start_lat"], inplace=True)
combined_df.dropna(subset=["end_lat"], inplace=True)

member_rides = combined_df[combined_df["member_casual"] == "member"]
casual_rides = combined_df[combined_df["member_casual"] == "casual"]


chicago_lat, chicago_lng = 41.8781, -87.6298
m = folium.Map(location=[chicago_lat, chicago_lng], zoom_start=5)

start_cluster = FastMarkerCluster(
    combined_df[["start_lat", "start_lng"]].values.tolist()
).add_to(m)
end_cluster = FastMarkerCluster(
    combined_df[["start_lat", "start_lng"]].values.tolist()
).add_to(m)
member_cluster = FastMarkerCluster(
    member_rides[["start_lat", "start_lng"]].values.tolist()
).add_to(m)
casual_cluster = FastMarkerCluster(
    casual_rides[["start_lat", "start_lng"]].values.tolist()
).add_to(m)


end_cluster = FastMarkerCluster(
    casual_rides[["end_lat", "end_lng"]].values.tolist()
).add_to(m)

m.save("index.html")
