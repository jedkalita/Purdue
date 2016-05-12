# encoding: utf-8
# module gtk._gtk
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gtk/_gtk.so
# by generator 1.136
# no doc

# imports
import atk as __atk
import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class Accessible(__atk.Object):
    """
    Object GtkAccessible
    
    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
    
    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance's name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Is used to notify that the parent has changed
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> gint: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
    
    Signals from GObject:
      notify (GParam)
    """
    def connect_widget_destroyed(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_connect_widget_destroyed(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


