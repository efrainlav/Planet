## Clip GeoTIFF Image to Bounding Polygon

This script allows you to clip a GeoTIFF image using a specified bounding polygon defined in a GeoJSON file. It also calculates the Normalized Difference Vegetation Index (NDVI) within the polygon region.

### Requirements

- Python 3.x
- `argparse`, `rasterio`, and `numpy` libraries

### Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:

```shell
pip install argparse rasterio numpy
```

3. Prepare your GeoTIFF image file and GeoJSON bounds file.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the script with the following command:

```shell
python script.py --image path/to/image.tif --bounds path/to/bounds.geojson --output path/to/output.tif
```

Replace `path/to/image.tif` with the path to your GeoTIFF image file, `path/to/bounds.geojson` with the path to your GeoJSON bounds file, and `path/to/output.tif` with the desired path to save the clipped image.

### Explanation

The script performs the following steps:

1. Imports the necessary libraries (`argparse`, `rasterio`, `json`, and `numpy`).
2. Defines a function `clip_image_to_polygon` that takes the image path, bounds path, output path, and an optional projection parameter.
3. The function initializes the `polygon_mask` variable.
4. Opens the image file using `rasterio.open` and reads the GeoJSON file using `open` and `json.load`.
5. Extracts the geometry from the GeoJSON file.
6. Clips the image to the polygon using `rasterio.mask.mask` and obtains the clipped image and its transform.
7. Creates a boolean mask indicating pixels inside the polygon.
8. Calculates the NDVI using the red and NIR bands of the clipped image.
9. Applies the mask to the NDVI to assign non-zero values to areas outside the polygon.
10. Updates the metadata for the clipped image, including height, width, transform, CRS, driver, and data type.
11. Writes the clipped image to a new file using `rasterio.open` and `write`.
12. Updates the metadata for the NDVI image, specifying the number of bands and data type.
13. Saves the NDVI as a separate image using `rasterio.open` and `write`.
14. If an exception occurs, it prints an error message.
15. If the script is executed directly (not imported), it parses the command-line arguments using `argparse.ArgumentParser`.
16. Calls the `clip_image_to_polygon` function with the provided command-line arguments.

You can customize the script by adjusting the parameters and uncommenting/commenting specific lines to modify the processing steps, such as normalizing the NDVI range.

**Note**: Make sure to replace `script.py` with the actual filename if you rename the script file.
