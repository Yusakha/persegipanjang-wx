# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class PersegiPanjang
###########################################################################

class PersegiPanjang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Persegi Panjang", pos = wx.DefaultPosition, size = wx.Size( 369,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 369,300 ), wx.Size( 369,300 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.tPanjang = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tPanjang.Wrap( -1 )

		bSizer1.Add( self.tPanjang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Panjang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.Panjang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.tLebar = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tLebar.Wrap( -1 )

		bSizer1.Add( self.tLebar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Lebar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.Lebar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.OK, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.Keliling = wx.StaticText( self, wx.ID_ANY, u"Keliling", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Keliling.Wrap( -1 )

		gSizer1.Add( self.Keliling, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Vkeliling = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.Vkeliling, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Luas = wx.StaticText( self, wx.ID_ANY, u"Luas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Luas.Wrap( -1 )

		gSizer1.Add( self.Luas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.vLuas = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.vLuas, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.OK.Bind( wx.EVT_BUTTON, self.OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OKOnButtonClick( self, event ):
		event.Skip()


