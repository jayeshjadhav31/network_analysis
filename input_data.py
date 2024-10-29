import subprocess
import os

layers = ['campus_polygon.shp','green_areas.shp','constructions.shp','network_data.kml']

for layer in layers:
    # Define the ogr2ogr command as a string
    input_file = layer
    table_name = result = layer.split('.')[0]
    print(table_name)

    ogr_command = (
        'ogr2ogr -f "PostgreSQL" '
        'PG:"dbname=iit_bombay user=postgres password=postgres host=localhost port=5432" '
        f'"D:\\STUDY\\GNR605 Principles of GIS\\Project\\data\\{table_name}\\{input_file}" '
        f'-nln trial_schema.{table_name} -overwrite'
    )

    # Path to the OSGeo4W Shell
    osgeo4w_shell_path = r"C:\Program Files\QGIS 3.34.9\OSGeo4W.bat"

    # Create a temporary batch file to run the command
    with open("temp_command.bat", "w") as f:
        f.write(ogr_command)

    # Run the temporary batch file using OSGeo4W Shell
    result = subprocess.run([osgeo4w_shell_path, "temp_command.bat"], shell=True)

    # Clean up the temporary file
    os.remove("temp_command.bat")
