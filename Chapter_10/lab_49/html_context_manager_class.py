class HTMLContextManager:
    
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        self.__start = "<TABLE>\n<TR>\n    <TH>Number</TH>\n    <TH>Description</TH>\n</TR>"
        return self
    
    def __exit__(self, type, value, traceback):
        self.__stop = "</TABLE>"
        self.__difference = self.__start + self.content + self.__stop
        print('HTML Page:' + '\n' + self.__difference) 
