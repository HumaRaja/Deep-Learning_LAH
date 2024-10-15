import cv2

def crop_image(image, x, y, width, height):
  """Crops an image to a specified region.

  Args:
    image: The input image.
    x: The starting x-coordinate of the crop region.
    y: The starting y-coordinate of the crop region.
    width: The width of the crop region.
    height: The height of the crop region.

  Returns:
    The cropped image.
  """

  cropped_image = image[y:y+height, x:x+width]
  return cropped_image

# Example usage:
img = cv2.imread('Screenshots/q/q113.png')
cropped_img = crop_image(img, 100, 200, 300, 400)  # Adjust coordinates as needed
cv2.imshow('Cropped Image', cropped_img)