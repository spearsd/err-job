from errbot import BotPlugin, botcmd
import subprocess

class AutoSysJob(BotPlugin):
    """AutoSys job plugin for Errbot"""

    @botcmd
    def job_status(self, msg, args):
        """Return job status"""
        string = subprocess.check_output(['ls','-l'])
        return "``````````````````````````````````````````````````" + str(string) + "``````````````````````````````````````````````````"
        #string = "Job Name                                                         Last Start           Last End             ST Run/Ntry Pri/Xit" + "\n________________________________________________________________ ____________________ ____________________ __ ________ _______" + "\nAZ7#cmd#UIHealthCheckCMD                                         10/28/2017 22:35:03  10/28/2017 22:35:52  SU 157897088/1 0"
        #return string
