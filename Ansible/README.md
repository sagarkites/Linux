# Ansible-overview
* components of ansible
   * **Mater** 
   * **Slaves Nodes** 
   * **playbooks** 
   * **inventory** 
* **How it works** - By connecting Nodes and communicating between nodes using ssh remoteless authetentication and executing                        tasks by scripting in yaml by using modules 
* **Inventory** - A Configuration File that conatains how to communicate between the Master and Nodes
  * **Group** - Group of Hosts
  * **ungroup** - single Host
  * **vars** - used single configuration attributes to entire group
  * **children** - used to merge the groups(Groups can act as hosts)
* **Playbooks** - Scripts in yaml which plays number of Tasks
* **playbook-components**:
  * **hosts** - Defines the tasks to be performed on which node
  * **tasks** - Number of oprations which playbooks to be played 
  * **vars** - Section where all veriables are defines
  * **jinja-veriables** - A special veriable has feature of replacing something 
* **privileges** - superuser permission
    * **become** - Gives the sudo access with current login user  
    * **become_user** - Gives the sudo access to even if you not loggin as that user
    * **become_method** - Overrides the default method present in ansible.cfg
* **Modules**:
  * **pkg**
  * **file**
