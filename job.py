from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class AutoSysJob(BotPlugin):
    """AutoSys job plugin for Errbot"""

    @botcmd
    def job_status(self, msg, args):
        """Return job status"""
        string = ""
        job_name = args
        target_server = ""
        with open('/var/errbot/target_server', 'r') as file:
            target_server = str(file.read())
        string = "Server:  \t" + target_server 
        string += "Job Name:  \t" + job_name
        string += "\nLast Start: \t" + "10/28/2017 22:35:03"
        string += "\nLast End: \t\t" + "10/28/2017 22:35:52"
        string += "\nStatus: \t\t" + "Success"
        return string
    
    # This method would attempt to loggin to the server listed in /var/errbot/target_server
    # then after logging in, source into P11 instance by executing . /export/apps/sched/autouser/autosys.bash.P11
    # finally continue trying to start start the job
    # optionally, the method could be configured to continually poll the job for X time looking for a SU status.
    @botcmd
    def job_start(self, msg, args):
        """Start requested job"""
        job_name = args
        target_server = ""
        with open('/var/errbot/target_server', 'r') as file:
            target_server = str(file.read())
        #login
        #source file
        yield "Starting " + job_name + " on " + target_server + "..."
        #poll for RU status
        time.sleep(3)
        yield job_name + " has started."
        #optionally poll for SU status
