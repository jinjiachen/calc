#coding=utf-8
import wx


class flange_weight_frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'test')
        panel=wx.Panel(self)
        PN=['1','2']
        DN=['coverage']
        wx.ComboBox(panel,-1,'default',(100,100),(80,20),DN)
        wx.ComboBox(panel,-1,'default',(100,100),(80,20),PN)
        

if __name__=='__main__':
   app=wx.PySimpleApp()
   frame=flange_weight_frame()
   frame.Show()
   

   app.MainLoop()
