import pyautogui

width, height = pyautogui.size()


try:
  print(f"Ana Ekran Çözünürlüğü: {width}x{height}")
  xdef,ydef = width / 1.23  , height / 1.23
  xdefmov , ydefmove = width/10  , height/15
except ZeroDivisionError:
  print("Çözünürlük bulunamadı.")
  breakpoint()
except ValueError:
  print("Bu çözünürlükte bir ekran oluşturulamadı.")
  breakpoint()
except:
  print("Bilinmeyen sorun meydana geldi.")
  breakpoint()