This is a practical for demostrating working of selinux in enforcing and permissive modes. 

1. With SELinux enabled, open index.py and try creating a directory, it would give an alert. If creating a directory other then /var/tmp or /tmp, give without password sudo access to apache user for mkdir command.

2. IT would give an error, saying about selinux and you will get an alert for the same.

3. Lower the restrictions by changing selinux mode to permissive and try again, this time the directory will be created.

It gave an error because despite of using sudo with no password, apache was not able to write to the directory because selinux prevented that from doing so, based on the context of that directory in which we were trying to create the new directory. 
