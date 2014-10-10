#coding=utf-8
import wx
import search_WNdb
class search_WN(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'�����Ժ�������ѯ',size=(700,600))
        panel=wx.Panel(self)
        PN=['10','16','25','40','63','100','160']
        DN=['10','15','20','25','32','40','50','65','80','100','125','150','200','250','300','350','400','450','500','600','700','800','900','1000','1200','1400','1600','1800','2000']
        wx.StaticText(panel,-1,'��ѡ��PN:',(10,10),(80,20))
        self.choice1=wx.Choice(panel,-1,(90,10),(80,20),choices=PN)
        wx.StaticText(panel,-1,'��ѡ��DN:',pos=(200,10),size=(80,20))
        self.choice2=wx.Choice(panel,-1,pos=(280,10),size=(80,20),choices=DN)
        button=wx.Button(panel,-1,'��ѯ',(150,50),(80,20))
        wx.StaticText(panel,-1,'�ֹ��⾶A1(A):',(10,80))
        self.text1=wx.TextCtrl(panel,-1,'',(120,80),(80,20))
        wx.StaticText(panel,-1,'�ֹ��⾶A1(B)',(10,110))
        self.text2=wx.TextCtrl(panel,-1,'',(120,110),(80,20))
        wx.StaticText(panel,-1,'�����⾶D:',(10,140))
        self.text3=wx.TextCtrl(panel,-1,'',(120,140),(80,20))
        wx.StaticText(panel,-1,'��˨������Բֱ��K:',(10,170))
        self.text4=wx.TextCtrl(panel,-1,'',(120,170),(80,20))
        wx.StaticText(panel,-1,'��˨��ֱ��L:',(10,200))
        self.text5=wx.TextCtrl(panel,-1,'',(120,200),(80,20))
        wx.StaticText(panel,-1,'��˨������n:',(10,230))
        self.text6=wx.TextCtrl(panel,-1,'',(120,230),(80,20))
        wx.StaticText(panel,-1,'��˨Th:',(10,260))
        self.text7=wx.TextCtrl(panel,-1,'',(120,260),(80,20))
        wx.StaticText(panel,-1,'�������C:',(10,290))
        self.text8=wx.TextCtrl(panel,-1,'',(120,290),(80,20))
        wx.StaticText(panel,-1,'������N(A):',(10,320))
        self.text9=wx.TextCtrl(panel,-1,'',(120,320),(80,20))
        wx.StaticText(panel,-1,'������N(B)',(10,350))
        self.text10=wx.TextCtrl(panel,-1,'',(120,350),(80,20))
        wx.StaticText(panel,-1,'������S:',(10,380))
        self.text11=wx.TextCtrl(panel,-1,'',(120,380),(80,20))
        wx.StaticText(panel,-1,'������H1:',(10,410))
        self.text12=wx.TextCtrl(panel,-1,'',(120,410),(80,20))
        wx.StaticText(panel,-1,'������R:',(10,440))
        self.text13=wx.TextCtrl(panel,-1,'',(120,440),(80,20))
        wx.StaticText(panel,-1,'�����߶�H:',(10,470))
        self.text14=wx.TextCtrl(panel,-1,'',(120,470),(80,20))
        self.Bind(wx.EVT_BUTTON,self.sea,button)
        image=wx.Image('images\WN.jpg',wx.BITMAP_TYPE_ANY)
        imagev=wx.StaticBitmap(panel,-1,wx.BitmapFromImage(image),pos=(230,80))
    def sea(self,event):
        s1=self.choice2.GetStringSelection()
        s2=self.choice1.GetStringSelection()
        results=search_WNdb.calc(s1,s2)
        self.text1.SetValue(str(results[0][1]))
        self.text2.SetValue(str(results[0][2]))
        self.text3.SetValue(str(results[0][3]))
        self.text4.SetValue(str(results[0][4]))
        self.text5.SetValue(str(results[0][5]))
        self.text6.SetValue(str(results[0][6]))
        self.text7.SetValue(str(results[0][7]))
        self.text8.SetValue(str(results[0][8]))
        self.text9.SetValue(str(results[0][9]))
        self.text10.SetValue(str(results[0][10]))
        self.text11.SetValue(str(results[0][11]))
        self.text12.SetValue(str(results[0][12]))
        self.text13.SetValue(str(results[0][13]))
        self.text14.SetValue(str(results[0][14]))
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=search_WN()
    frame.Show()
    myapp.MainLoop()
