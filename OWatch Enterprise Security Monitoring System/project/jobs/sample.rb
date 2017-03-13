#!/usr/bin/env ruby
require 'roo-xls'

# Update every 2 seconds
SCHEDULER.every '2s' do
file_path1_1 = "#{Dir.pwd}/spreadsheet1.xls"
file_path1_2 = "#{Dir.pwd}/guardupdate1.xls"
file_path1_3 = "#{Dir.pwd}/guardactivity1.xls"
file_path2_1 = "#{Dir.pwd}/spreadsheet2.xls"
file_path2_2 = "#{Dir.pwd}/guardupdate2.xls"
file_path2_3 = "#{Dir.pwd}/guardactivity2.xls"
file_path3_1 = "#{Dir.pwd}/channelA.xls"
file_path3_2 = "#{Dir.pwd}/channelB.xls"

# Guard 1
def fetch_spreadsheet_data1_1(path1_1)
  s = Roo::Excel.new(path1_1)
  send_event('Checkpoint1',   { current: s.cell('B',2) })
  send_event('Guard1',   { current: s.cell('C',2) })
  send_event('NextCheckpoint1',   { current: s.cell('D',2) })
end

def fetch_spreadsheet_data1_2(path1_2)
  s = Roo::Excel.new(path1_2)
  send_event('GuardReached1',   { current: s.cell('A',2) })
  send_event('GuardAlarm1',   { current: s.cell('B',2) })
end

def fetch_spreadsheet_data1_3(path1_3)
  s = Roo::Excel.new(path1_3)
  send_event('GuardActivity1',   { current: s.cell('B',2) })
end

# Guard 2
def fetch_spreadsheet_data2_1(path2_1)
  s = Roo::Excel.new(path2_1)
  send_event('Checkpoint2',   { current: s.cell('B',2) })
  send_event('Guard2',   { current: s.cell('C',2) })
  send_event('NextCheckpoint2',   { current: s.cell('D',2) })
end

def fetch_spreadsheet_data2_2(path2_2)
  s = Roo::Excel.new(path2_2)
  send_event('GuardReached2',   { current: s.cell('A',2) })
  send_event('GuardAlarm2',   { current: s.cell('B',2) })
end

def fetch_spreadsheet_data2_3(path2_3)
  s = Roo::Excel.new(path2_3)
  send_event('GuardActivity2',   { current: s.cell('B',2) })
end

# Covert Channel 1
def fetch_spreadsheet_data3_1(path3_1)
  s = Roo::Excel.new(path3_1)
  send_event('channelA',   { current: s.cell('B',2) })
end

# Covert Channel 2
def fetch_spreadsheet_data3_2(path3_2)
  s = Roo::Excel.new(path3_2)
  send_event('channelB',   { current: s.cell('B',2) })
end

module Handler
  def file_modified
    fetch_spreadsheet_data1_1(path1_1)
    fetch_spreadsheet_data1_2(path1_2)
    fetch_spreadsheet_data1_3(path1_3)
    fetch_spreadsheet_data2_1(path2_1)
    fetch_spreadsheet_data2_2(path2_2)
    fetch_spreadsheet_data2_3(path2_3)
    fetch_spreadsheet_data3_1(path3_1)
    fetch_spreadsheet_data3_2(path3_2)
  end
end

module Handler
  def file_modified
    fetch_spreadsheet_data4(path2)
  end
end

fetch_spreadsheet_data1_1(file_path1_1)
fetch_spreadsheet_data1_2(file_path1_2)
fetch_spreadsheet_data1_3(file_path1_3)
fetch_spreadsheet_data2_1(file_path2_1)
fetch_spreadsheet_data2_2(file_path2_2)
fetch_spreadsheet_data2_3(file_path2_3)
fetch_spreadsheet_data3_1(file_path3_1)
fetch_spreadsheet_data3_2(file_path3_2)
end
