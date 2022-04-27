import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """ Represent a note in the notebook. Match against a string in 
        searches and store tags for each note.
    """

    def __init__(self, memo, tags=""):
        """ Initialize a note with memo and optional space-seperated
        tags. Automatically set the note's creation date and a unique 
        id.

        Args:
            memo (str): memo text for the note. 
            tags (str, optional): TODO: not sure what it actuall is at the moment. Defaults to "".
        """        
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags




