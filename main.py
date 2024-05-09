from DbConnect import open_conn, execute_query

db = open_conn()
result = execute_query(db)

upcoming_minute = 34  # the next upcoming minute
for row in result:
    contact_no = row['contact_no']
    message = "Hello I'm sending message to " + row['name']
    current_hour = 11
    wait_time = 10 # time to wait before sending the message (minute)
    close_tab = True # close the browser tab
    close_time = 3 # time to close the tab (minute)

    pywhatkit.sendwhatmsg(contact_no, message, current_hour,
                          upcoming_minute, wait_time, close_tab, close_time)

    upcoming_minute += 1