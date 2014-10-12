#coding=utf-8
import wx
class circleframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'圆筒计算厚度')
        panel=wx.Panel(self)
        wx.StaticText(panel,-1,'设计压力P(MPa):',(40,50))
        wx.StaticText(panel,-1,'圆筒内径Di(mm):',(40,90))
        wx.StaticText(panel,-1,'焊接系数φ:',(40,130))
        wx.StaticText(panel,-1,'材料许用应力[σ](MPa):',(40,170))
        wx.StaticText(panel,-1,'计算厚度(mm):',(40,250))
        self.text1=wx.TextCtrl(panel,-1,'',(200,45))
        self.text2=wx.TextCtrl(panel,-1,'',(200,85))
        self.text3=wx.TextCtrl(panel,-1,'',(200,125))
        self.text4=wx.TextCtrl(panel,-1,'',(200,165))
        button=wx.Button(panel,-1,'计算',(50,205))
        self.Bind(wx.EVT_BUTTON,self.calc,button)
        self.text5=wx.TextCtrl(panel,-1,'',(200,245))
    def calc(self,event):
        p=float(self.text1.GetValue()) #设计压力
        di=float(self.text2.GetValue()) #圆筒内径
        f=float(self.text3.GetValue()) #焊接系数
        delta=float(self.text4.GetValue()) #焊接系数
        ans=p*di/(2*f*delta-p)
        self.text5.SetValue(`ans`)
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=circleframe()
    myframe.Show()
    myapp.MainLoop()
