from html_context_manager_class import HTMLContextManager
content = '''
<TR>
    <TD>1</TD>
    <TD>Say hello!</TD)
</TR>
<TR>
    <TD>2</TD>
    <TD>Say good bye!</TD>
</TR>
'''

if __name__ == "__main__":
    with HTMLContextManager(content) as context: pass