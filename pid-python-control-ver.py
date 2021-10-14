from control.matlab import *
import numpy as np
from matplotlib import pyplot as plt


def main():
    # PIDコントローラK
    Kp = 0.5
    Ki = 0.03
    Kd = 0.03
    num = [Kd, Kp, Ki]  # 分子の多項式係数
    den = [1, 0]  # 分母の多項式係数
    K = tf(num, den)  # 伝達関数システムの作成

    # フィードバック対象G
    Kt = 1
    J = 0.01
    C = 0.1
    num = [Kt]
    den = [J, C, 0]
    G = tf(num, den)

    # フィードバック
    sys = feedback(K*G, 1)  # KとGのネガティヴフィードバックをやる
    t = np.linspace(0, 3, 1000)  # numpyを使って
    y, T = step(sys, t)  # フィードバックを用いてステップ応答を求める

    plt.plot(T, y)  # 点をプロット(x, y)
    plt.grid()
    plt.axhline(1, color="b", linestyle="--")  # 目標値の点線表示
    plt.xlim(0, 3)

    plt.show()


if __name__ == "__main__":  # メイン判断のガード
    main()
