import wx
import main
import re
class sub(main.PersegiPanjang):
    def __init__(self, parent):
        main.PersegiPanjang.__init__(self, parent)
    def check(self):
        panjang = self.Panjang.GetValue()
        lebar = self.Lebar.GetValue()
        if re.search("[a-z]", panjang) or re.search("[a-z]", lebar):
            self.Vkeliling.SetValue(str("inputan harus int"))
            self.vLuas.SetValue(str("inputan harus int"))
            return True
        else:
            return False
    def OKOnButtonClick( self, event ):
        if self.check():
            pass
        else:
            panjang = self.Panjang.GetValue()
            lebar = self.Lebar.GetValue()
            keliling = (2*float(panjang))+(2*float(lebar))
            luas = float(panjang)*float(lebar)
            self.Vkeliling.SetValue(str(keliling))
            self.vLuas.SetValue(str(luas))

app = wx.App()
frame = sub(parent=None)
frame.Show()
app.MainLoop()