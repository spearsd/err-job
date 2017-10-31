from errbot import BotPlugin, botcmd
import subprocess, tempfile, re

class AutoSysJob(BotPlugin):
    """AutoSys job plugin for Errbot"""

    @botcmd
    def job_status(self, msg, args):
        """Return job status"""
        string = ""
        string_multi = ""
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(['ls','-l'], stdout=tempf)
            proc.wait()
            tempf.seek(0)
            string = str(string) + str(tempf.read())
        string_array = string.split("\\n")
        for str in string_array:
            string_multi = string_multi + str
        return "```" + string_multi
        #return "```" + re.sub(r"\\", "\\\\", str(string))
        #string = "Job Name                                                         Last Start           Last End             ST Run/Ntry Pri/Xit" + "\n________________________________________________________________ ____________________ ____________________ __ ________ _______" + "\nAZ7#cmd#UIHealthCheckCMD                                         10/28/2017 22:35:03  10/28/2017 22:35:52  SU 157897088/1 0"
        #return string
