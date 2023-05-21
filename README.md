# PythonIPLocator
IP locator in python.

Certainly! Let's go through the code step by step and explain what it does and how it works:

1. Import the necessary libraries:
   
   import os
   import geoip2.database
  



2. Define the `locate_ip` function
3. 
   def locate_ip(ip_address):
       database_file = "GeoLite2-City.mmdb"  # Path to the GeoLite2 database file
       
  

   
3. Check if the database file exists:
   
   if not os.path.isfile(database_file):
       print("GeoLite2 database file not found.")
       return
   

   This code block checks if the GeoLite2-City database file exists at the specified path. If the file is not found, it prints an error message and returns from the function.

4. Read the database and retrieve location information:
   
   try:
       reader = geoip2.database.Reader(database_file)
       response = reader.city(ip_address)
       ...
   except geoip2.errors.AddressNotFoundError:
       print("IP address not found in the database.")
   except Exception as e:
       print(f"An error occurred: {str(e)}")
   

  
5. Extract and print location details:
   
   country = response.country.name
   city = response.city.name
   latitude = response.location.latitude
   longitude = response.location.longitude

   print(f"IP Address: {ip_address}")
   print(f"Location: {city}, {country}")
   print(f"Latitude: {latitude}")
   print(f"Longitude: {longitude}")
   

  

6. Close the reader:
   
   reader.close()
   

