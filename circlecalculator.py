# -*- coding: cp936 -*-
import wx
class circleframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'内压圆筒计算厚度(GB150-2011)')
        panel=wx.Panel(self)
        wx.StaticText(panel,-1,'设计压力P(MPa):',(40,50))
        wx.StaticText(panel,-1,'圆筒内径Di(mm):',(40,90))
        wx.StaticText(panel,-1,'焊接系数φ:',(40,130))
        wx.StaticText(panel,-1,'材料许用应力[σ](MPa):',(40,170))
        wx.StaticText(panel,-1,'有效厚度δe(mm):',(40,210))
        wx.StaticText(panel,-1,'计算厚度δ(mm):',(40,290))
        wx.StaticText(panel,-1,'计算应力σt(MPa):',(40,330))
        wx.StaticText(panel,-1,'最大允许工作压力[Pw](MPa):',(40,370))
        self.text1=wx.TextCtrl(panel,-1,'',(200,45))
        self.text2=wx.TextCtrl(panel,-1,'',(200,85))
        self.text3=wx.TextCtrl(panel,-1,'',(200,125))
        self.text4=wx.TextCtrl(panel,-1,'',(200,165))
        self.text5=wx.TextCtrl(panel,-1,'',(200,205))
        button=wx.Button(panel,-1,'计算',(50,245))
        self.Bind(wx.EVT_BUTTON,self.calc,button)
        self.text6=wx.TextCtrl(panel,-1,'',(200,290))
        self.text7=wx.TextCtrl(panel,-1,'',(200,330))
        self.text8=wx.TextCtrl(panel,-1,'',(200,370))
    def calc(self,event):
        p=float(self.text1.GetValue()) #设计压力
        di=float(self.text2.GetValue()) #圆筒内径
        f=float(self.text3.GetValue()) #焊接系数
        cigema=float(self.text4.GetValue()) #许用应力
        delta=float(self.text5.GetValue())  #有效厚度
        ans1=p*di/(2*f*cigema-p)
        ans2=p*(di+delta)/2/delta
        ans3=2*delta*cigema*f/(di+delta)
        self.text6.SetValue(`ans1`)
        self.text7.SetValue(`ans2`)
        self.text8.SetValue(`ans3`)
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=circleframe()
    myframe.Show()
    myapp.MainLoop()
