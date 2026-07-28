import tkinter as tk
from tkinter import messagebox
from weather_api import Api_management

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        root.title("Weather App")

        # City input
        tk.Label(root, text="City:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button
        self.search_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)
        self.city_entry.bind("<Return>", self.get_weather)

        # Output label
        self.output_label = tk.Label(root, text="", justify="left")
        self.output_label.grid(row=1, column=0, columnspan=3, padx=5, pady=10, sticky="w")

    def get_weather(self, event=None):
        city = self.city_entry.get().strip()
        if len(city) < 2:
            messagebox.showerror("Error", "Please enter a valid city.")
            return

        api = Api_management(city)
        response = api.extract_climate_info()
        if not response:
            messagebox.showerror("Error", "Could not get weather data.")
            return

        climate_info = api.treating_response(response)

        text = (
            f"City: {climate_info.city_name}\n"
            f"Region: {climate_info.region}\n"
            f"Country: {climate_info.country}\n\n"
            f"Date: {climate_info.date}  Hour: {climate_info.hour}\n\n"
            f"Chance of rain: {climate_info.chance_of_rain}%\n"
            f"Humidity: {climate_info.humidity}\n"
            f"Winds: {climate_info.winds} km/h\n\n"
            f"Condition: {climate_info.condition}\n"
            f"Current temperature: {climate_info.temperature}°C\n"
            f"Feels like: {climate_info.feels_like}°C"
        )
        self.output_label.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()