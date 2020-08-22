import wx
import smtplib
import dropbox
import wx.adv

def send_email(subject, msg, from_address, password, to_address):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(from_address,password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(from_address, to_address, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")
def upload_cloud():
    dropbox_access_token = "AM74RjwqLKAAAAAAAAAAHHadWMHyHUZuzNqCMNx905gARRpIVv6nWj_QsYQ-q-w2"
    dropbox_path = "/history.txt"
    computer_path = "C:\\Users\\msmit\\Desktop\\Cloud\\Backup.txt"
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))
from_mail = ""
pass_mail = ""
to_mail = ""
sub_mail = ""
msg_mail = ""

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1552, 840))
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_1.Add(static_line_1, 0, wx.ALL | wx.EXPAND, 5)

        static_line_2 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_1.Add(static_line_2, 0, wx.ALL | wx.EXPAND, 5)

        static_text_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "E-MAIL")
        static_text_1.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_1.Add(static_text_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        static_line_3 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_1.Add(static_line_3, 0, wx.ALL | wx.EXPAND, 5)

        static_line_4 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_1.Add(static_line_4, 0, wx.ALL | wx.EXPAND, 5)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

        static_text_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "FROM", style=wx.ALIGN_CENTER)
        static_text_2.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_2.Add(static_text_2, 0, wx.ALL, 5)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_1.SetMinSize((600, 23))
        self.text_ctrl_1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_2.Add(self.text_ctrl_1, 0, wx.ALL, 5)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 0, 0, 0)

        static_text_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "PASSWORD", style=wx.ALIGN_CENTER)
        static_text_3.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_3.Add(static_text_3, 0, wx.ALL, 5)

        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_2.SetMinSize((350, 23))
        self.text_ctrl_2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_3.Add(self.text_ctrl_2, 0, wx.ALL, 5)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_4, 0, 0, 0)

        static_text_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "TO", style=wx.ALIGN_CENTER)
        static_text_4.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(static_text_4, 0, wx.ALL, 5)

        self.text_ctrl_3 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_3.SetMinSize((600, 23))
        self.text_ctrl_3.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_4.Add(self.text_ctrl_3, 0, wx.ALL, 5)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_5, 0, 0, 0)

        static_text_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "SUBJECT", style=wx.ALIGN_CENTER)
        static_text_5.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(static_text_5, 0, wx.ALL, 5)

        self.text_ctrl_4 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_4.SetMinSize((600, 23))
        self.text_ctrl_4.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_5.Add(self.text_ctrl_4, 0, wx.ALL, 5)

        self.text_ctrl_5 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "",style = wx.TE_MULTILINE)
        self.text_ctrl_5.SetMinSize((1000, 400))
        self.text_ctrl_5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_1.Add(self.text_ctrl_5, 0, wx.ALL, 10)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_6, 0, 0, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "SEND ONLY")
        self.button_1.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.button_1, 0, wx.ALL, 5)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "SEND AND STORE IN CLOUD")
        self.button_2.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.button_2, 0, wx.ALL, 5)

        static_text_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "NOTE:\n           Sign in into google and go to the below link and toggle the switch to ON before using this software.")
        static_text_6.SetMinSize((1200, 40))
        static_text_6.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_1.Add(static_text_6, 0, wx.ALL, 5)

        self.hyperlink_1 = wx.adv.HyperlinkCtrl(self.panel_1, wx.ID_ANY, "https://myaccount.google.com/lesssecureapps", "")
        self.hyperlink_1.SetMinSize((1200, 46))
        self.hyperlink_1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_1.Add(self.hyperlink_1, 0, wx.ALL, 5)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_TEXT, self.From, self.text_ctrl_1)
        self.Bind(wx.EVT_TEXT, self.password, self.text_ctrl_2)
        self.Bind(wx.EVT_TEXT, self.to, self.text_ctrl_3)
        self.Bind(wx.EVT_TEXT, self.subject, self.text_ctrl_4)
        self.Bind(wx.EVT_TEXT, self.message, self.text_ctrl_5)
        self.Bind(wx.EVT_BUTTON, self.send_only, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.send_cloud, self.button_2)
        # end wxGlade

    def From(self, event):  # wxGlade: MyFrame.<event_handler>
        global from_mail
        from_mail=self.text_ctrl_1.GetValue()
        event.Skip()

    def password(self, event):  # wxGlade: MyFrame.<event_handler>
        global pass_mail
        pass_mail=self.text_ctrl_2.GetValue()
        event.Skip()

    def to(self, event):  # wxGlade: MyFrame.<event_handler>
        global to_mail
        to_mail=self.text_ctrl_3.GetValue()
        event.Skip()

    def subject(self, event):  # wxGlade: MyFrame.<event_handler>
        global sub_mail
        sub_mail=self.text_ctrl_4.GetValue()
        event.Skip()

    def message(self, event):  # wxGlade: MyFrame.<event_handler>
        global msg_mail
        msg_mail=self.text_ctrl_5.GetValue()
        event.Skip()

    def send_only(self, event):  # wxGlade: MyFrame.<event_handler>
        global sub_mail,msg_mail,from_mail,pass_mail,to_mail
        send_email(sub_mail,msg_mail,from_mail,pass_mail,to_mail)
        event.Skip()

    def send_cloud(self, event):  # wxGlade: MyFrame.<event_handler>
        global sub_mail,msg_mail,from_mail,pass_mail,to_mail
        send_email(sub_mail,msg_mail,from_mail,pass_mail,to_mail)
        my_file = open("Backup.txt", "w+")
        my_file.write(" ///// FROM :")
        my_file.write(from_mail)
        my_file.write(" ///// TO :")
        my_file.write(to_mail)
        my_file.write(" /////SUBJECT : ")
        my_file.write(sub_mail)
        my_file.write(" ///// MESSAGE : ")
        my_file.write(msg_mail)
        my_file.close()
        upload_cloud()
        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
