from __future__ import unicode_literals

import prompt_toolkit as ptk

GIT_COMMAND_STRUCTURE = {
  'init': {
    'help_': 'Create an empty Git repository or reinitialize an existing one',
  },
  'clone': {
    'help_': 'Clone a repository into a new directory',
  },
  'add': {
    'help_': 'Add file contents to the index',
    'flags_': ['--all', '--dry-run', '--force', '--interactive', '--verbose'],
  },
  'commit': {
    'help_': 'Record changes to the repository',
    'flags_': ['--all', '--message'],
  },
}

class GitCompleter(ptk.completion.Completer):

  def get_completions(self, document, complete_event):
    if not document.is_cursor_at_the_end:
      yield None


    for key in GIT_COMMAND_STRUCTURE:
      yield ptk.completion.Completion(key)


commands = ptk.completion.WordCompleter(['clone', 'init', 'commit', 'add'])
text = ptk.prompt('git > ', completer=GitCompleter())
print 'You said: %s' % text
