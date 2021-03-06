# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class CertificateRequest(object):
    """
    CertificateRequest(data=None)
    
    :Parameters:
        data : SecItem or str or any buffer compatible object
            Data to initialize the certificate request from, must be in DER format
    
    An object representing a certificate request
    """
    def format(self, level=0, indent='    '): # real signature unknown; restored from __doc__
        """
        format(level=0, indent='    ') -> string)
        
        :Parameters:
            level : integer
                Initial indentation level, all subsequent indents are relative
                to this starting level.
            indent : string
                string replicated once for each indent level then prepended to output line
        
        This is equivalent to:
        indented_format(obj.format_lines()) on an object providing a format_lines() method.
        """
        return ""

    def format_lines(self, level=0): # real signature unknown; restored from __doc__
        """
        format_lines(level=0) -> [(level, string),...]
        
        :Parameters:
            level : integer
                Initial indentation level, all subsequent indents are relative
                to this starting level.
        
        Formats the object into a sequence of lines with indent level
        information.  The return value is a list where each list item is a
        tuple.  The first item in the tuple is an integer
        representing the indentation level for that line. Any remaining items
        in the tuple are strings to be output on that line.
        
        The output of this function can be formatted into a single string by
        calling `indented_format()`, e.g.:
        
            print indented_format(obj.format_lines())
        
        The reason this function returns a tuple as opposed to an single
        indented string is to support other text formatting systems such as
        GUI's with indentation controls.  See `indented_format()` for a
        complete explanation.
        """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate extensions as a tuple of CertificateExtension objects"""

    subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """subject as an `DN` object"""

    subject_public_key_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate public info as SubjectPublicKeyInfo object"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """version as integer"""



