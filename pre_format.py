#coding=cp936

import wx
import format


class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'���϶���������',size=(400,600))
        panel=wx.Panel(self)
        list1=['���ְ�','Բ�ְ�','�ֹ�','Բ��']
        list2=['Q245R','Q235B','20']
#        list3=['�⹺','���޸�']
        wx.StaticText(panel,-1,'ͼ��',(50,90))
        self.input1=wx.TextCtrl(panel,-1,'',(120,90))
        wx.StaticText(panel,-1,'����',(50,130))
        self.input2=wx.TextCtrl(panel,-1,'',(120,130))
        wx.StaticText(panel,-1,'����',(50,170))
        self.input3=wx.Choice(panel,-1,(120,170),choices=list1)
        wx.StaticText(panel,-1,'�ƺ�',(50,210))
        self.input4=wx.Choice(panel,-1,(120,210),choices=list2)
        self.text5=wx.StaticText(panel,-1,'����(mm)',(50,250))
        self.input5=wx.TextCtrl(panel,-1,'',(120,250))
        self.text6=wx.StaticText(panel,-1,'���(mm)',(50,290))
        self.input6=wx.TextCtrl(panel,-1,'',(120,290))
        self.text7=wx.StaticText(panel,-1,'���(mm)',(50,330))
        self.input7=wx.TextCtrl(panel,-1,'',(120,330))
        wx.StaticText(panel,-1,'�к�',(50,50))
        self.input8=wx.TextCtrl(panel,-1,'',(120,50))
        wx.StaticText(panel,-1,'����',(50,370))
        self.input9=wx.TextCtrl(panel,-1,'',(120,370))
        button=wx.Button(panel,-1,'��������',(50,450))
        wx.CheckBox(panel,-1,'�⹺',pos=(50,410))
        wx.CheckBox(panel,-1,'���޸�',pos=(110,410))

        self.Bind(wx.EVT_BUTTON,self.fun1,button)
        self.Bind(wx.EVT_CHOICE,self.renew1,self.input3)


    def fun1(self,event):
        i=self.input8.GetValue()#�к�
        num=self.input1.GetValue()#ͼ��
        name=self.input2.GetValue()#����
        mat=self.input3.GetStringSelection()#����
        pai=self.input4.GetStringSelection()#�ƺ�
        amount=float(self.input9.GetValue())#����
        x1=self.input5.GetValue()
        x2=self.input6.GetValue()
        x3=self.input7.GetValue()
        format.exc(i,num,name,mat,pai,x1,x2,x3,amount)



    def renew1(self,event):
        if self.input3.GetStringSelection().encode('cp936')=='�ֹ�':
            self.input7.Show(True)
            self.text7.Show(True)
            self.text5.SetLabel('�⾶(mm)')
            self.text6.SetLabel('���(mm)')
            self.text7.SetLabel('����(mm)')
        elif self.input3.GetStringSelection().encode('cp936')=='Բ��':
            self.text5.SetLabel('�⾶(mm)')
            self.text6.SetLabel('����(mm)')
            self.text7.Show(False)
            self.input7.Show(False)
        elif self.input3.GetStringSelection().encode('cp936')=='���ְ�':
            self.text7.Show(True)
            self.input7.Show(True)
            self.text5.SetLabel('����(mm)')
            self.text6.SetLabel('���(mm)')
            self.text7.SetLabel('���(mm)')
        elif self.input3.GetStringSelection().encode('cp936')=='Բ�ְ�':
            self.text5.SetLabel('�⾶(mm)')
            self.text6.SetLabel('���(mm)')
            self.text7.Show(False)
            self.input7.Show(False)
        
        
        
        
        
        

    
#if __name__=='__main__':
#    myapp=wx.PySimpleApp()
#    frame=myframe()
#    frame.Show()
#    myapp.MainLoop()
