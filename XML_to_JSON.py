#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Inder -> This is working (Final after Nitin's 2nd Request)
import json
import xmltodict
from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse('E:\\iLink\\Projects\\Abbvie\\Kafka\\XML_TO_JSON\\xmlFile.xml')
root = tree.getroot()

# find the eventMetadata element
event_Metadata = root.find('{urn:cmxors.siperian.mrm.events}eventMetadata')

# find the eventType element
eventType_key = event_Metadata.find('{urn:siperian.mrm.events}eventType')
# remove the eventType element from the insertEvent element
event_Metadata.remove(eventType_key)

# find the orsId element
orsId_key = event_Metadata.find('{urn:siperian.mrm.events}orsId')
# remove the orsId element from the insertEvent element
event_Metadata.remove(orsId_key)

# find the triggerUid element
triggerUid_key = event_Metadata.find('{urn:siperian.mrm.events}triggerUid')
# remove the triggerUid element from the insertEvent element
event_Metadata.remove(triggerUid_key)

# find the messageId element
messageId_key = event_Metadata.find('{urn:siperian.mrm.events}messageId')
# remove the messageId element from the insertEvent element
event_Metadata.remove(messageId_key)

# find the messageDate element
messageDate_key = event_Metadata.find('{urn:siperian.mrm.events}messageDate')
# remove the messageDate element from the insertEvent element
event_Metadata.remove(messageDate_key)

tree.write("E:\\iLink\\Projects\\Abbvie\\Kafka\\XML_TO_JSON\\stagingXML.xml")

with open("E:\\iLink\\Projects\\Abbvie\\Kafka\\XML_TO_JSON\\stagingXML.xml") as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    # xml_file.close()
     
    # generate the object using json.dumps()
    # corresponding to json data
     
    json_data = json.dumps(data_dict)
     
    # Write the json data to output
    # json file
    with open("E:\iLink\Projects\Abbvie\Kafka\XML_TO_JSON\dataJson1.json", "w") as json_file:
        json_file.write(json_data)

print('Saved JSON')


# In[ ]:




