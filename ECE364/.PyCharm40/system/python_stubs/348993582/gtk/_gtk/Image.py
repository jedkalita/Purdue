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


from Misc import Misc

class Image(Misc):
    """
    Object GtkImage
    
    Properties from GtkImage:
      pixbuf -> GdkPixbuf: Pixbuf
        A GdkPixbuf to display
      pixmap -> GdkPixmap: Pixmap
        A GdkPixmap to display
      image -> GdkImage: Image
        A GdkImage to display
      mask -> GdkPixmap: Mask
        Mask bitmap to use with GdkImage or GdkPixmap
      file -> gchararray: Filename
        Filename to load and display
      stock -> gchararray: Stock ID
        Stock ID for a stock image to display
      icon-set -> GtkIconSet: Icon set
        Icon set to display
      icon-size -> gint: Icon size
        Symbolic size to use for stock icon, icon set or named icon
      pixel-size -> gint: Pixel size
        Pixel size to use for named icon
      pixbuf-animation -> GdkPixbufAnimation: Animation
        GdkPixbufAnimation to display
      icon-name -> gchararray: Icon Name
        The name of the icon from the icon theme
      storage-type -> GtkImageType: Storage type
        The representation being used for image data
      gicon -> GIcon: Icon
        The GIcon being displayed
    
    Properties from GtkMisc:
      xalign -> gfloat: X align
        The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
      yalign -> gfloat: Y align
        The vertical alignment, from 0 (top) to 1 (bottom)
      xpad -> gint: X pad
        The amount of space to add on the left and right of the widget, in pixels
      ypad -> gint: Y pad
        The amount of space to add on the top and bottom of the widget, in pixels
    
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
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def get_animation(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_set(self, *args, **kwargs): # real signature unknown
        pass

    def get_image(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixel_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def get_stock(self, *args, **kwargs): # real signature unknown
        pass

    def get_storage_type(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_animation(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_file(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_gicon(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_icon_set(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_image(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def set_from_stock(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixel_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


