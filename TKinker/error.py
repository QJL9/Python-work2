import tkinter as tk
from tkinter import messagebox

class FaultTolerantTk(tk.Tk):
    def report_callback_exception(self, exc, val, tb):
        self.destroy_unmapped_children(self)
        messagebox.showerror('Error!', val)

    # NOTE: It's an optional method. Add one if you have multiple windows to open
    def destroy_unmapped_children(self, parent):
        """
        Destroys unmapped windows (empty gray ones which got an error during initialization)
        recursively from bottom (root window) to top (last opened window).
        """
        children = parent.children.copy()
        for index, child in children.items():
            if not child.winfo_ismapped():
                parent.children.pop(index).destroy()
            else:
                self.destroy_unmapped_children(child)

# def main():
root = FaultTolerantTk()
root.report_callback_exception('a','someerror','b')
root.mainloop()


# if __name__ == '__main__':
#     main()