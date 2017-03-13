# Update Guard 2
import os.path, time
import math
import pandas as pd
import xlrd

# After recieving date of creation of file, we can determine whether the file is updated or not. As file is not updated, alarm is raised or guard left location is detected.
def timer():
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/spreadsheet2.xls")
    access_time=time.time()-ctime
    print(access_time)
    time.sleep(2)
    guardactivity = xlrd.open_workbook("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardactivity2.xls")
    guardactivity = guardactivity.sheet_by_index(0)
    print("Alarm is on") = guardactivity.cell(1,1).value

    if(access_time>60):
        alarm_on()

    if(access_time<60):
        alarm_off()

    if(access_time>45):
        left_location()

    if(access_time<45):
        reached_location()

    timer()


def alarm_on():
	print("Alarm is on")
	print("Guard Activity: ", guardactivity)
	dfs = pd.read_excel('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls', sheetname=None)
	data = {'On-Time': 'Late'}
	writer = pd.ExcelWriter('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls')
	for sheetname, df in dfs.items():
	    df = df.replace(data)
	    df.to_excel(writer, sheetname, index=False)
	writer.save()

def alarm_off():
	print("Alarm is off")
	dfs = pd.read_excel('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls', sheetname=None)
	data = {'Late': 'On-Time'}
	writer = pd.ExcelWriter('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls')
	for sheetname, df in dfs.items():
	    df = df.replace(data)
	    df.to_excel(writer, sheetname, index=False)
	writer.save()

def left_location():
	print("Left Location")
	dfs = pd.read_excel('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls', sheetname=None)
	data = {'Yes': 'No'}
	writer = pd.ExcelWriter('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls')
	for sheetname, df in dfs.items():
	    df = df.replace(data)
	    df.to_excel(writer, sheetname, index=False)
	writer.save()

def reached_location():
	print("Reached Location")
	dfs = pd.read_excel('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls', sheetname=None)
	data = {'No': 'Yes'}
	writer = pd.ExcelWriter('/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls')
	for sheetname, df in dfs.items():
	    df = df.replace(data)
	    df.to_excel(writer, sheetname, index=False)
	writer.save()

timer()
