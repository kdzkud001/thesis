import numpy as np
from fpdf import FPDF
import os
import cv2

def generate_cctag(tag_id, size=200):
    # This is a simplified CCTag generator and may not be fully accurate
    # For production use, consider using a dedicated CCTag library
    img = np.zeros((size, size), dtype=np.uint8)
    center = size // 2
    
    # Outer ring
    cv2.circle(img, (center, center), size//2 - 1, 255, 2)
    
    # Inner rings (simplified)
    for i in range(3):
        radius = size // 4 - i * (size // 16)
        cv2.circle(img, (center, center), radius, 255, 2)
    
    # "Cuts" in the rings (simplified representation of CCTag structure)
    angle = (tag_id % 8) * 45  # 8 possible positions, 45 degrees apart
    end_x = int(center + (size//2 - 1) * np.cos(np.radians(angle)))
    end_y = int(center + (size//2 - 1) * np.sin(np.radians(angle)))
    cv2.line(img, (center, center), (end_x, end_y), 0, 4)

    return img

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
    # Generate CCTag image
    cctag_image = generate_cctag(marker_id, size=200)

    # Save image temporarily
    marker_file = f'cctag_{marker_id}.png'
    cv2.imwrite(marker_file, cctag_image)

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
pdf_output = "cctags_grid.pdf"
pdf.output(pdf_output)

print(f"PDF generated: {pdf_output}")
