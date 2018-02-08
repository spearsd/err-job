from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class AutoSysJob(BotPlugin):
    """AutoSys job plugin for Errbot"""

    def ssh(self, msg, command):
        user_array = msg.frm.split("@")
        username = user_array[0]
        gpg_string = "$(gpg2 --batch --passphrase $ERRBOT_PASS -a -d /root/.password-store/" + username + ".gpg)"
        user_server = username + "@" + str(self.get_plugin('AutoSysServer').target_server)
        output = subprocess.check_output(["sshpass", "-p", gpg_string, "ssh", "-o", "UserKnownHostsFile=/dev/null", "-o", "StrictHostKeyChecking=no", user_server, command], shell=True)
        return output
    
    @botcmd
    def job_status(self, msg, args):
        """Return job status"""
        string = ""
        job_name = args
        target_server = self.get_plugin('AutoSysServer').target_server
        command = "AutoSysJob " + job_name
        
        if target_server == "":
            result = "Target server not set. Set the target server using !server target (servername)."
        else:
            result = ssh(msg, command)
            
        if result.find("Job Name:") == -1:
            result = "Cannot connect to targeted server with your user."
        
        #subprocess.check_output()
        return result
        
        ###################################################################
        #with open('/var/errbot/target_server', 'r') as file:
        #    target_server = str(file.read())
        #string = "Server:  \t\t" + target_server 
        #string += "\nJob Name:  \t" + job_name
        #string += "\nLast Start: \t" + "01/08/2018 22:35:03"
        #string += "\nLast End: \t\t" + "01/08/2018 22:35:52"
        #string += "\nStatus: \t\t" + "Success"
        #return string
    
    # This method would attempt to loggin to the server listed in /var/errbot/target_server
    # then after logging in, source into P11 instance by executing . /export/apps/sched/autouser/autosys.bash.P11
    # finally continue trying to start start the job
    # optionally, the method could be configured to continually poll the job for X time looking for a SU status.
    @botcmd
    def job_start(self, msg, args):
        """Start requested job"""
        job_name = args
        target_server = self.get_plugin('AutoSysServer').target_server
        #with open('/var/errbot/target_server', 'r') as file:
        #    target_server = str(file.read())
        #login
        #source file
        yield "Starting " + job_name + " on " + target_server + "..."
        #poll for RU status
        time.sleep(3)
        yield job_name + " has started."
        string = "Server:  \t\t" + target_server 
        string += "\nJob Name:  \t" + job_name
        string += "\nLast Start: \t" + "01/08/2018 21:35:03"
        string += "\nLast End: \t\t" + "01/08/2018 21:35:52"
        string += "\nStatus: \t\t" + "Running"
        yield string
        #optionally poll for SU status
