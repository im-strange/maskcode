
class MaskCode:
  def __init__(self, picture):
    self.file = picture

  def embedd(self, content):
    with open(self.file, "ab") as main:
      content = content.encode("utf-8")
      main.write(content)
      main.close()

  def extract(self):
    with open(self.file, "rb") as main:
      content = main.read()
      added = content.index(bytes.fromhex("FFD9")) + 2
      main.seek(added)
      return main.read()

  def reset(self):
    with open(self.file, "rb") as main:
      content = main.read()
      offset = content.index(bytes.fromhex("FFD9")) + 2
    with open(self.file, "r+") as main:
      main.seek(offset)
      main.truncate()

  def execute(self):
    codes = (self.extract()).decode()
    exec(codes)
