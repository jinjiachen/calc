#/usr/bin/env python
#coding=utf-8
import wx
class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'计算软件')
        panel=wx.Panel(self)
        mymenubar=wx.MenuBar()
        mymenu1=wx.Menu()
        mymenu2=wx.Menu()
        myexit=mymenu1.Append(wx.NewId(),'&退出')
        item1=mymenu2.Append(-1,'方板质量')
        item2=mymenu2.Append(-1,'圆板质量')
        item3=mymenu2.Append(-1,'钢管')
        item4=mymenu2.Append(-1,'材料下偏差')
        mymenu2.Append(-1,'安全阀最小口径')
        mymenubar.Append(mymenu1,'文件')
        mymenubar.Append(mymenu2,'计算')
        self.SetMenuBar(mymenubar)
        self.Bind(wx.EVT_MENU,self.exit,myexit)
        self.Bind(wx.EVT_MENU,self.squ,item1)
        self.Bind(wx.EVT_MENU,self.cir,item2)
        self.Bind(wx.EVT_MENU,self.cyl,item3)
        self.Bind(wx.EVT_MENU,self.dev,item4)
    def squ(self,event):
        frame1=myframe1()
        frame1.Show()
    def cir(self,event):
        frame2=myframe2()
        frame2.Show()
    def cyl(self,event):
        frame3=myframe3()
        frame3.Show()
    def dev(self,event):
        frame4=myframe4()
        frame4.Show()
    def exit(self,event):
        self.Close(True)
class myframe1(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'方板质量计算')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'长度(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'宽度(mm):',pos=(50,100))
            wx.StaticText(panel,-1,'高度(mm):',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'计算',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            length=float(self.text1.GetValue())
            width=float(self.text2.GetValue())
            height=float(self.text3.GetValue())
            density=7850
            ans=length*width*height*7850/pow(10,9)
            self.text4.SetValue(`ans`)
class myframe2(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'圆板质量计算')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'直径(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'厚度(mm):',pos=(50,100))
            wx.StaticText(panel,-1,'数量(mm):',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'计算',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            pi=3.14159265357
            D=float(self.text1.GetValue())
            t=float(self.text2.GetValue())
            quantity=float(self.text3.GetValue())
            density=7850
            ans=pi*D*D/4*t*quantity*7850/pow(10,9)
            self.text4.SetValue(`ans`)
class myframe3(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'方板质量计算')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'直径(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'壁厚(mm):',pos=(50,100))
            wx.StaticText(panel,-1,'长度(mm):',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'计算',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            pi=3.14159265357
            D=float(self.text1.GetValue())
            t=float(self.text2.GetValue())
            d=D-2*t
            length=float(self.text3.GetValue())
            density=7850
            ans=pi/4*(D*D-d*d)*length*7850/pow(10,9)
            self.text4.SetValue(`ans`)
class myframe4(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'材料下偏差')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'直径(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'壁厚(mm):',pos=(50,100))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,150))
            self.button=wx.Button(panel,-1,'计算',pos=(60,150))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            D=float(self.text1.GetValue())
            S=float(self.text2.GetValue())
            if D<=102:
                dev=max(0.125*S,0.4)
            else:
                if S/D<=0.05:dev=max(0.15*S,0.4)
                elif S/D<=0.1:dev=max(0.125*S,0.4)
                else:dev=max(0.1*S,0.4)
            self.text3.SetValue(`dev`)
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=myframe()
    frame.Show()
    myapp.MainLoop()
