# Read the txt file 
import urllib.request

url = 'https://adventofcode.com/2022/day/1/input'

urllib.request.urlretrieve(url, 'input.txt')

with open('input.txt', 'r') as f:
    content = f.read()

print(content)
# Sepperate all the indexes into groups by using the blank spaces as deviders

# Assign each group and aggregate the sum values of that group

# Find the group with the highest aggregation

# Print highest aggregation