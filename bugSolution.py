def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            for line in f:
                # process each line
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return