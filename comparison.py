import matplotlib.pyplot as plt

# Update to include both YOLOv5n and YOLOv5s, and adjust text positioning
models = ["Haar Cascade", "MobileNet SSD", "TensorFlow Lite", "YOLOv5n", "YOLOv5s"]
speed = [8, 6, 5, 7, 3]  # Speed: Adjusted with both YOLOv5n and YOLOv5s
accuracy = [3, 6, 7, 8, 9]  # Accuracy: Adjusted with both YOLOv5n and YOLOv5s

# Create the updated scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(speed, accuracy, color=['red', 'blue', 'green', 'orange', 'purple'], s=100)

# Annotate each model with adjusted positioning for visibility
for i, model in enumerate(models):
    if model == "TensorFlow Lite":
        plt.text(speed[i], accuracy[i] - 0.2, model, fontsize=16, ha='right')  # Adjust TensorFlow placement
    elif model == "YOLOv5s":
        plt.text(speed[i], accuracy[i] - 0.2, model, fontsize=16, ha='left')  # Adjust YOLOv5s placement
    else:
        plt.text(speed[i], accuracy[i], model, fontsize=16, ha='right')

# Set axis labels and title
plt.xlabel("Speed (1 = Slow, 10 = Fast)", fontsize=14)
plt.ylabel("Accuracy (1 = Low, 10 = High)", fontsize=14)
plt.title("Comparison of Object Detection Models on Raspberry Pi", fontsize=16)

# Display the updated plot
plt.grid(True)
plt.show()
