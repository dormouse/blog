import datetime

import sublime, sublime_plugin
from subprocess import call
import subprocess
import os
import re
import tempfile
import platform

ENVIRON = os.environ
if platform.system() != 'Windows':
    ENVIRON['PATH'] += ':/usr/local/bin'

DIGRAPH_START = re.compile(
    '.*(digraph([ \t\n\r]+[a-zA-Z\200-\377_][a-zA-Z\200-\3770-9_]*[ \t\n\r]*{|[ \t\n\r]*{).*)',
    re.DOTALL | re.IGNORECASE
)


def surroundingGraphviz(data, cursor):
    '''
    Find graphviz code in source surrounding the cursor.
    '''

    data_before = data[0:cursor]
    data_after = data[cursor:]

    # find code before selector
    code_before_match = DIGRAPH_START.match(data_before)
    if not code_before_match:
        return None
    code_before = code_before_match.group(1)
    unopened_braces = len(code_before.split('{')) - len(code_before.split('}'))

    # cursor must be in the middle of the graphviz code
    if unopened_braces <= 0:
        return None

    # find code after selector
    code_after_match = re.compile('(' + ('.*\\}' * unopened_braces) + ').*', re.DOTALL).match(data_after)
    if not code_after_match:
        return None
    code_after = code_after_match.group(1)

    # done!
    code = code_before + code_after
    return code


def g_converter(code, output_format):
    '''
    Convert graphviz code to a PDF or PNG.
    '''
    output_prefix = 'sublime_text_graphviz_'

    # temporary graphviz file
    grapviz = tempfile.NamedTemporaryFile(prefix=output_prefix,
                                          dir=None,
                                          suffix='.viz',
                                          delete=False,
                                          mode='wb')
    grapviz.write(code.encode('utf-8'))
    grapviz.close()

    # compile pdf
    if output_format == 'pdf':
        output_suffix = '.pdf'
        output_cmd = '-Tpdf'
    else:
        output_suffix = '.png'
        output_cmd = '-Tpng'

    filename = tempfile.mktemp(prefix=output_prefix,
                               dir=None,
                               suffix=output_suffix)
    call(['dot', output_cmd, '-o' + filename, grapviz.name],
         env=ENVIRON)
    os.unlink(grapviz.name)

    return filename


class GraphvizPreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]

        if not sel.empty():
            code = self.view.substr(sel).strip()
        else:
            code = surroundingGraphviz(
                self.view.substr(sublime.Region(0, self.view.size())),
                sel.begin()
            )


        if not code:
            sublime.error_message('Graphviz: Please place cursor in graphviz code before running')
            return


        pdf_filename = g_converter(code, 'pdf')
        png_filename = g_converter(code, 'png')

        try:
            if platform.system() == 'Windows':
                os.startfile(pdf_filename)
            elif platform.system() == 'Linux':
                call(['feh', png_filename], env=ENVIRON)
                # p = subprocess.Popen(['feh', png_filename],
                    # stdin=subprocess.PIPE,
                    # stdout=subprocess.PIPE,
                    # stderr=subprocess.PIPE,
                    # shell=False)

                # stdout,stderr = p.communicate()
                # print('stdout : ',stdout)
                # print('stderr : ',stderr)
            else:
                call(['open', pdf_filename], env=ENVIRON)
        except Exception as e:
            sublime.error_message('Graphviz: Could not open PDF, ' + str(e))
            raise e
        return



