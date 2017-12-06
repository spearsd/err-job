from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class AutoSysJob(BotPlugin):
    """AutoSys job plugin for Errbot"""

    @botcmd
    def job_status(self, msg, args):
        """Return job status"""
        string = ""
        job_name = args
        string = "Job Name:  \t" + job_name
        string += "\nLast Start: \t" + "10/28/2017 22:35:03"
        string += "\nLast End: \t\t" + "10/28/2017 22:35:52"
        string += "\nST: \t\t\t\t" + "SU"
        string += "\nRun/Ntry: \t\t" + "157897088/1"
        string += "\nPri/Xit:\t\t\t" + "0"
        return string
    
    @botcmd
    def job_start(self, msg, args):
        """Start requested job"""
        job_name = args
        yield "Starting " + job_name + "..."
        time.sleep(3)
        yield job_name + " has started."

    
# Used to run commands in terminal and capture the result in string var.
#with tempfile.TemporaryFile() as tempf:
#    proc = subprocess.Popen(['ls','-l'], stdout=tempf)
#    proc.wait()
#    tempf.seek(0)
#    string = str(string) + str(tempf.read())
