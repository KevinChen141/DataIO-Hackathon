import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Read data from CSV files
jan = pd.read_csv("Data-IO 2024 Dataset/January.csv")
feb = pd.read_csv("Data-IO 2024 Dataset/February.csv")
march = pd.read_csv("Data-IO 2024 Dataset/March.csv")
april = pd.read_csv("Data-IO 2024 Dataset/April.csv")
may = pd.read_csv("Data-IO 2024 Dataset/May.csv")
june = pd.read_csv("Data-IO 2024 Dataset/June.csv")
july = pd.read_csv("Data-IO 2024 Dataset/July.csv")
aug = pd.read_csv("Data-IO 2024 Dataset/August.csv")
sept = pd.read_csv("Data-IO 2024 Dataset/September.csv")
oct = pd.read_csv("Data-IO 2024 Dataset/October.csv")
nov = pd.read_csv("Data-IO 2024 Dataset/November.csv")
dec = pd.read_csv("Data-IO 2024 Dataset/December.csv")

# Combine data from all months
combined_data = pd.concat(
    [jan, feb, march, april, may, june, july, aug, sept, oct, nov, dec],
    ignore_index=True,
)


# Converts time data to specific time (hours, min, sec)
def convert_to_time(ride_time):
    converted_times = []
    for time in ride_time:
        datetime_object = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        converted_times.append(datetime_object)
    return converted_times


# Filter data based on rides for member
member_rides = combined_data[combined_data["member_casual"] == "member"]
member_ride_start_time = member_rides["started_at"]  # start time data
member_ride_end_time = member_rides["ended_at"]  # end time data

# Convert start and end times to datetime objects
member_ride_converted_start_time = convert_to_time(member_ride_start_time)
member_ride_converted_end_time = convert_to_time(member_ride_end_time)

# Calculate time differences for member rides
member_ride_durations = [
    (end - start).total_seconds() / 60  # Convert timedelta to minutes
    for start, end in zip(
        member_ride_converted_start_time, member_ride_converted_end_time
    )
]

# Member types of bike count
num_member_electric_bikes = member_rides[
    member_rides["rideable_type"] == "electric_bike"
].shape[0]
num_member_classic_bikes = member_rides[
    member_rides["rideable_type"] == "classic_bike"
].shape[0]


# Filter data based on rides for casual
casual_rides = combined_data[combined_data["member_casual"] == "casual"]
casual_ride_start_time = casual_rides["started_at"]
casual_ride_end_time = casual_rides["ended_at"]
casual_ride_converted_start_time = convert_to_time(casual_ride_start_time)
casual_ride_converted_end_time = convert_to_time(casual_ride_end_time)

num_casual_bikes_electric = casual_rides[
    casual_rides["rideable_type"] == "electric_bike"
].shape[0]
num_casual_bikes_classic = casual_rides[
    casual_rides["rideable_type"] == "classic_bike"
].shape[0]

casual_ride_durations = [
    (end - start).total_seconds() / 60
    for start, end in zip(
        casual_ride_converted_start_time, casual_ride_converted_end_time
    )
]


# Plot for types of bikes used based
# -------------------------------------
# labels = [
#     "Electric Bike (Member)",
#     "Classic Bike (Member)",
#     "Electric Bike (Casual)",
#     "Classic Bike (Casual)",
# ]
# counts = [
#     num_member_electric_bikes,
#     num_member_classic_bikes,
#     num_casual_bikes_electric,
#     num_casual_bikes_classic,
# ]
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# max_count = max(
#     max(num_member_electric_bikes, num_member_classic_bikes),
#     max(num_casual_bikes_electric, num_casual_bikes_classic),
# )

# labels_member = ["Electric Bike", "Classic Bike"]
# counts_member = [num_member_electric_bikes, num_member_classic_bikes]
# ax1.bar(labels_member, counts_member, color=["blue", "green"])
# ax1.set_title("Member Rides")
# ax1.set_xlabel("Bike Type")
# ax1.set_ylabel("Count (millions)")
# ax1.set_ylim(0, max_count + 100000)

# labels_casual = ["Electric Bike", "Classic Bike"]
# counts_casual = [num_casual_bikes_electric, num_casual_bikes_classic]
# ax2.bar(labels_casual, counts_casual, color=["orange", "red"])
# ax2.set_title("Casual Rides")
# ax2.set_xlabel("Bike Type")
# ax2.set_ylabel("Count (millions)")
# ax2.set_ylim(0, max_count + 100000)

# plt.tight_layout()
# plt.show()


# Bar plot for number of rides by user
# -------------------------------------
# categories = ["Member", "Casual"]
# num_member_rides = len(member_rides)
# num_casual_rides = len(casual_rides)
# ride_counts = [num_member_rides, num_casual_rides]

# plt.bar(categories, ride_counts, color=["blue", "green"])
# plt.xlabel("User Type")
# plt.ylabel("Number of Rides (millions)")
# plt.title("Number of Rides by User Type")
# plt.show()


# Plotting for average usage duration by user type
# -------------------------------------
# plt.bar(
#     ["Member", "Casual"],
#     [
#         sum(member_ride_durations) / len(member_ride_durations),
#         sum(casual_ride_durations) / len(casual_ride_durations),
#     ],
#     color=["blue", "green"],
# )
# plt.xlabel("User Type")
# plt.ylabel("Average Ride Duration (minutes)")
# plt.title("Average Ride Duration by User Type")
# plt.show()


# Plotting both histograms side by side
# -------------------------------------
# fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# # Member ride durations vs number of rides for members
# axs[0].hist(
#     member_ride_durations,
#     bins=range(0, 125 + 5, 5),
#     color="blue",
#     edgecolor="black",
# )
# axs[0].set_xlabel("Ride Duration (minutes)")
# axs[0].set_ylabel("Number of Rides (millions)")
# axs[0].set_title("Number of Member Rides by Duration")

# # Member ride durations vs number of rides for casual
# axs[1].hist(
#     casual_ride_durations,
#     bins=range(0, 125 + 5, 5),
#     color="green",
#     edgecolor="black",
# )
# axs[1].set_xlabel("Ride Duration (minutes)")
# axs[1].set_ylabel("Number of Rides (millions)")
# axs[1].set_title("Number of Casual Rides by Duration")

# # Set the same y-axis range for both plots
# axs[1].set_ylim(axs[0].get_ylim())

# plt.tight_layout()
# plt.show()
