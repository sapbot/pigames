

inf = 0

def scr(text):
  my_file = open("data/display.data", "w+")
  my_file.write("")
  my_file.close()
  
  my_file = open("data/display.data", "a+")
  my_file.write(text)
  my_file.close()
  
  print("edited file:")
  print(text)
  
def cls():
  my_file = open("data/cls.data", "w+")
  my_file.write("")
  my_file.close()
  
  my_file = open("data/cls.data", "a+")
  my_file.write("1")
  my_file.close()
  
  my_file = open("data/cls.data", "w+")
  my_file.write("")
  my_file.close()
  
  my_file = open("data/cls.data", "a+")
  my_file.write("0")
  my_file.close()
  print("cls")

