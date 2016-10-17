# Example using Windows Task Scheduler

import pythoncom, win32api
import time
from win32com.taskscheduler import taskscheduler

def create_daily_task(name, cmd, hour=None, minute=None):
    """creates a daily task"""
    cmd = cmd.split()
    ts = pythoncom.CoCreateInstance(taskscheduler.CLSID_CTaskScheduler,None,
                                    pythoncom.CLSCTX_INPROC_SERVER,
                                    taskscheduler.IID_ITaskScheduler)

    if '%s.job' % name not in ts.Enum():
        task = ts.NewWorkItem(name)

        task.SetApplicationName(cmd[0])
        task.SetParameters(' '.join(cmd[1:]))
        task.SetPriority(taskscheduler.REALTIME_PRIORITY_CLASS)
        task.SetFlags(taskscheduler.TASK_FLAG_RUN_ONLY_IF_LOGGED_ON)
        task.SetAccountInformation('', None)
        ts.AddWorkItem(name, task)
        run_time = time.localtime(time.time() + 300)
        tr_ind, tr = task.CreateTrigger()
        tt = tr.GetTrigger()
        tt.Flags = 0
        tt.BeginYear = int(time.strftime('%Y', run_time))
        tt.BeginMonth = int(time.strftime('%m', run_time))
        tt.BeginDay = int(time.strftime('%d', run_time))
        if minute is None:
            tt.StartMinute = int(time.strftime('%M', run_time))
        else:
            tt.StartMinute = minute
        if hour is None:
            tt.StartHour = int(time.strftime('%H', run_time))
        else:
            tt.StartHour = hour
        tt.TriggerType = int(taskscheduler.TASK_TIME_TRIGGER_DAILY)
        tr.SetTrigger(tt)
        pf = task.QueryInterface(pythoncom.IID_IPersistFile)
        pf.Save(None,1)
        task.Run()
    else:
        raise KeyError("%s already exists" % name)

    task = ts.Activate(name)
    exit_code, startup_error_code = task.GetExitCode()
    return win32api.FormatMessage(startup_error_code)
