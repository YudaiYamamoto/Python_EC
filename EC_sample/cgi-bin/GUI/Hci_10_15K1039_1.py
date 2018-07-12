#IPアドレス
#http://localhost:8000/cgi-bin/GUI/Hci_10_15K1039_1.py


import cgitb
import cgi, sys, io
cgitb.enable()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form=cgi.FieldStorage()

cart = form.getvalue('cart','0')
cancel = form.getvalue('cancel','0')
x = form.getvalue('cancel','0')
a = int(form.getvalue('pen','0'))
aa = 100
a0 = int(form.getvalue('0','0'))
b = int(form.getvalue('pencil','0'))
bb = 75
b1 = int(form.getvalue('1','0'))
c = int(form.getvalue('eraser','0'))
cc = 60
c2 =  int(form.getvalue('2','0'))
d = int(form.getvalue('ruler','0'))
dd = 150
d3 = int(form.getvalue('3','0'))
e = int(form.getvalue('glue','0'))
ee = 100
e4 = int(form.getvalue('4','0'))
f = int(form.getvalue('appointment_book','0'))
ff = 1000
f5 = int(form.getvalue('5','0'))
g = int(form.getvalue('paper_clip','0'))
gg = 150
g6 = int(form.getvalue('6','0'))
h = int(form.getvalue('highlighter','0'))
hh = 100
h7 = int(form.getvalue('7','0'))
i = int(form.getvalue('notebook','0'))
ii = 500
i8 = int(form.getvalue('8','0'))
j = int(form.getvalue('scissors','0'))
jj = 600
j9 = int(form.getvalue('9','0'))

room = form.getvalue('room','0')
passward = form.getvalue('pas','0')

filepath = "GUI.txt"
passfile = "passward.txt"
roomfile = "room.txt"

s = []
rooms = []
minus = [a0,b1,c2,d3,e4,f5,g6,h7,i8,j9]
name = ["ペン","鉛筆","消しゴム","定規","のり","手帳","クリップ","蛍光ペン","ノート","はさみ"]
try:
  file = open(filepath, 'r', encoding = "utf-8")
  p = open(passfile,"r",encoding="utf-8-sig")
  r = open(roomfile, "r", encoding="utf-8-sig")
  real_passward=p.readline().rstrip("\n")
  for line in file:
      s.append(int(line.rstrip("\n")))
  for line in r:
      rooms.append(line.rstrip("\n"))
except IOError:
  pass
else:
  file.close()
  p.close()
  r.close()

if s == [] or cancel == "4":
  s = [0,0,0,0,0,0,0,0,0,0]

s[0] = s[0] + a
s[1] = s[1] + b
s[2] = s[2] + c
s[3] = s[3] + d
s[4] = s[4] + e
s[5] = s[5] + f
s[6] = s[6] + g
s[7] = s[7] + h
s[8] = s[8] + i
s[9] = s[9] + j

count = 0
for x in s:
  if x < 0:
    s[count] = 0
  count = count + 1

count = 0
for m in minus:
  if m != "0":
    s[count] = s[count] - m
  count = count + 1

present = ""
count = 0
for x in s:
    if x != 0:
        present = present + """<pre> {} ×{}個 <input type="number" name="{}"></pre>""".format(name[count],x,count)
    count = count + 1
check = s[0]*aa + s[1]*bb + s[2]*cc + s[3]*dd + s[4]*ee + s[5]*ff + s[6]*gg + s[7]*hh + s[8]*ii + s[9]*jj

comment = ""
if passward != "0":
  cart = "pas"
if cart == "pas":
  comment = comment + """パスワードを入力してください。\n<input type="text" name="pas">
                         <p><a href="/cgi-bin/GUI/Hci_10_15K1039_3.py"> パスワードを変更する </a></p>
                         <pre>請求先を選択してください。</pre>
                           <select name = "room">"""
  for x in sorted(rooms, key = lambda room:room):
      comment = comment + """ 
                           <option value="{}">{}</option>""".format(x,x)
  comment = comment + """  </select>
                          <p><a href="/cgi-bin/GUI/Hci_10_15K1039_2.py"> 請求先の追加 </a></p>
                          <p><a href="/cgi-bin/GUI/Hci_10_15K1039_1.py"> 注文画面に戻る </a></p>"""
  if passward == real_passward:
      present = ""
      count = 0
      for x in s:
          if x != 0:
              present = present + """<pre> {} ×{}個 </pre>""".format(name[count],x)
          count = count + 1
      check = s[0]*aa + s[1]*bb + s[2]*cc + s[3]*dd + s[4]*ee + s[5]*ff + s[6]*gg + s[7]*hh + s[8]*ii + s[9]*jj
      comment = """<pre>ご注文完了いたしました。ご利用ありがとうございます。\n</pre>
                   <pre>請求先: {}</pre>
                   <pre>ご購入商品 \n{}</pre>
                   <strong> 合計金額: {}円</strong>
      <p><a href="/cgi-bin/GUI/Hci_10_15K1039_1.py"> 注文画面に戻る </a></p>""".format(room,present,check)
      s = [0,0,0,0,0,0,0,0,0,0]
  elif passward == "0":
    pass
  elif passward != real_passward:
    comment = comment + "パスワードが違います。もう一度やり直してください。"


else:
    comment = comment +"""<pre><font size=7> 商品一覧</font>\n</pre>
    <pre> ペン　　　　￥{}:  　  <img src="http://www.sashienomori.com/110504_4/sharppen2.gif" alt="写真" width=50 height=50><input type="number" name="pen">    鉛筆　　　　￥{}:  　 <img src="http://www.civillink.net/fsozai/sozai/enpitu4.gif" alt="写真" width=50 height=50><input type="number" name="pencil"></pre>
    <pre> 消しゴム　　￥{}: <img src="http://myds.jp/illustration/stationery/eraser/a.jpg" alt="写真" width=60 height=50> <input type="number" name="eraser">       定規　　　　￥{}:　  <img src="http://illustcut.com/box/life/bungu/bungu02_21.png" alt="写真" width=50 height=50><input type="number" name="ruler"></pre>
    <pre> のり　　　　￥{}: <img src="https://t19.pimg.jp/021/908/309/1/21908309.jpg" alt="写真" width=50 height=50><input type="number" name="glue">         手帳　　　　 ￥{}:　 <img src="http://allfree-clipart-design.com/wp-content/uploads/Business-Diary-Address-Book-or-Notebook-Vector.jpg" alt="写真" width=50 height=50><input type="number" name="appointment_book"></pre>
    <pre> クリップ　　￥{}: <img src="http://01.gatag.net/img/201504/28l/gatag-00002619.jpg" alt="写真" width=50 height=50><input type="number" name="paper_clip">　　　　 蛍光ペン　 　￥{}:    <img src="https://illustration.jp.net/wp-app/wp-content/uploads/2016/01/04_05_12-300x300.jpg" alt="写真" width=50 height=50><input type="number" name="highlighter"></pre>
    <pre> ノート　　　￥{}: 　<img src="http://www.oofree.net/drawing_object/p2/note.png" alt="写真" width=50 height=50><input type="number" name="notebook">       はさみ　　　￥{}: 　<img src="data:image/png;base64,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" alt="写真" width=50 height=50><input type="number" name="scissors"></pre>  
    <p>    <button type="submit" name="aaa" value="5"> カートへ入れる </button></p>
    <p>  <button type="submit" name="cancel" value="4"> キャンセル </button> <button type="submit" name="cart" value="pas"> 購入へ </button></p>
    <pre> 現在のカート      カートから削除\n {}</pre>
    <strong> 合計金額: {}円</strong>
     """.format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,present,check)
    #comment = comment + "{},{},{},{},{},{},{},{},{},{}".format(a0,b1,c2,d3,e4,f5,g6,h7,i8,j9)
with open(filepath, "w") as file:
    for post in s:
        file.write(str(post) + "\n")
with open(passfile, "w",encoding = "utf-8") as file:
        file.write(real_passward+"\n")

template ="""
<html>
 <head>
    <meta charset="utf-8">
   <title> page </title>
  </head>
    <body>
     <strong><font size = "3"></font></strong>
     <pre></pre>
     <form method="POST" action="/cgi-bin/GUI/Hci_10_15K1039_1.py"> 
     {comment}
     </form>
    </body>
</html>

"""
    
result = template.format(comment=comment)
print("Content-type: text/html\n")
print(result)

#実行時間
#GUIで1品目を購入(パスワード:hosei,請求先も先頭の場所とする)
#H+P+H+K+P+P+H+K+K+K+K+K+K = 5.9[S]
