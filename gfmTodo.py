import sublime_plugin
from datetime import datetime 

class gfmBase(sublime_plugin.TextCommand):
  def run(self, edit):
    filename = self.view.file_name()
    # list of allowed filetypes
    allowed_filetypes = ('.md', '.markdown', '.mdown', '.todo')
    if filename is None or not filename.endswith(allowed_filetypes):
      return False  
    self.runCommand(edit)

class toggle_completeCommand(gfmBase):
  def runCommand(self, edit):    
    for region in self.view.sel():
      lines = self.view.lines(region)
      lines.reverse()
      for line in lines:
        line_head = self.view.find("[-] \[[ X]\]", line.begin())
        line_contents = self.view.substr(line).strip()

        # prepend @done if item is ongoing
        if line_contents.startswith('- [ ]'): 
          self.view.insert(edit, line.end(), " _@done (%s)_" % datetime.now().strftime("%Y-%m-%d %H:%M"))
          self.view.replace(edit, line_head, "- [X]")
        
        # undo @todo
        elif line_contents.startswith('- [X]'):
          subfix = self.view.find('(\s)*_@done(.)+\)_', line.begin())
          self.view.erase(edit, subfix)
          self.view.replace(edit, line_head, "- [ ]")
