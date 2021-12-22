print("Hello from docker!!")

# import bagpy
# from bagpy import bagreader
# import pandas as pd
# import seaborn as sea
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image

# b = bagreader('test.bag')
# # print(b.topic_table)
# # csvfiles = []
# # for t in b.topics:
# #     data = b.message_by_topic(t)
# #     csvfiles.append(data)

# # # print(csvfiles[0])
# # # data = pd.read_csv(csvfiles[0])

# # data = b.message_by_topic('/device_0/sensor_1/Color_0/image/data')
# # print("File saved: {}".format(data))

# # img_csv = pd.read_csv(data)
# # img_csv
# # img_arr = np.ndarray(img_csv)
# # im = Image.fromarray(img_arr)
# # im.save("your_file.jpeg")
# # get all the messages of type velocity
# velmsgs   = b.vel_data()
# velmsgs
# veldf = pd.read_csv(velmsgs[0])
# plt.plot(veldf['Time'], veldf['linear.x'])

# # quickly plot velocities
# b.plot_vel(save_fig=True)

# # you can animate a timeseries data
# bagpy.animate_timeseries(veldf['Time'], veldf['linear.x'], title='Velocity Timeseries Plot')
