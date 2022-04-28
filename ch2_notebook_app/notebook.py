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
        global last_id  #TODO: look up what global is doing?
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags




class Notebook:
    """ Represent a collection of notes that can be tagged, modified,
        and searched. 
    """
    def __init__(self):
        """ Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=""):
        """ Create a new note and add it to the list

        Args:
            memo (str): memo text for the note. 
            tags (str, optional): TODO: not sure what it actuall is at the moment. Defaults to "".
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo  #TODO: what if note_id not exist?
    
    def modify_tags(self, note_id, tags):
        self._find_note(note_id).tags = tags  #TODO: what if note_id not exist?
    
    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]