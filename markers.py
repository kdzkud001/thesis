import cv2
import numpy as np
from fpdf import FPDF
import os

# Check OpenCV version
print(f"OpenCV version: {cv2.__version__}")

# ArUco Dictionary (latest syntax)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

# Marker size (5cm = 50mm)
marker_size_mm = 50

# PDF setup
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# Calculate grid layout
page_width = 210  # A4 width in mm
page_height = 297  # A4 height in mm
margin = 10  # margin in mm
columns = 2
rows = 5

# Calculate spacing
x_spacing = (page_width - 2 * margin - columns * marker_size_mm) / (columns - 1)
y_spacing = (page_height - 2 * margin - rows * marker_size_mm) / (rows - 1)

for marker_id in range(10):
    # Generate marker image
    marker_image = np.zeros((200, 200), dtype=np.uint8)
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, 200)

    # Save image temporarily
    marker_file = f'marker_{marker_id}.png'
    cv2.imwrite(marker_file, marker_image)

    # Calculate position
    row = marker_id // columns
    col = marker_id % columns
    x = margin + col * (marker_size_mm + x_spacing)
    y = margin + row * (marker_size_mm + y_spacing)

    # Add marker to PDF
    pdf.image(marker_file, x=x, y=y, w=marker_size_mm)

    # Remove temporary file
    os.remove(marker_file)

# Save the PDF
pdf_output = "aruco_markers_grid.pdf"
pdf.output(pdf_output)

print(f"PDF generated: {pdf_output}")
