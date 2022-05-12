from imp import init_builtin
import pytesseract

def get_text(boxes):
    data = []
    for box in boxes:
        for [a,b] in box:
            print(x_init,y_init,x_final,y_final)
