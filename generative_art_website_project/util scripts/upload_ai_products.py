# import os
# import random
# # from shop.models import AIProduct
# from django.core.files.base import ContentFile
#
# path = '/Users/raunit_x/Desktop/The Generative Art Project/AI Art/Individual Artworks'
# for file in os.listdir(path):
#     if random.random() > 0.3:
#         continue
#     # ai_product_object = AIProduct()
#     file_path = f'{path}/{file}'
#     with open(file_path, 'rb') as f:
#         data = f.read()
#     ai_product_object.name = file.split('.')[0]
#     ai_product_object.image.save(f'ai{file}', ContentFile(data))
#     ai_product_object.information = 'Created by a Style GAN'
#     ai_product_object.save()

