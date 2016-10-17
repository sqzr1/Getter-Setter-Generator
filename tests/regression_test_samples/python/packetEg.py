#-------------------------------------------------------------------------------
# Name:        Found on wxPython Google grps have no idea what it does?
# Purpose:
#
# Author:      Soribo
#
# Created:     08/09/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wx
import time
import struct
import pyraknet
from pyraknet import PacketTypes, PacketReliability, PacketPriority


class Client():
        def __init__(self):
                        self.net = pyraknet.Peer()
                        self.net.init(thread_sleep_timer=1)
                        self.SERVERPORT = 5555
                        self.IP = '127.0.0.1'
                        self.message = ""


        #----------------------------------------------------------------------
        def getpackets(self):
                        packet = self.net.receive()
                        if packet:
                                        self.message = self.handle_packet(packet)
                        return self.message


        #----------------------------------------------------------------------
        def handle_packet(self, packet):
                        packet_type = ord(packet.data[0])
                        if packet_type == PacketTypes.ID_CONNECTION_ATTEMPT_FAILED:
                                        print 'Could not connect. Quitting...'
                        elif packet_type == PacketTypes.ID_CONNECTION_REQUEST_ACCEPTED:
                                        print 'Connecetd to server!'
                                        self.message = "Connected to Server."
                        elif packet_type == PacketTypes.ID_USER_PACKET_ENUM:
                                        print "PacketTypes.ID_USER_PACKET_ENUM"
                                        print packet.data[1:]
                                        self.message = packet.data[1:]
                        elif packet_type == PacketTypes.ID_USER_PACKET_ENUM:
                                        print "PacketTypes.ID_PONG"
                                        print packet.data[1:]
                                        self.message = packet.data[1:] + " Being Ponged"
                        elif packet_type == PacketTypes.ID_PING:
                                        print "PacketTypes.ID_PING"
                                        print packet.data[1:]
                                        self.message = packet.data[1:] + " Being Pinged"


                        return self.message


        def clear(self):
                self.message = ""


        def connect(self):
                self.net = pyraknet.Peer()
                self.net.init(thread_sleep_timer=10)
                self.net.connect(self.IP, self.SERVERPORT)
                print 'Connecting to server...'


        def disconnect(self):
                data = struct.pack('B', PacketTypes.ID_DISCONNECTION_NOTIFICATION)
                self.net.send(data, len(data), PacketPriority.MEDIUM_PRIORITY,
PacketReliability.RELIABLE, 0, self.net.get_address_from_ip(self.IP,
self.SERVERPORT))


        #----------------------------------------------------------------------
        def send_ping(self):
                data = struct.pack('B', PacketTypes.ID_PING)
                self.net.send(data, len(data), PacketPriority.MEDIUM_PRIORITY,
PacketReliability.RELIABLE, 0, self.net.get_address_from_ip(self.IP,
self.SERVERPORT))


        #----------------------------------------------------------------------
        def send_pong(self):
                data = struct.pack('B', PacketTypes.ID_PONG)
                self.net.send(data, len(data), PacketPriority.MEDIUM_PRIORITY,
PacketReliability.RELIABLE, 0, self.net.get_address_from_ip(self.IP,
self.SERVERPORT))


        #----------------------------------------------------------------------
        def send_message(self, message):
                data = struct.pack('B', PacketTypes.ID_USER_PACKET_ENUM) + message
                self.net.send(data, len(data), PacketPriority.MEDIUM_PRIORITY,
PacketReliability.RELIABLE, 0, self.net.get_address_from_ip(self.IP,
self.SERVERPORT))


class ExamplePanel(wx.Panel):
        def __init__(self, parent):
                wx.Panel.__init__(self, parent)
                self.command = ""
                self.message = ""
                self.command_array = []
                self.command_method = ""
                self.commands = {"netconnect": self.NetConnect, "help":self.ThisHelp, "ping": self.Ping, "netdisconnect":self.NetDisconnect}


                self.timer = wx.Timer(self, 10)


                self.network = Client()


                # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
                self.logger = wx.TextCtrl(self, pos=(20,20), size=(750,500),style=wx.TE_MULTILINE | wx.TE_READONLY)


                # the edit control - one line version.
                self.editname = wx.TextCtrl(self, value=">>>",
                        pos=(10, 530), size=(500,-1),
                        style=wx.TE_PROCESS_ENTER|wx.WANTS_CHARS)


                #wx.EVT_KEY_DOWN(self, wx.ID_ANY, self.CatchArrows)
                wx.EVT_TIMER(self, 100, self.on_timer)
                self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
                self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)
                self.Bind(wx.EVT_TEXT_ENTER, self.on_enter, self.editname)
                self.Bind(wx.EVT_KEY_DOWN, self.onKeyPress, self.editname)
                self.Bind(wx.EVT_CLOSE, self.on_close, self)
                #self.Bind(wx.WXK_DOWN, self.on_down, self.editname)


##      def CatchArrows(self, event):
##              print event.GetKeyCode()


        def EvtChar(self, event):
                self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
                event.Skip()


        def EvtText(self, event):
                self.logger.AppendText('EvtText: %s\n' % event.GetString())
                event.Skip()


        def ThisHelp(self):
                self.LoggerPrintLn(str(self.commands.keys()))


        def LoggerPrint(self, string):
                self.logger.AppendText(string)


        def LoggerPrintLn(self, string):
                self.logger.AppendText(string + "\n")


        def NetConnect(self):
                self.network.connect()


        def NetDisconnect(self):
                self.network.disconnect()


        def on_close(self, event):
           self.timer.Stop()
           self.Destroy()


        def onKeyPress(self, event):
                self.LoggerPrintLn("Inside onKeyPress")
                self.LoggerPrintLn(event.GetString())


        def on_enter(self, event):
                self.input = event.GetString()
                if self.input.startswith("/"):
                        self.logger.AppendText(self.input + " C\n")
                        self.ParseCommand(self.input[1:])
                elif self.input == "":
                        self.editname.Clear()
                else:
                        self.logger.AppendText(self.input + "\n")
                self.editname.Clear()


        def on_timer(self, event):
                self.message = self.network.getpackets()
                if self.message:
                        self.LoggerPrintLn(self.message)
                        self.network.clear()


        def ParseCommand(self, string):
                self.command_array = str.split(string)
                if self.command_array[0] in self.commands.keys():
                        self.commands[self.command_array[0]]()
                else:
                        self.LoggerPrintLn(self.command_array[0] + " is not a valid command")


        def Ping(self):
                self.network.send_ping()


        def OnExit(self,event):
                self.Close(True)


app = wx.App(False)
frame = wx.Frame(None, size = (800, 600))
panel = ExamplePanel(frame)
panel.timer.Start(100)
frame.Show()
app.MainLoop()


