import numpy as np

dt = 0.001
t = np.arange(0, 20, dt)
position_in_beat = np.mod(t, 0.8)

def simulate(R, C, Qpeak):
    Q = np.where(position_in_beat < 0.3, Qpeak * np.sin(np.pi * position_in_beat / 0.3), 0)

    P = np.zeros(len(t))
    P[0] = 80

    for i in range(len(t) - 1):
        P[i + 1] = P[i] + ((Q[i] - P[i] / R) / C) * dt

    return Q[-800:], P[-800:]

if __name__ == '__main__':
    rng = np.random.default_rng(0)
    N = 500
    Q_all, P_all, params = [], [], []

    for n in range(N):
        R = rng.uniform(0.7, 1.3)
        C = rng.uniform(1.0, 2.5)
        Qpeak = rng.uniform(300, 500)
        Q, P = simulate(R, C, Qpeak)
        Q_all.append(Q)
        P_all.append(P)
        params.append([R, C, Qpeak])

        if n % 50 == 0:
            print('finished', n)

    np.savez('data.npz', Q=np.array(Q_all), P=np.array(P_all), params=np.array(params))
    print('saved!', np.array(P_all).shape)            