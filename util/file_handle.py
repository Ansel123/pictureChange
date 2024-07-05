import base64
import json
import mimetypes
import os

from common.log import logger


# 读取配置文件
def get_config_path(json_path: str):
    cursor = os.path.dirname(__file__)
    return os.path.join(cursor, json_path)


# 读取配置文件
def update_config(config_path, user_id, append):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    if append:
        config["use_group"].append(user_id)
    else:
        config["use_group"].remove(user_id)
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


# 用于图片和文件转成base64
def file_toBase64(file_path: str):
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as file:
                image_data = file.read()
                base64_image = base64.b64encode(image_data).decode('utf-8')
                # 获取文件的MIME类型
                mime_type, _ = mimetypes.guess_type(file_path)
                logger.info(f"文件路径: {file_path}")
                logger.info(f"文件MIME类型: {mime_type}")
                if mime_type is None:
                    mime_type = "application/octet-stream"  # 默认MIME类型
                base64_image = f"data:{mime_type};base64,{base64_image}"
                return base64_image
        except Exception as e:
            logger.error(f"读取文件时出错: {e}")
            return None
    else:
        logger.warning(f"文件不存在: {file_path}")
        return None


def delete_file(file_content):
    try:
        if os.path.isfile(file_content):
            os.remove(file_content)
            return "🥰图片已成功删除\n🧸感谢您的使用！"
    except Exception as e:
        logger.error(f"{str(e)}")
    return "😭文件不存在或已删除"
