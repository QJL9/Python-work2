from tkinter import Frame

from tkinter.commondialog import Dialog
from tkinter.font import Font

class Chooser(Dialog):

    def __init__(self, *args, **kw):
        # We use commondialog simply for the master handling logic
        super().__init__(*args, **kw)
        self.w = Frame(self.master).winfo_toplevel()

    def hide(self):
        """Hide the font selection dialog if visible."""
        self.w.tk.call("tk", "fontchooser", "hide")

    def show(self, **options):
        """Show and wait for the font selection dialog."""
        # update instance options
        for k, v in options.items():
            self.options[k] = v

        self.w = w = Frame(self.master).winfo_toplevel()
        self.options["parent"] = w
        if self.options.get("command"):
            self.options["command"] = self._wrapper(self.options["command"])
        w.bind("<<TkFontchooserVisibility>>", self._vischange)
        w.tk.call(("tk", "fontchooser", "configure", *w._options(self.options)))
        w.tk.call(("tk", "fontchooser", "show"))
        # "Depending on the platform, may return immediately or only once the dialog has been withdrawn."
        # https://www.tcl.tk/man/tcl/TkCmd/fontchooser.htm
        # Therefore, we need to vwait to ensure we do not return early
        print("vwait")
        w.tk.call(("vwait", "fontdone"))

    def configure(self, **options):
        """Set the values of one or more options."""
        for k in options:
          self[k] = options[k]
          
    config = configure

    def _vischange(self, event):
        if not self.w.tk.call(("tk", "fontchooser", "configure", "-visible")):
            self.w.tk.call(("set", "fontdone", "done"))

    def _wrapper(self, command):
        def wrap(font):
            actual = self.w.tk.call(("font", "actual", font))
            font = Font(**{i[1:]: j for i, j in zip(actual[::2], actual[1::2])})
            command(font)
        return wrap

    def __setitem__(self, key, value):
        self.w.tk.call("tk", "fontchooser", "configure", "-" + key, value)

    def __getitem__(self, key):
        return self.w.tk.call("tk", "fontchooser", "configure", "-" + key)


def askfont(**options):
    "Ask for a font"
    def setrtn(font):
        nonlocal rtnval
        rtnval = font
    rtnval = None
    options = options.copy()
    options["command"] = setrtn
    chooser = Chooser(**options)
    chooser.show()
    return rtnval

if __name__ == "__main__":
    askfont()