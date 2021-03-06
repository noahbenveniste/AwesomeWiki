import multicorn

class ForeignDataWrapper(multicorn.ForeignDataWrapper):

    def __init__(self, options, columns):
        super(ForeignDataWrapper, self).__init__(options, columns)
        self.columns = columns

    def execute(self, quals, columns):
        for index in range(20):
            line = {}
            for column_name in self.columns:
                line[column_name] = '%s %s' % (column_name, index)
            yield line