import Queue
from Tkconstants import BOTTOM, LEFT, VERTICAL, Y, RIGHT, TOP, END
import Tkinter

__author__ = 'victorino'


class KaaGui(Tkinter.Frame):
    def __init__(self, parent, username, client_queue, server_queue):
        Tkinter.Frame.__init__(self, parent)

        self.username = username
        self.client_queue = client_queue
        self.server_queue = server_queue

        # paned window: top > chat, bottom > input
        self.pw = Tkinter.PanedWindow(self, orient=VERTICAL)

        # input frame
        self.frm_input = Tkinter.Frame(self)
        # username
        self.lbl_username = Tkinter.Label(self.frm_input, text=self.username)
        self.lbl_username.pack(side=LEFT)
        # message input
        self.txt_message = Tkinter.Entry(self.frm_input)
        self.txt_message.pack(side=LEFT)

        # output frame
        self.frm_output = Tkinter.Frame(self)
        # output scrollbar
        self.scr_chat = Tkinter.Scrollbar(self.frm_output)
        self.scr_chat.pack(side=RIGHT)
        # chat output
        self.lst_chat = Tkinter.Listbox(self.frm_output)
        self.lst_chat.pack()
        self.lst_chat.config(yscrollcommand=self.scr_chat.set)

        # add input & output frames to panel window
        self.pw.add(self.frm_output)
        self.pw.add(self.frm_input)
        self.pw.pack()

        # bindings
        # send binding
        self.txt_message.bind("<Return>", self.send_message)
        # start receiving binding
        self.master.after(100, self.check_received_loop)

    def send_message(self, event):
        message = self.txt_message.get()
        # prevent empty message
        if message != '':
            # send message to client process
            self.client_queue.put(message)
            # update chat window
            self.lst_chat.insert(END, "You>" + message)
            # empty the text field
            self.txt_message.delete(0, END)

    def check_received_loop(self):
        try:
            message = self.server_queue.get(0)
            # update chat window
            self.lst_chat.insert(END, message)
        # if empty message, loop
        except Queue.Empty:
            self.master.after(100, self.check_received_loop)
