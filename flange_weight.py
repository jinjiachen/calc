#!/usr/bin/python
# -*- coding:cp936 -*-
import wx


class flange_weight_frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'FlangeWeight')
        self.panel=wx.Panel(self)
        PN=['2.5','6','10','16','25','40','63','100','160']
        self.ComboPN=wx.ComboBox(self.panel,-1,'��ѡ��PN:',(50,50),(100,20),choices=PN) #PN��ѡ����Ͽ�
        self.Bind(wx.EVT_COMBOBOX,self.fun1,self.ComboPN)
        
        self.ComboDN=wx.ComboBox(self.panel,-1,'��ѡ��DN:',(50,80),(100,20),[]) #DN��ѡ����Ͽ�
        
#        Type=['��ʽƽ��PL','������BL','����ƽ��SO','�����Ժ�WN','�в庸SW','����Th','����PJ','�Ժ���SE','ƽ����RJ']
        self.ComboType=wx.ComboBox(self.panel,-1,'��������:',(50,110),(100,20),[]) #�����ѯ�����Ķ���
        self.Bind(wx.EVT_COMBOBOX,self.fun2,self.ComboDN)
        button=wx.Button(self.panel,-1,'��ѯ',(50,150))
        text1=wx.StaticText(self.panel,-1,'��������Ϊ:',(50,200))
        text2=wx.TextCtrl(self.panel,-1,'',(140,200))

    def fun1(self,event):
        s1=self.ComboPN.GetStringSelection()
        if s1=='160':
            DN=['10','15','20','25','32','40','50','65']
        elif s1=='63' or s1=='100':
            DN=['10','15','20','25','32','40','50','65','80']
        elif s1=='25' or s1=='40':
            DN=['10','15','20','25','32','40','50','65','80','100','125','150','200','250','300','350','400','450','500','600']
        else:
            DN=['10','15','20','25','32','40','50','65','80','100','125','150','200','250','300','350','400','450','500','600','700','800','900','1000','1200','1400','1600','1800','2000']
        a1=len(DN)
        self.ComboDN.Clear()
        for i in range(0,a1):
            self.ComboDN.Append(DN[i])

    def fun2(self,event):
        s2=self.ComboPN.GetStringSelection()
        if s2=='2.5':
            Type=['��ʽƽ��PL','������BL']
        elif s2=='6':
            Type=['��ʽƽ��PL','������BL','����ƽ��SO','����Th','����PJ','�Ժ���SE','ƽ����RJ']
        elif s2=='63' or s2=='100':
            Type=['������BL','�в庸SW','�����Ժ�WN']
        elif s2=='160':
            Type=['������BL','�����Ժ�WN']
        else:
            Type=['��ʽƽ��PL','������BL','����ƽ��SO','�����Ժ�WN','�в庸SW','����Th','����PJ','�Ժ���SE','ƽ����RJ']
            a2=len(Type)
        self.ComboType.Clear()
        for i in range(0,a2):
            self.ComboType.Append(Type[i])
        

if __name__=='__main__':
   app=wx.PySimpleApp()
   frame=flange_weight_frame()
   frame.Show()
   app.MainLoop()
