#-Turtle Kütüphanesini Projeye Dahil Ediyoruz CMD Satırına python -m pip install turtle yazarak kurabilirsiniz

from turtle import *

radius=120

#-Yön Konumu -150 Derecelik Açının Tersi
setheading(-150)
penup()

#-Logonun İlk Kırmızı Kısmı
color("red")
begin_fill()
forward(radius)
pendown()
right(90) #-Açının 90 Olmasını Sağlıyoruz
circle(-radius, 120)

#-Mesafenin  180 Dereceye Eşit Olması
forward(radius*3**.5)
left(120)

#-120 Derece Daire Açısı ve 240 Derece Yarıçapını Ayarlar
circle(2*radius, 120)
left(60)
forward(radius*3**.5)
end_fill()

#-YEŞİL KISIM

left(180)
color("green")
begin_fill()
forward(radius*3**.5)
left(120)
circle(2*radius, 120)
left(60)
forward(radius*3**.5)
left(180)
circle(-radius, 120)
end_fill()

#-SARI KISIM

left(180)
circle(radius,120)
color("yellow")
begin_fill()
circle(radius, 120)
right(180)
forward(radius*3**.5)
right(60)
circle(-2*radius, 120)
right(120)
forward(radius*3**.5)
end_fill()

#-MAVİ KISIM

penup()
left(98)
forward(radius/20)
setheading(60)
color("blue")
pendown()
begin_fill()
circle(distance(0,0))
end_fill()
hideturtle()
done()