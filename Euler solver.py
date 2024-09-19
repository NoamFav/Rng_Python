import matplotlib.pyplot as plt


def rabbit_population(a, b, r, f):
    return a * r - b * r * f


def fox_population(c, d, r, f):
    return -c * f + d * r * f


def eagle_population(e, r, f, alpha_r, alpha_f, delta):
    return e * (alpha_r * r + alpha_f * f) - delta * e


if __name__ == "__main__":
    a = 0.1  # Rabbit birth rate
    b = 0.02  # Rabbit death rate per fox
    c = 0.3   # Fox death rate
    d = 0.01  # Fox birth rate per rabbit
    h = 0.01  # Step size
    alpha_r = 0.005
    alpha_f = 0.01
    delta = 0.2
    end_time = 100  # End time
    steps = int(end_time / h)  # Number of steps
    rabbit_start = 40
    fox_start = 9
    e_start = 5
    rabbit_values = [rabbit_start]
    fox_values = [fox_start]
    eagle_values = [e_start]
    t_values = [0]  # Time starts at 0

    for i in range(steps):
        r = rabbit_values[-1]
        f = fox_values[-1]
        e = eagle_values[-1]

        rabbit_change = rabbit_population(a, b, r, f)
        fox_change = fox_population(c, d, r, f)
        eagle_change = eagle_population(e, r, f, alpha_r, alpha_f, delta)

        rabbit_values.append(r + h * rabbit_change)
        fox_values.append(f + h * fox_change)
        eagle_values.append(e + h * eagle_change)
        t_values.append(h * (i + 1))

    plt.plot(t_values, rabbit_values, label="Rabbits")
    plt.plot(t_values, fox_values, label="Foxes")
    plt.plot(t_values, eagle_values, label="Eagles")
    plt.title("Rabbit and Fox Population Dynamics")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.show()
