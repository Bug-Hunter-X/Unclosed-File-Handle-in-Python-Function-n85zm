def function_with_unclosed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    # Missing f.close() or similar resource cleanup
    # The file remains open, potentially causing issues later