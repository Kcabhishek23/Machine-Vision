import cv2
from datetime import date

# Load RoboDK snapshot
img = cv2.imread("images/task-b1-result.png")

if img is None:
    print("Error: Image not found")
    exit()

# Print image shape
print("Image shape (H, W, C):", img.shape)

# 🔴 Red square annotation
cv2.rectangle(
    img,
    (236, 124),     # top-left
    (287, 176),     # bottom-right
    (255, 0, 0),    # red color (BGR)
    2
)

cv2.putText(
    img,
    "Green Tile",
    (225, 115),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 0, 255),
    2
)

# 🔵 Blue square annotation
cv2.rectangle(
    img,
    (347, 145),     # top-left
    (379, 178),     # bottom-right
    (0, 0, 255),    # blue color (BGR)
    2
)

cv2.putText(
    img,
    "Blue Part",
    (385, 180),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (255, 0, 0),
    2
)

# ✍ Name and date
text = "Abhishek KC - " + str(date.today())
cv2.putText(
    img,
    text,
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 0, 255),
    2
)

# Save and show result
cv2.imwrite("task-b2-result.png", img)
cv2.imshow("Annotated RoboDK Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
