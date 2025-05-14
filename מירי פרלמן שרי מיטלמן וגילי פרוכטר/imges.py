from PIL import Image

try:
    # פתח את התמונה הצבעונית
    image_file = Image.open("convert_image.png")
    # המר לגווני אפור (שחור-לבן)
    gray_image = image_file.convert('L')
    # שמור את התמונה החדשה
    gray_image.save('result_gray.png')
    print("ההמרה הושלמה בהצלחה!")
    # הצג את התמונה החדשה
    gray_image.show()
except Exception as e:
    print(f"שגיאה: {e}")
