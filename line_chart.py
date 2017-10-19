import matplotlib.pyplot as plt

# Part 1
# plt.plot([1, 2, 3, 4])

# Part 2
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='green', linestyle='dashdot')
plt.plot([2, 3, 4, 5], [2, 3, 4, 5], color='#2B5B84', linestyle='dashed')
plt.ylabel('Important Figures')
plt.legend()

# Part 3

# plt.subplot(2, 1, 1)
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='green', linestyle='dashdot')
# # plt.subplot(2, 1, 1).set_xlim([0, 6])
# # plt.subplot(2, 1, 1).set_ylim([0, 20])
#
# plt.subplot(2, 1, 2)
# plt.plot([2, 3, 4, 5], [2, 3, 4, 5], color='#2B5B84', linestyle='dashed')
# # plt.subplot(2, 1, 2).set_xlim([0, 6])
# # plt.subplot(2, 1, 2).set_ylim([0, 20])

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.ylabel('Important Figures')

plt.show()
