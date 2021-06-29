# -*- coding: utf-8 -*-
from multiprocessing import Process
import xml.etree.ElementTree as ElementTree
import shutil


def xmlCopy(xmlTreeRoot):
    for node in xmlTreeRoot:
        if node.attrib['source_path'][0] == '/':
            shutil.copy2(node.attrib['source_path'] + '/' + node.attrib['file_name'], node.attrib['destination_path'])
        else:
            shutil.copy2(node.attrib['source_path'] + '\\' + node.attrib['file_name'], node.attrib['destination_path'])


if __name__ == "__main__":
    tree = ElementTree.parse("file.xml")
    root = tree.getroot()
    p = Process(target=xmlCopy, args=(root,))
    p.start()
    p.join()

