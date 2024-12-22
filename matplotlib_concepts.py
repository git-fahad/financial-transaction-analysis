import matplotlib.pyplot as plt
#
x = [1,2,3,4,5]
y = [5,6,7,8,9]
# plt.plot(x,y)
# plt.title("Simple Line Plot")
# plt.xlabel("x-axis")
# plt.xlabel("y-axis")
# plt.show()
#
# a = [1,2,4,5,2,46,5]
# b = [23,1,4,56,23,4,3]
# plt.scatter(a,b, color = 'blue', marker = 'o')
# plt.title("Simple scatter plot")
# plt.xlabel("x-axis")
# plt.ylabel("x-axis")
# plt.show()

categories = ['Maths', 'Science', 'Social Science', 'Language']
values = [22,21,10,34]
# plt.bar(categories, values, color = 'red')
# plt.title("Bar Plot")
# plt.xlabel("Subject")
# plt.ylabel("Marks")
# plt.show()

# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
# plt.hist(data, bins=7, color = 'black', edgecolor = 'yellow')
# plt.show()
#
# plt.plot(x, y, linestyle='--', color='red')
# plt.show()

d = [1,2,3,4,6,8,9]
e = [2,1,3,5,6,2,1]
# plt.plot(x,y, label="Line 1")
# plt.plot(d, [i*2 for i in e], label="Line 2")
# plt.legend()
# plt.show()

plt.subplot(2,1,1)
plt.plot(categories,values,color='blue')
plt.title("First plot")

plt.subplot(2,1,2)
plt.bar(d,e,color='green')
plt.title("Second plot")

plt.tight_layout()
plt.show()
plt.savefig("plot.png")


