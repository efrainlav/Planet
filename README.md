## Clip GeoTIFF Image to Bounding Polygon

This script allows to clip a GeoTIFF image using a specified bounding polygon defined in a GeoJSON file. It also calculates the Normalized Difference Vegetation Index (NDVI) within the polygon region.

Sample Input:  
● [T11SLU_20200925T183121_4Band_clip.tif](https://hello.planet.com/data/s/gH7JSoEgK4gP3Qd)  
● [bounds.geojson](https://hello.planet.com/data/s/dyKCqHJQFyCgfEA)

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

### Example Usage
```shell
clip_image.py --image T11SLU_20200925T183121_4Band_clip.tif --bounds bounds.geojson --output result.tif
```

### Optional Projection (--proj)
The script provides an optional --proj argument that allows you to specify the EPSG code for the output projection. If you want the clipped image to be in a specific projection, you can provide the EPSG code using this argument.

Here's how you can use the --proj option:

```shell
clip_image.py --image T11SLU_20200925T183121_4Band_clip.tif --bounds bounds.geojson --output result.tif --proj EPSG:4326
```
Replace EPSG:4326 with the desired EPSG code for the output projection. If you don't specify the --proj option, the script will use the same projection as the input image.

Make sure to use the appropriate EPSG code for your desired projection. You can find EPSG codes for different coordinate reference systems (CRS) in the EPSG Geodetic Parameter Registry or consult the documentation of the CRS you want to use.

