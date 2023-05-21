import os
import geoip2.database

def locate_ip(ip_address):
    database_file = "GeoLite2-City.mmdb"  # Path to the GeoLite2 database file

    if not os.path.isfile(database_file):
        print("GeoLite2 database file not found.")
        return

    try:
        reader = geoip2.database.Reader(database_file)
        response = reader.city(ip_address)

        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude

        print(f"IP Address: {ip_address}")
        print(f"Location: {city}, {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

        reader.close()
    except geoip2.errors.AddressNotFoundError:
        print("IP address not found in the database.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
ip_address = "8.8.8.8"  # Replace with the desired IP address
locate_ip(ip_address)
