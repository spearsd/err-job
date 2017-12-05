from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class AutoSysJob(BotPlugin):
    """AutoSys job plugin for Errbot"""

    @botcmd
    def job_status(self, msg, args):
        """Return job status"""
        string = ""
        string_multi = ""
        job_name = args
        #with tempfile.TemporaryFile() as tempf:
        #    proc = subprocess.Popen(['ls','-l'], stdout=tempf)
        #    proc.wait()
        #    tempf.seek(0)
        #    string = str(string) + str(tempf.read())
        #t = PrettyTable(['Job Name', 'Last Start', 'Last End', 'ST', 'Run/Ntry', 'Pri/Xit'])
        #t.add_row([args, '10/28/2017 22:35:03', '10/28/2017 22:35:52', 'SU', '157897088/1', '0'])
        #string = "Job Name                                                           Last Start           Last End             ST Run/Ntry Pri/Xit" + "\n____________________________________________________________________________________________ ____________________ ____________________ __ ________ _______" + "\n" + job_name + "                                         10/28/2017 22:35:03  10/28/2017 22:35:52  SU 157897088/1 0"
        string = "Job Name: \t\t" + job_name
        string += "\nLast Start: \t" + "10/28/2017 22:35:03"
        string += "\nLast End: \t\t" + "10/28/2017 22:35:52"
        string += "\nST: \t\t\t\t" + "SU"
        string += "\nRun/Ntry: \t\t" + "157897088/1"
        string += "\nPri/Xit:\t\t\t" + "0"
        return string
    
    @botcmd
    def job_start(self, msg, args):
        """Return job status"""
        string = ""
        string_multi = ""
        job_name = args
        yield "Starting " + job_name + "..."
        time.sleep(2)
        yield job_name + " has started."
