import matplotlib.pyplot as plt

# line 1 points
x1 = [4,2,3]
y1 = [9,3,4]
#plotting the line 1 points
plt.plot(x1, y1,color="orange", label = "Orange Line")


# line 2 points
x2 = [5,6,1]
y2 = [7,5,1]
#plotting the line 2 points
plt.plot(x2, y2,color="blue", label = "Blue Line")


# line 6 points
x3 = [6,4,4]
y3 = [6,2,5]
#plotting the line 2 points
plt.plot(x3, y3,color="aqua", label = "Aqua Line")


# line 5 points
x4 = [3,7,7]
y4 = [8,1,3]
#plotting the line 5 points
plt.plot(x4, y4,color="violet", label = "Violet Line")


# line 3 points
x5 = [8,9,2]
y5= [5,7,6]
#plotting the line 3 points
plt.plot(x5, y5,color="blue", label = "Blue Line")


# line 8 points
x6 = [9,6,8]
y6 = [4,9,2]
#plotting the line 4 points
plt.plot(x6, y6,color="green", label = "Green Line")


# line 7 points
x6 = [5,3,8]
y6 = [2,8,5]
#plotting the line 4 points
plt.plot(x6, y6,color="red", label = "Red Line")


# line 9 points
x6 = [5,7,4]
y6 = [9,4,2]
#plotting the line 4 points
plt.plot(x6, y6,color="yellow", label = "Yellow Line")


# line 9 points
x6 = [4,7,4]
y6 = [5,7,2]
#plotting the line 4 points
plt.plot(x6, y6,color="black", label = "Black Line")


# line 9 points
x6 = [4,6,3]
y6 = [5,2,7]
#plotting the line 4 points
plt.plot(x6, y6,color="maroon", label = "Maroon Line")

# naming the x axis
plt.xlabel('X')
# naming the y axis
plt.ylabel('Y')
# giving a title to the graph
plt.title('Plots of Line')

# showing a legend on the plot
plt.legend()

# functioning to show the plot
plt.show()