#! /usr/bin/env python

import urllib2
from xml.dom import minidom, Node

class RSSItem:
	"""This is an RSS item, it contain all the RSS info like Tile and Description"""
	def __init__(self,title="",description="", link=""):
		self.title = title
		self.description = description
		self.link = link

class RSSReader:
	"""This class is an RSS reader, it should have a better docstring"""
	
	def __init__(self,RSSUrl):
		"""Initialize the class"""
		self.RSSUrl = RSSUrl;
		self.xmldoc = self.GetXMLDocument(RSSUrl)
		if (not self.xmldoc):
			print "Error Getting XML Document!"
		
	def GetXMLDocument(self,RSSUrl):
		"""This function reads in a RSS URL and then returns the XML documentn on success"""
		url_info = urllib2.urlopen(RSSUrl)
		xmldoc = None
		if (url_info):
			xmldoc = minidom.parse(url_info)
		else	:
			print "Error Getting URL"
		return xmldoc
	
	def GetItemText(self,xml_node):
		"""Get the text from an xml item"""
		text = ""
		for text_node in xml_node.childNodes:
			if (text_node.nodeType == Node.TEXT_NODE):
				text += text_node.nodeValue
		return text
	
	def GetChildText(self, xml_node, child_name):
		"""Get a child node from the xml node"""
		if (not xml_node):
			print "Error GetChildNode: No xml_node"
			return ""
		for item_node in xml_node.childNodes:
			if (item_node.nodeName==child_name):
				return self.GetItemText(item_node)
		"""Return Nothing"""
		return ""
	
	def CreateRSSItem(self,item_node):
		"""Create an RSS item and return it"""
		title = self.GetChildText(item_node,"title")
		description = self.GetChildText(item_node,"description")
		link = self.GetChildText(item_node, "link")
		return RSSItem(title,description,link)
	
	def GetItems(self):
		"""Generator to get items"""
		for item_node in self.xmldoc.documentElement.childNodes:
				if (item_node.nodeName == "item"):
					"""Allright we have an item"""
					rss_item = self.CreateRSSItem(item_node)
					yield rss_item
					
if __name__ == "__main__":

	rss_reader = RSSReader('http://rss.slashdot.org/Slashdot/slashdot')
	for rss_item in rss_reader.GetItems():
		if (rss_item):
			print rss_item.title
			print ""
			print rss_item.description
			print ""