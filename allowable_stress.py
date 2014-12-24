# -*- coding:cp936 -*-
from __future__ import division
import wx


class allowableframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'许用应力计算(GB47012-2010)')
        panel=wx.Panel(self)
        material=['钢管20','Q245R','Q235B']
        wx.StaticText(panel,-1,'选择材料(mm):',(100,50))
        wx.StaticText(panel,-1,'厚度(mm):',(100,100))
        wx.StaticText(panel,-1,'温度:',(100,150))
        wx.StaticText(panel,-1,'许用应力(MPa):',(100,250))
        self.choices=wx.Choice(panel,-1,(200,50),(100,30),choices=material)
        self.text1=wx.TextCtrl(panel,-1,'',(200,100)) #输入厚度
        self.text2=wx.TextCtrl(panel,-1,'',(200,150)) #输入温度
        button=wx.Button(panel,-1,'计算',(100,200)) 
        self.text3=wx.TextCtrl(panel,-1,'',(200,250)) #输出许用应力
        self.Bind(wx.EVT_BUTTON,self.all,button)
    def all(self,event):
        a1=self.choices.GetStringSelection()
        a2=float(self.text1.GetValue()) #取厚度
        a3=float(self.text2.GetValue()) #取温度
        if a1=='Q235B':
            if a2>=3 and a2<16:
                if a3<150:
                    ans=113
                elif a3>=150 and a3<200:
                    ans=(105-113)/50*(a3-150)+113
            elif a2>=16 and a2<30:
                if a3<100:
                    ans=113
                elif a3>=100 and a3<150:
                    ans=(107-113)/50*(a3-100)+113
                elif a3>=150 and a3<200:
                    ans=(99-107)/50*(a3-150)+107
        elif a1=='Q245R':
            if a2>=3 and a2<16:
                if a3<=20:
                    ans=133
                elif a3>20 and a3<=100:
                    ans=(132-133)/80*(a3-20)+133
                elif a3>100 and a3<=150:
                    ans=(126-132)/50*(a3-100)+132
                elif a3>150 and a3<=200:
                    ans=(118-126)/50*(a3-150)+126
            elif a2>=16 and a2<36:
                if a3<=20:
                    ans=133
                elif a3>20 and a3<=100:
                    ans=(126-133)/80*(a3-20)+133
                elif a3>100 and a3<=150:
                    ans=(120-126)/50*(a3-100)+126
                elif a3>150 and a3<=200:
                    ans=(112-120)/50*(a3-150)+120
            elif a2>=36 and a2<60:
                if a3<=20:
                    ans=133
                elif a3>20 and a3<=100:
                    ans=(120-133)/80*(a3-20)+133
                elif a3>100 and a3<=150:
                    ans=(114-120)/50*(a3-100)+120
                elif a3>150 and a3<=200:
                    ans=(107-114)/50*(a3-150)+114
        self.text3.SetValue(str(ans))
                
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=allowableframe()
    myframe.Show()
    myapp.MainLoop()
