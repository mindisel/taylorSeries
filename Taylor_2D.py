import numpy as np  # 수치계산
import matplotlib.pyplot as plt  # 그래프
import sympy as sp  # 기호계산 (방정식)

# 처음화면 -> e^x 만
XLIMS = [-6 , 6 ]
YLIMS = [-6, 6]

# x_value를 생성
x_value = np.linspace(XLIMS[0], XLIMS[1], 100) 
y_value = np.exp(x_value)
plt.ylim(YLIMS)

# 화면 그리기
line, = plt.plot(x_value, y_value, linewidth=1)

plt.axhline(0)
plt.axvline(0)

plt.grid(True)

# x축 눈금 설정 (1씩 증가)
plt.xticks(np.arange(XLIMS[0], XLIMS[1] + 1, 1))
plt.yticks(np.arange(XLIMS[0], XLIMS[1] + 1, 1))


# e^x 의 테일러급수 그리기
x = sp.symbols('x')
f = sp.exp(x)

x0 = 1

for n in range(1, 11):
    T = sp.series(f, x, x0, n + 1).removeO()
    T_func = sp.lambdify(x, T, 'numpy')
    
    # plot 은 2d 그래프 그리는것으로 -> 반환값 : Line2D : 객체의 리스트를 반환
    line2, = plt.plot(x_value, T_func(x_value), linewidth=1, color='r')
    
    plt.pause(1)
    
    line2.remove()

plt.show()
