#coding=utf-8
from __future__ import division
from math import pi
import wx


class calc_weight_frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'重量计算')
        panel=wx.Panel(self)
        list1=['方板','圆板','钢管']
        self.choice1=wx.RadioBox(panel,-1,'选择材料的类型',pos=(50,50),choices=list1)
        self.label1=wx.StaticText(panel,-1,'长度(mm)',(50,100))
        self.text1=wx.TextCtrl(panel,-1,'',(150,100))
        self.label2=wx.StaticText(panel,-1,'宽度(mm)',(50,140))
        self.text2=wx.TextCtrl(panel,-1,'',(150,140))
        self.label3=wx.StaticText(panel,-1,'厚度(mm)',(50,180))
        self.text3=wx.TextCtrl(panel,-1,'',(150,180))
        self.label4=wx.StaticText(panel,-1,'密度(kg/m3)',(50,220))
        self.text4=wx.TextCtrl(panel,-1,'',(150,220))
        self.text4.SetValue('7850')#设定密度默认为7850kg/m3
        self.button1=wx.Button(panel,-1,'计算重量',(50,260))
        wx.StaticText(panel,-1,'净重(kg)',(50,300))
        self.text5=wx.TextCtrl(panel,-1,'',(150,300))
        wx.StaticText(panel,-1,'毛重(kg)',(50,340))
        self.text6=wx.TextCtrl(panel,-1,'',(150,340))

        self.Bind(wx.EVT_RADIOBOX,self.renew,self.choice1)
        self.Bind(wx.EVT_BUTTON,self.calculation,self.button1)

    def renew(self,event):
        if self.choice1.GetSelection()==0:
            self.text3.Show(True)
            self.label3.Show(True)
            self.label1.SetLabel('长度(mm)')
            self.label2.SetLabel('宽度(mm)')
            self.label3.SetLabel('厚度(mm)')
        elif self.choice1.GetSelection()==1:
            self.label1.SetLabel('外径(mm)')
            self.label2.SetLabel('厚度(mm)')
            self.label3.Show(False)
            self.text3.Show(False)
        elif self.choice1.GetSelection()==2:
            self.label3.Show(True)
            self.text3.Show(True)
            self.label1.SetLabel('外径(mm)')
            self.label2.SetLabel('厚度(mm)')
            self.label3.SetLabel('长度(mm)')

    def calculation(self,event):
        if self.choice1.GetSelection()==0:
            length=float(self.text1.GetValue())
            width=float(self.text2.GetValue())
            thickness=float(self.text3.GetValue())
            density=float(self.text4.GetValue())
            ans=self.square(length,width,thickness,density)
            self.text5.SetValue(str(ans[0]))
            self.text6.SetValue(str(ans[1]))
        elif self.choice1.GetSelection()==1:
            Do=float(self.text1.GetValue())
            t=float(self.text2.GetValue())
            density=float(self.text4.GetValue())
            ans=self.circle(Do,t,density)
            self.text5.SetValue(str(ans[0]))
            self.text6.SetValue(str(ans[1]))
        elif self.choice1.GetSelection()==2:
            Do=float(self.text1.GetValue())
            t=float(self.text2.GetValue())
            length=float(self.text3.GetValue())
            density=float(self.text4.GetValue())
            ans=self.cylinder(Do,t,length,density)
            self.text5.SetValue(str(ans[0]))
            self.text6.SetValue(str(ans[1]))
            



    def square(self,length,width,thickness,density):##方板的重量计算
        weight=length*width*thickness*density/1000**3
        gross_weight=weight/0.93
        return(weight,gross_weight)

    def circle(self,Do,t,density):##圆钢板的重量计算
        weight=pi/4*Do**2*t*density/1000**3
        gross_weight=weight/0.72
        return(weight,gross_weight)

    def cylinder(self,Do,t,length,density):##计算钢管的重量
        Di=Do-2*t
        weight=pi/4*(Do**2-Di**2)*length*density/1000**3
        gross_weight=weight/0.88
        return(weight,gross_weight)
        
        
500*100*10*7850/1000**3/0.93

if __name__=='__main__':
   app=wx.PySimpleApp()
   frame=calc_weight_frame()
   frame.Show()
   app.MainLoop()




