def create(Document.New):
    '''
        Create new Document
    '''
    return Document()
def load():
    '''
        Load document from database
    '''
    pass

class Document(object):
    New = 1
    Status_Allowed = [New]
    def __init__(self,id = None,status = None,**kwargs):
        if id != None:
            self.__Id = int(id)
        if status != None:
            if status not in Document.Status_Allowed:
                raise ValueError
            self.__Status = status
    id = property(lambda self: self.__Id)
    @property
    def status(self):
        return Document.__Statusi

    def save(self):
        pass

    def restore(self):
        pass
