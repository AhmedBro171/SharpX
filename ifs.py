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

  # I will finish that tommorow, unless someone edits it before, in case. Here is the meaning of this : 
  """
  Interacting with Filesystem.
  Future functions :
  - delete
  - move
  - copy
  """
