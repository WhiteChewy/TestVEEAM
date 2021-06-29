# -*- coding: utf-8 -*-
from multiprocessing import Process
import xml.etree.ElementTree as ElementTree
import shutil


def xmlTreeToList(xmlTreeRoot):
    nodeList = []
    for node in xmlTreeRoot:
        nodeList.append(node.attrib)
    return nodeList


def fileCopy(nodes):
    for node in nodes:
        if node['source_path'][0] == '/':
            shutil.copy2(node['source_path'] + '/' + node['file_name'], node['destination_path'])
        else:
            shutil.copy2(node['source_path'] + '\\' + node['file_name'], node['destination_path'])


if __name__ == "__main__":
    tree = ElementTree.parse("file.xml")
    root = tree.getroot()
    nodes = xmlTreeToList(root)
    p1 = Process(target=fileCopy, args=([nodes[i] for i in range(0, len(nodes), 2)],))
    p2 = Process(target=fileCopy, args=([nodes[i] for i in range(1, len(nodes), 2)],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

