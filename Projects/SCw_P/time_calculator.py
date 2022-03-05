def add_time(time, addhrtime,day=None):
  #TODO: add day later
  # print(day)
  weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ]
  # am_pm = ""
  nday = None
  # spliting time
  time = time.split()
  # converting time to int
  [time_hr,time_minutes] = (time[0].split(":"))
  # print(time_hr,time_minutes)
  # original am/pm
  ori_am_pm = time[1]
  # print(ori_am_pm )

  # repeat process for addhrtime
  addhrtime = addhrtime.split()
  # converting time to int
  [addtime_hr,addtime_minutes] = (addhrtime[0].split(":"))

  # adding minutes from both time
  total_minutes = (int(time_minutes) + int(addtime_minutes))
  total_hrs = (int(time_hr) + int(addtime_hr))
  # print(total_hrs,total_minutes)
  # minutes = str(total_minutes - (int(hrs) * 60))
  if total_minutes >= 60:
    total_hrs += 1
    total_minutes = total_minutes % 60

  # if its a only one digit then add zero to left
  if len(str(total_minutes)) == 1 :
    total_minutes = str(total_minutes).zfill(2)


  if total_hrs >= 12:
  # a is how many 12 in new_hours, b is a remainder of division
    a,b =divmod(total_hrs, 12)
    total_hrs = b if b else total_hrs // a

    if a>1:
      if ori_am_pm =='PM':
        n = ((a-1)//2)+1
      else:
        n=a//2
    elif a==1:
      if ori_am_pm == 'PM':
        n =1


    if a>0 and a%2 !=0:
      ori_am_pm = 'AM' if ori_am_pm == 'PM' else 'PM'
  else:
    n == 0

  weekday = ""
  if day:
    day = day.title()
    if n > 0:
      index = weekdays.index(day)
      index += n % 7
      if n > 6:
        index = index - 7
      weekday = weekdays[index]
    else:
      index = weekdays.index(day)
      weekday = weekdays[index]

  added_time = f"{total_hrs}:{total_minutes} {ori_am_pm}, {weekday}"

  if n > 1:
    text = f" ({n} days later)"
    added_time += text
  elif n == 1:
    text = " (next day)"
    added_time += text


  return  added_time



# print(add_time("11:06 PM",   "2:02"))
# print(add_time("3:00 PM", "3:10"))
# # # # Returns: 6:10 PM

# print(add_time("11:43 AM", "00:20"))
# # # # Returns: 12:03 PM


# print(add_time("11:30 AM", "2:32", "Monday"))
# # # Returns: 2:02 PM, Monday


print(add_time("10:10 PM", "3:30"))
# # Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# # Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# # Returns: 7:42 AM (9 days later)

