from PIL import Image, ImageDraw, ImageFont


image = Image.open('note.jpg')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', 25) if 'arial.ttf' else ImageFont.load_default()
color = (255, 0, 0)
draw.text((190, 445), 'Hello, World!', font=font, fill=color)
font = ImageFont.truetype('arial.ttf', 20) if 'arial.ttf' else ImageFont.load_default()
draw.text((635, 405), '12-12-2004', font=font, fill=color)
font = ImageFont.truetype('arial.ttf', 20) if 'arial.ttf' else ImageFont.load_default()
draw.text((635, 570), 'Some details...', font=font, fill=color)
font = ImageFont.truetype('arial.ttf', 30) if 'arial.ttf' else ImageFont.load_default()
draw.text((610, 760), '5,000 UGX', font=font, fill=color)
draw.text((610, 830), '5,000 UGX', font=font, fill=color)
draw.text((610, 900), '5,000 UGX', font=font, fill=color)
draw.text((610, 970), '5,000 UGX', font=font, fill=color)
draw.text((610, 1030), '5,000 UGX', font=font, fill=color)
draw.text((610, 1080), '5,000 UGX', font=font, fill=color)
draw.text((610, 1125), '5,000 UGX', font=font, fill=color)






image.save('output.jpg')


