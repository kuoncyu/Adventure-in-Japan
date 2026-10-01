import json, sys
from PIL import Image, ImageDraw
ks=['hanlin','shiaolan','poyu','sihyu','zihchian','wanjhen','lali','kerou','jianlin','jiaen']
G=json.load(open('guess.json')) if __import__('os').path.exists('guess.json') else {}
def crop_face(k, cx, cy, S):
    im=Image.open(f'cut2/{k}.png').convert('RGBA')
    box=(int(cx-S/2),int(cy-S/2),int(cx+S/2),int(cy+S/2))
    c=Image.new('RGBA',(S,S),(0,0,0,0)); c.paste(im.crop((max(0,box[0]),max(0,box[1]),min(im.width,box[2]),min(im.height,box[3]))),(max(0,-box[0]),max(0,-box[1])))
    return c.resize((128,128),Image.LANCZOS)
if __name__=='__main__':
    G=json.load(open('guess.json'))
    tiles=[]
    for k in ks:
        cx,cy,S=G[k]; f=crop_face(k,cx,cy,S)
        bg=Image.new('RGBA',(128,128),(230,230,230,255)); bg.alpha_composite(f); tiles.append((k,bg.convert('RGB').resize((256,256))))
    sheet=Image.new('RGB',(256*5,256*2+0),(30,30,30)); d=ImageDraw.Draw(sheet)
    for i,(k,t) in enumerate(tiles):
        sheet.paste(t,((i%5)*256,(i//5)*256)); d.text(((i%5)*256+4,(i//5)*256+4),k,fill=(255,0,0))
    sheet.save('/home/claude/jp/facesheet.png')
