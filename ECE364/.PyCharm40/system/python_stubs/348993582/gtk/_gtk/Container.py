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


from Widget import Widget

class Container(Widget):
    """
    Object GtkContainer
    
    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)
    
    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def add_with_properties(self, *args, **kwargs): # real signature unknown
        pass

    def check_resize(self, *args, **kwargs): # real signature unknown
        pass

    def children(self, *args, **kwargs): # real signature unknown
        pass

    def child_get(self, *args, **kwargs): # real signature unknown
        pass

    def child_get_property(self, *args, **kwargs): # real signature unknown
        pass

    def child_set(self, *args, **kwargs): # real signature unknown
        pass

    def child_set_property(self, *args, **kwargs): # real signature unknown
        pass

    def child_type(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_add(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_check_resize(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_child_type(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_composite_name(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_forall(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_child_property(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_remove(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_child_property(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_focus_child(cls, *args, **kwargs): # real signature unknown
        pass

    def forall(self, *args, **kwargs): # real signature unknown
        pass

    def foreach(self, *args, **kwargs): # real signature unknown
        pass

    def get_border_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_chain(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_child(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_focus_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def get_resize_mode(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def install_child_property(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def list_child_properties(cls, *args, **kwargs): # real signature unknown
        pass

    def propagate_expose(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def resize_children(self, *args, **kwargs): # real signature unknown
        pass

    def set_border_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_chain(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_child(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def set_focus_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def set_reallocate_redraws(self, *args, **kwargs): # real signature unknown
        pass

    def set_resize_mode(self, *args, **kwargs): # real signature unknown
        pass

    def unset_focus_chain(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    border_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_focus_chain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_resize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reallocate_redraws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


