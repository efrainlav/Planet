import argparse
import rasterio
from rasterio.mask import mask
import json
import numpy as np

def clip_image_to_polygon(image_path, bounds_path, output_path, proj=None):
    try:
        polygon_mask = None  # Initialize the polygon mask variable
        # Open the image file
        with rasterio.open(image_path) as src:
            # Read the GeoJSON file
            with open(bounds_path) as f:
                bounds_geojson = json.load(f)

            # Extract the geometry from the GeoJSON file
            geometry = bounds_geojson['features'][0]['geometry']

            # Clip the image to the polygon
            clipped_image, clipped_transform = mask(src, [geometry], crop=True)

            # Create a boolean mask indicating pixels inside the polygon
            polygon_mask = np.any(clipped_image, axis=0)

            # Calculate the NDVI
            red_band = clipped_image[2, :, :]  # Assuming red is band 3
            nir_band = clipped_image[3, :, :]  # Assuming NIR is band 4
            ndvi = (nir_band.astype(float) - red_band.astype(float)) / (nir_band.astype(float) + red_band.astype(float))


            # Apply the mask to the NDVI to assign non-zero values to areas outside the polygon
            ndvi[~polygon_mask] = -9999  # You can adjust the value to assign outside the polygon


            # Update metadata for the clipped image
            clipped_meta = src.meta.copy()
            clipped_meta.update({
                'height': clipped_image.shape[1],
                'width': clipped_image.shape[2],
                'transform': clipped_transform,
                'crs': src.crs if proj is None else rasterio.crs.CRS.from_string(proj),
                'driver': 'GTiff',
                'dtype': ndvi.dtype
            })

            # Write the clipped image to a new file
            with rasterio.open(output_path, 'w', **clipped_meta) as dst:
                dst.write(clipped_image)

            print(f"Clipped image saved to {output_path}")

            # Update metadata for the NDVI image
            ndvi_meta = clipped_meta.copy()
            ndvi_meta.update({
                'count': 1,
                'dtype': 'float32'
            })

            # Save the NDVI as a separate image
            ndvi_output_path = output_path.replace('.tif', '_ndvi.tif')
            with rasterio.open(ndvi_output_path, 'w', **ndvi_meta) as ndvi_dst:
                ndvi_dst.write(ndvi.astype(np.float32), 1)

            print(f"NDVI image saved to {ndvi_output_path}")

    except Exception as e:
        print(f"Error occurred while clipping image: {str(e)}")

if __name__ == "__main__":
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='Clip GeoTIFF image to bounding polygon')
    parser.add_argument('--image', type=str, help='Path to the GeoTIFF image file')
    parser.add_argument('--bounds', type=str, help='Path to the GeoJSON bounds file')
    parser.add_argument('--output', type=str, help='Path to save the clipped image')
    parser.add_argument('--proj', type=str, default=None, help='EPSG code for the output projection')
    args = parser.parse_args()

    # Clip the image to the polygon
    clip_image_to_polygon(args.image, args.bounds, args.output, args.proj)
