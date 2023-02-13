from nptdms import TdmsFile




# Example of accessing a specific group and a specific channel within the group
with TdmsFile.open("data/Rad Test_TPS7H4010-SEP(Run-22)21_01_10.tdms") as tdms_file:
    group_name_list = tdms_file.groups()
    group_test = tdms_file['Beam1_SCOPE3-5172_2']

            
    # You can't go outside the with statement, else you won't be able to access the channels of each group
    # data[group_name][channel][:range:range+n]
    
print(group_name_list[7]) # group_test
channel = group_test
for value in channel:
    print(value)
    



channel_sum = 0.0
channel_length = 0
with TdmsFile.open('./data/Rad Test_TPS7H4010-SEP(Run-22)21_01_10.tdms') as tdms_file:
    for chunk in tdms_file.data_chunks():
        channel_chunk = chunk['Beam1_SCOPE3-5172_2'][.]
        channel_length += len(channel_chunk)
        channel_sum += channel_chunk[:].sum()
channel_mean = channel_sum / channel_length

