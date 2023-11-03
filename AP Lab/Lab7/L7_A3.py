import sys

def wrap_lines(filename, width):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        wrapped_lines = []
        for line in lines:
            line = line.rstrip('\n')
            if len(line) > width:
                while len(line) > width:
                    wrapped_lines.append(line[:width])
                    line = line[width:]
                wrapped_lines.append(line)
            else:
                wrapped_lines.append(line)

        with open(filename, 'w') as file:
            for line in wrapped_lines:
                file.write(line + '\n')

        print(f"Lines wrapped at width {width} in {filename}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
    else:
        filename = sys.argv[1]
        width = int(sys.argv[2])
        wrap_lines(filename, width)
