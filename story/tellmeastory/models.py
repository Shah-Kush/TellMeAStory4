from django.db.models import BooleanField, ImageField, TextField, CharField, Model
from django.urls import resolve, Resolver404
from re import fullmatch, Match
from validators import url

# Create your models here.
class User(Model):
    username: CharField = CharField(max_length=200)
    password: CharField = CharField(max_length=512)
    display_name: CharField = CharField(max_length=200)

    def __str__(self):
        return self.username

    def is_valid_username(self) -> bool:
        """
        Returns True if self.username consists of only the following:
        Unicode word characters, numbers, hyphens, underscores.
        Also, the length of self.username must be >= 5 and <= 14
        """
        # strip to remove leading/trailing spaces
        stripped_uname: str = self.username.strip()

        # \w   : Unicode word chars, numbers
        # (-_): Hyphens, underscores
        # *    : Any number of times, 0 inclusive
        PATTERN: str = r"[\w(-_)]*"
        regex_match: Match = fullmatch(PATTERN, stripped_uname)

        # fullmatch returns a Match object if the string matches the pattern
        # otherwise, it returns None
        return (5 <= len(self.username) <= 14) and regex_match != None

    def is_unique_username(self) -> bool:
        """
        Returns True if self.username is not associated with another
        User in the database.
        """
        # DoesNotExist should be raised if the query returns nothing
        # TODO: come back, I may be misinterpreting queries
        try:
            User.objects.get(username=self.username)
        except self.DoesNotExist:
            return True
        return False

    def is_valid_display_name(self) -> bool:
        """
        Returns True if self.display_name has a length of >= 5 and <= 20.
        """
        return 5 <= len(self.display_name) <= 20

class Node(Model):
    """ Story Node class. Holds a story's contents to present
    to users that select the respective story node. """
    image: ImageField = ImageField(upload_to="storyimages", default=None)
    image_url: TextField = TextField()
    node_title: CharField = CharField(max_length=200)
    content: CharField = CharField(max_length=10_000)
    # The Node has an url if False, otherwise it has an image file
    has_image_file: BooleanField = BooleanField(default=False)

    def __str__(self):
        """
        Returns current Title for A Story Node.
        """
        return self.node_title

    def add_image(self, newFile=None, newURL=None) -> bool:
        """
        Allows for image to be attached to a Story Node.
        """
        # If both parameters are given, then the image cannot
        # be updated to just one. Return False.
        if newFile is not None and newURL is not None:
            return False
        # newFile is given and can be updated as current image
        elif newFile is not None:
            return self.add_image_from_file(file=newFile)
        # newURL is given and can be updated as current image
        elif newURL is not None:
            return self.add_image_from_url(URL=newURL)
        # Nothing was given. No changes made. Return False
        else:
            return False

    def add_image_from_file(self, file) -> bool:
        """
        Allows for image url to be attached to a Story Node.
        Returns True if attached, otherwise false.
        """
        # Try to find image file
        self.image = file
        try:
            # Update image properties
            self.has_image_file = True
            self.image_url = TextField(default=None)
            self.save()
            return True
        except:
            # Error thrown
            # Change nothing
            return False

    def add_image_from_url(self, URL) -> bool:
        """
        Allows for image url to be linked to a node.
        Returns True if downloaded and attached, otherwise false.
        """
        # Try to find url
        self.image_url = URL
        try:
            # Will not throw error if valid file
            if url(self.image_url):
                # Update image properties
                self.has_image_file = False
                self.image = None
                self.save()
                return True
            # Failsafe for no exception and invalid url
            return False
        except:
            # Error thrown, meaning file does not exist
            # Change nothing
            return False
