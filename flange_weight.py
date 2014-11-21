#coding=utf-8
import wx


class flange_weight_frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'FlangeWeight')
        self.panel=wx.Panel(self)
        PN=['2.5','6','10','16','25','40','63','100','160']
        self.ComboPN=wx.ComboBox(self.panel,-1,'��ѡ��PN:',(50,50),(100,20),choices=PN)
        self.Bind(wx.EVT_COMBOBOX,self.fun1,self.ComboPN)
        self.ComboDN=wx.ComboBox(self.panel,-1,'��ѡ��DN:',(50,80),(100,20),[])
        Type=['unknow']
#        ComboDN=wx.ComboBox(panel,-1,'��ѡ��DN:',(50,80),(100,20),DN)
        ComboType=wx.ComboBox(self.panel,-1,'��������:',(50,110),(100,20),Type)
        button=wx.Button(self.panel,-1,'��ѯ',(50,150))
        text1=wx.StaticText(self.panel,-1,'��������Ϊ:',(50,200))
        text2=wx.TextCtrl(self.panel,-1,'',(140,200))

    def fun1(self,event):
        s=self.ComboPN.GetStringSelection()
        if s=='160':
            DN=['10','15','20','25','32','40','50','65']
        elif s=='63' or s=='100':
            DN=['10','15','20','25','32','40','50','65','80']
        elif s=='25' or s=='40':
            DN=['10','15','20','25','32','40','50','65','80','100','125','150','200','250','300','350','400','450','500','600']
        else:
            DN=['10','15','20','25','32','40','50','65','80','100','125','150','200','250','300','350','400','450','500','600','700','800','900','1000','1200','1400','1600','1800','2000']
#        ComboDN=wx.ComboBox(self.panel,-1,'��ѡ��DN:',(50,80),(100,20),DN)
        a=self.ComboPN.GetCount()
        print a
        self.ComboDN.Clear()
        for i in range(0,a):
            print DN[i]
            self.ComboDN.Append(DN[i])
        return DN

if __name__=='__main__':
   app=wx.PySimpleApp()
   frame=flange_weight_frame()
   frame.Show()
   app.MainLoop()