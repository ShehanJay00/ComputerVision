import cv2

img = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)

while True:
    cv2.imshow('Puppy',img)

    # IF we've waited at least 1 ms AND we've pressed the Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break
    # == 27: This checks if the ASCII value of the pressed key is equal to 27, which corresponds to the "Esc" key.


cv2.destroyAllWindows()

# Goto the venv that you created , otherwise cv2 should be installed in your base environment

# The expression 0xFF represents the hexadecimal value FF, which is equal to 255 in decimal. In binary representation, FF is 11111111. This value is often used as a mask to extract the least significant 8 bits of a larger number.

# In the context of the code cv2.waitKey(1) & 0xFF, it's used to ensure that only the least significant 8 bits of the key event value returned by cv2.waitKey(1) are considered. This is because cv2.waitKey() may return a 32-bit integer representing the key event, but only the least significant 8 bits correspond to the ASCII value of the pressed key.