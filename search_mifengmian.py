#coding=utf-8
import wx
import search_mifengmiandb

class search_mifengmian(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'密封面参数',(10,10),(900,600))
		panel=wx.Panel(self)
		PN=['2.5','6','10','25','>=40']
		DN=['10','15','20','25','32','40','50','65','80','100','125','150','200','250','300','350','400','450','500','600','700','800','900','1000','1200','1400','1600','1800','2000']
		wx.StaticText(panel,-1,'请选择PN',(10,10))
		self.choice1=wx.Choice(panel,-1,(90,10),choices=PN)
		wx.StaticText(panel,-1,'请选择DN',(200,10))
		self.choice2=wx.Choice(panel,-1,(280,10),choices=DN)
		wx.StaticText(panel,-1,'外径d:(mm)',(30,50))
		wx.StaticText(panel,-1,'f1:(mm)',(30,90))
		wx.StaticText(panel,-1,'f2:(mm)',(30,130))
		wx.StaticText(panel,-1,'f3:(mm)',(30,170))
		wx.StaticText(panel,-1,'W:(mm)',(30,210))
		wx.StaticText(panel,-1,'X:(mm)',(30,250))
		wx.StaticText(panel,-1,'Y:(mm)',(30,290))
		wx.StaticText(panel,-1,'Z:(mm)',(30,330))
		self.text1=wx.TextCtrl(panel,-1,'',(110,50))
		self.text2=wx.TextCtrl(panel,-1,'',(110,90))
		self.text3=wx.TextCtrl(panel,-1,'',(110,130))
		self.text4=wx.TextCtrl(panel,-1,'',(110,170))
		self.text5=wx.TextCtrl(panel,-1,'',(110,210))
		self.text6=wx.TextCtrl(panel,-1,'',(110,250))
		self.text7=wx.TextCtrl(panel,-1,'',(110,290))
		self.text8=wx.TextCtrl(panel,-1,'',(110,330))

		button1=wx.Button(panel,-1,'查询',(360,10))
		self.Bind(wx.EVT_BUTTON,self.search,button1)


        	image=wx.Image('/home/ifk/github/calc/images/seal.jpg',wx.BITMAP_TYPE_ANY)
	        imagev=wx.StaticBitmap(panel,-1,wx.BitmapFromImage(image),pos=(230,80))

	def search(self,event):
		PN=self.choice1.GetStringSelection()
		DN=self.choice2.GetStringSelection()	
		if PN=="2.5":
			PN="2point5"
		elif PN==">=40":
			PN="40"
		results=search_mifengmiandb.calc(PN,DN)
		print results
		self.text1.SetValue(results[0][0])
		self.text2.SetValue(results[1][7])
		self.text3.SetValue(results[1][8])
		self.text4.SetValue(results[1][9])
		self.text5.SetValue(results[1][10])
		self.text6.SetValue(results[1][11])
		self.text7.SetValue(results[1][12])
		self.text8.SetValue(results[1][13])
		

if __name__=='__main__':
	myapp=wx.PySimpleApp()
	frame=search_mifengmian()
	frame.Show()
	myapp.MainLoop()
