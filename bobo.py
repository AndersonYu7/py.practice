"""
 VPython教學: 15-1.一維彈性碰撞公式
 Ver. 1: 2018/2/28
 Ver. 2: 2019/9/13
 作者: 王一哲
"""

from vpython import *

"""
 
"""
d1, m1, v1, c1 = 0.2, 0.5, 1.0, color.red        # 木塊1的寬度=0.1 m, 質量=0.5 kg, 初速, 紅色
d2, m2, v2, c2 = 0.2, 0.1, 0.0, color.green      # 木塊2的寬度=0.1 m, 質量=0.1 kg, 初速, 綠色
d3, m3, v3, c3 = 0.2, 0.1, 0.0, color.purple
xmax, xmin = 2.0, -2.0                           # x 軸範圍
t, dt = 0, 0.0005                                # 時間, 畫面更新的時間間隔，單位為s, 原為0.001但能量不夠準確, 故改為0.0005

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="1 Dimension Collision", width=800, height=300, center=vec(0, 0.4, 0),
               background=vec(0, 0.6, 0.6))
# 產生地板
floor = box(pos=vec(0, -d1/2.0, 0), size=vec((xmax - xmin), 0.05, 0.8), color=color.blue)
# 產生左側木塊 b1,  右側木塊 b2 並設定初速度
b1 = box(pos=vec(xmin + 0.5*d1, 0, 0), size=vec(d1, d1, d1), color=c1, m=m1, v=vec(v1, 0, 0))
b2 = box(pos=vec(-0.5, 0, 0), size=vec(d2, d2, d2), color=c2, m=m2, v=vec(v2, 0, 0))
b3 = box(pos=vec(1, 0, 0), size=vec(d3, d3, d3), color=c3, m=m3, v=vec(v3, 0, 0))
# 繪圖部分
gd = graph(title="<i>v</i>-<i>t</i> plot", x=0, y=300, width=600, height=450,
           xtitle="<i>t</i> (s)", ytitle="red: <i>v</i><sub>1</sub>, green: <i>v</i><sub>2</sub> (m/s)")
vt1 = gcurve(graph=gd, color=c1)
vt2 = gcurve(graph=gd, color=c2)
vt3 = gcurve(graph=gd, color=c3)

# 自訂函式，一維彈性碰撞速度公式
def af_col_v(m1, m2, m3, v1, v2, v3):
    v1_prime = (m1-m2)/(m1+m2)*v1 + (2*m2)/(m1+m2)*v2
    v2_prime = (2*m1)/(m1+m2)*v1 + (m2-m1)/(m1+m2)*v2
    v3_prime = (m3-m2)/(m3+m2)*v3 + (2*m2)/(m3+m2)*v2_prime
    v2_prime2 = (2*m2)/(m2+m3)*v2_prime + (m3-m2)/(m2+m3)*v3
    return (v1_prime, v2_prime,v3_prime,v2_prime2)

"""
3. 物體運動部分, 重複執行直到木塊抵達邊緣時

""" 

# 印出木塊撞前速度
print("m1=", b1.m, "m2 =", b2.m)
print(b1.v.x, b2.v.x)

while ((b2.pos.x <= xmax - d2/2) and (b1.pos.x >= xmin + d1/2)):
    rate(1000)
# 計算木塊間的距離, 若發生碰撞則計算撞後速度
    dx = b2.pos.x - b1.pos.x
    if(dx <= (d1 + d2)/2):
        b1.v.x, b2.v.x = af_col_v(b1.m, b2.m, b1.v.x, b2.v.x)
# 更新木塊的位置
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
    b3.pos += b3.v * dt
# 畫 v-t 圖
    vt1.plot(pos=(t, b1.v.x))
    vt2.plot(pos=(t, b2.v.x))
# 更新時間
    t += dt

print(b1.v.x, b2.v.x, b3.v.x)