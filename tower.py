def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Step 1: Move top n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)


# Example usage
n = 3  # Number of disks
tower_of_hanoi(n, "Source", "Target", "Auxiliary")
