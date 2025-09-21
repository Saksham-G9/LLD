import xmltodict
import json
from abc import ABC, abstractmethod


# Target
class ITarget(ABC):
    @abstractmethod
    def get_json_data(self): ...


# Adaptee
class XMLProvider:
    def get_xml_data(self):
        return "<data><item>123</item></data>"


# Adapter
class XMLProviderAdapter(ITarget):
    def __init__(self, xml_provider: XMLProvider):
        self.xml_provider = xml_provider

    def get_json_data(self):
        xml_data = self.xml_provider.get_xml_data()
        json_data = json.dumps(xmltodict.parse(xml_data))
        return json_data


# Client
class Client:
    def __init__(self, target: ITarget):
        self.target = target

    def get_json_data(self):
        return self.target.get_json_data()


# Usage
xml_provider = XMLProvider()
adapter = XMLProviderAdapter(xml_provider)
client = Client(adapter)

print(client.get_json_data())  # {"data": {"item": "123"}}
