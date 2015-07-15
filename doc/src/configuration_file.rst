Configuration File
==================

The configuration file named ssm.conf contains the configuration options for
System Storage Manager to function correctly. Also, the file should be placed in
user's /etc/ directory. The configuration options can be modified as needed.
However, the environment variables will take priority over configuration options
in event of conflict. Moreover, if the configuration file does not exist,
the default values will be used instead.

The path and name of configuration file can be changed using environment variable
**SSM_CONFIG_PATH** which is set as **/etc/ssm.conf** by default.

The list of current available options and their default values:

general:
	default_backend = lvm

btrfs:
	default_pool = btrfs_pool

crypt:
	default_pool = crypt_pool
	volume_name = encrypted

lvm:
	default_pool = lvm_pool
	volume_name = lvol


The configuration options are formatted as:

[<section_name_1>]
<option_name_1>=<value_1>
...
<option_name_n>=<value_n>

[<section_name_2>]
<option_name_1>=<value_1>
...
<option_name_n>=<value_n>
