import plotly.graph_objs as go
from plotly.subplots import make_subplots

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def collatz_graph(n):
    sequence = collatz_sequence(n)
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Scatter(x=list(range(len(sequence))), y=sequence, mode='lines', name=f'Collatz sequence for {n}'))
    fig.update_layout(title=f'Collatz sequence for {n}', xaxis_title='Step', yaxis_title='Value')
    fig.show()

def collatz_range(start, end):
    for n in range(start, end+1):
        print(f"Starting number: {n}")
        sequence = collatz_sequence(n)
        for i in range(len(sequence)):
            print(sequence[i])
            collatz_graph(sequence[i])
            input("Press Enter to continue...")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

collatz_range(start, end)