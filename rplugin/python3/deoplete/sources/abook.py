import json
import deoplete.util
import re
import string

from deoplete.logger import getLogger
from subprocess import Popen, PIPE
from .base import Base

ABOOK_RE = re.compile(r'^(?P<email>[^\s]+)\s+(?P<name>.*)$')

log = getLogger('logging')

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim);

        log.debug("**** INIT:")
        self.abook_bin = self.vim.vars['deoplete#sources#abook#abook_bin'] or 'abookija'
        self.rank = 600
        self.name = 'abook'
        self.mark = '[AB]'
        self.min_pattern_length = 0
        #self.filetypes = ['mail']


    def get_complete_position(self, context):
        pos = context['input'].rfind(' ')
        return pos if pos < 0 else pos + 1

    def gather_candidates(self, context):
        #line = str(self.vim.current.window.cursor[0])
        #column = str(self.vim.current.window.cursor[1] + 1)
        line = context["input"]

        # Only complete To, CC and BCC headers
        if not (line.startswith("To: ") or line.startswith("Cc: ") or line.startswith("Bcc: ")):
            return []
        command = [self.abook_bin, '--mutt-query', line[line.rfind(" "):]]

        log.debug("****context:" + str(context))
        buf = '\n'.join(self.vim.current.buffer[:])

        process = Popen(command, stdout=PIPE, stdin=PIPE)
        command_results = process.communicate(input=str.encode(buf))[0]

        if process.returncode != 0:
            return []

        results = []
        for row in command_results.decode('utf-8').split(u"\n"):
            regexp = ABOOK_RE.search(row)
            if regexp:
                results.append("%s <%s>" % (regexp.group("name").strip(), regexp.group("email").strip()))

        log.debug("**** RESULTS:" + str(results))

        return [{'word': x} for x in results]
        #return [{'word': x['name'], 'kind': x['type']} for x in results]
