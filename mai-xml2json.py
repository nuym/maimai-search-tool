import os
import json
import xml.etree.ElementTree as ET

def xml_to_json(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data_dict = {}
    # 找到所有的 StringID 元素
    for string_id in root.findall(".//StringID"):
        id_element = string_id.find('id')
        str_element = string_id.find('str')

        if id_element is not None and str_element is not None:
            data_dict[id_element.text] = str_element.text

    return data_dict

def convert_all_xml_to_json(xml_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(xml_folder):
        if filename.endswith(".xml"):
            xml_path = os.path.join(xml_folder, filename)
            json_data = xml_to_json(xml_path)

            # 将 XML 文件名改为 .json
            json_filename = os.path.splitext(filename)[0] + '.json'
            json_path = os.path.join(output_folder, json_filename)

            # 保存 JSON 数据
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=4)

            print(f"Converted {filename} to {json_filename}")

# 使用示例
xml_folder = 'C:/Users/nuym/Desktop/maimai-search-tool/xml'  # XML 文件夹路径
output_folder = 'C:/Users/nuym/Desktop/maimai-search-tool/json'  # 输出 JSON 文件夹路径

convert_all_xml_to_json(xml_folder, output_folder)
