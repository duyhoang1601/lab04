#1.the same on-screen.
def read_content(filename):
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)
read_content('poem.txt')
#2. line by line and display
def count_line(filename):
    with open(filename, "r") as f:
        count = 0
        for line in f:
            if not line.startswith('T'):
                count += 1
    print(f"No of line start with T = {count}")
count_line('story.txt')
    
        
        
       
