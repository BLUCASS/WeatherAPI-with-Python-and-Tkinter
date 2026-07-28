from weather_api import Api_management, User, Menu

def main():
    user = User()
    menu = Menu()
    city = user.get_city()
    api = Api_management(city)
    response = api.extract_climate_info()
    if response: 
        data = api.treating_response(response)
        menu.print_menu(data)

if __name__ == "__main__":
    main()