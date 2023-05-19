# FS Interaction.
import os

class FileSystemObject:
  def handle(name, typeof, where, data=None):
    with open(self.where + self.name, self.typeof) as OpenFile:
      if self.typeof == 'wb' or 'w':
        self.OpenFile.write(self.data)
        return 'FileSystemObject: Created : ' + self.name + ' at : ' + self.where + self.name
      if self.typeof == 'rb' or 'r':
        self.Data = self.OpenFile.read()
        return self.Data
  def delete(file):
    os.remove(self.file)
  def copy(file1, file2):
    os.cp(file1, file2)

  # I will finish that later, unless someone edits it before, in case. Here is the meaning of this : 
  """
  Interacting with Filesystem.
  Future functions :
  - delete (X)
  - move 
  - copy (X)
  """
