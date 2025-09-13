from PIL import Image
masked_matrix=Image.open('word_matrix.png')
masker=Image.open('mask.png')
resized_masker=masker.resize((1015,559))
resized_masker.putalpha(150)
masked_matrix.paste(im=resized_masker,box=(0,0),mask=resized_masker)
masked_matrix.show()
