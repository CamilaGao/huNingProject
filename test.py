# from django_redis import get_redis_connection
#
# # 获取默认的 Redis 连接
# redis_conn = get_redis_connection()
#
# # 获取所有键
# keys = redis_conn.keys('*')
#
# # 遍历所有键，并获取对应的值
# for key in keys:
#     value = redis_conn.get(key)
#     print(f"Key: {key}, Value: {value.decode('utf-8')}")
import os
import django

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hengDaProject.settings')
django.setup()

from aboutApp.models import Award

# Awards 文件夹路径（相对于项目目录）
awards_folder = os.path.join('media', 'Award')

# 遍历文件夹中的所有图片
for filename in os.listdir(awards_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # 构造图片文件的路径
        image_path = os.path.join('Award', filename)

        # 创建并保存 Award 实例
        award = Award(description=f"Award {filename}", photo=image_path)
        award.save()
        print(f"Added {filename} to the database.")
