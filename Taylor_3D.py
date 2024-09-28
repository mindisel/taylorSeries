import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp  # 기호계산 (방정식)

# 초기 설정
n_order = 10

# 메쉬 그리드 생성
X, Y = np.meshgrid(np.linspace(-5,5, 30), np.linspace(-5,5, 30))

# 함수 정의
def f(x, y):
    return  np.exp(x) * np.sin(y)

# 그래프 생성
fig = plt.figure()  # 시각화할 내용 담는 컨테이너 역할 하는 figure 객체
ax = fig.add_subplot(1, 1, 1, projection='3d')  # 행수,열,위치 , 3d 그릴 수 있도록 설정

# 격자가 있는 서피스 플롯
ax.view_init(elev=24, azim=-137)  # 원하는 각도로 조정

surf = ax.plot_surface(X, Y, f(X, Y), color='gray', alpha=0.3, edgecolor='k', linewidth=0.5)  # 3d 그리기
ax.quiver(0, 0, 0, 5, 0, 0, color='r', linewidth=2, label='X axis')  # X축
ax.quiver(0, 0, 0, 0, 5, 0, color='g', linewidth=2, label='Y axis')  # Y축
ax.quiver(0, 0, 0, 0, 0, 5, color='b', linewidth=2, label='Z axis')  # Z축

ax.set_zlim([-5, 5])
ax.set_title('f(x,y) = e^x * sin(y)')
ax.set_xlabel('x')
ax.set_ylabel('y')

# 테일러 급수 그래프
a, b = sp.symbols('x y')
x0 = -1
F =sp.exp(a) * sp.sin(b) # sympy 에서 함수는 클래스의 객체로 표현됨 즉, 함수 = 객체

# 테일러 급수의 범위 설정
X_taylor, Y_taylor = np.meshgrid(np.linspace(-1,1, 30), np.linspace(-1,1, 30))  # 테일러 급수 범위

for n in range(1, 6):
    color = ['r','b','y','r','b']
    T = F.series(a, x0, n + 1).removeO()
    T_func = sp.lambdify([a, b], T, 'numpy')
    
    # 테일러 급수 그래프 그리기
    Z_taylor = T_func(X_taylor, Y_taylor)
    surface_3d = ax.plot_surface(X_taylor, Y_taylor, Z_taylor, color=color[n-1], alpha=0.3, edgecolor='k', linewidth=0.5) # 하나의 '면' 서피스만 반환 -> plot 은 리스트의  line2d 선을 반환  
    
    plt.pause(1)  # 그래프 업데이트 지연
    
    surface_3d.remove()
    

plt.show()
