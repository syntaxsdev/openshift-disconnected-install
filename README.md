# OpenShift Disconnected Install
## WORK IN PROGRESS!
### Ansible Disconnected OpenShift Installation

Currently only supports Semi-Disconnected (RH Registry to local Quay - despite the name)

This Ansible automation aims to completely streamline the process of installing OpenShift Disconnected on a hypervisor or baremetal setup.

Right now, only Proxmox is supported.

The automation will install the VM for you into Proxmox and connect to it via SSH to finish the Mirror Registry installation. If you already have a dedicated VM you will use for the Registry, you can also skip that part.


#### Supported Fully Autonomous Installs Environments/Hypervisor
- Proxmox
- Baremetal (WIP - in future)

## Before running
Modify the [`ansible/inventory/group_vars/all.yaml`](ansible/inventory/group_vars/all.yaml) file to include specific variables for your need.

1. Ensure you have a DNS solution, or else the full automation will fail.
    This tool also supports adding a DNS host using OpnSense to keep the full automation going.
    
    If you chose not to streamline using the singular [full automation playbook](ansible/playbooks/full_install.yaml), run the playbook in parts - starting with the VM creation first [1_install_mirror_vm.yaml](ansible/playbooks/1_install_mirror_vm.yaml) and manually add your DNS record and then continue running the next playbook [2_create_registy.yaml](ansible/playbooks/2_create_registry.yaml).

### Run the full installation
```sh
cd ansible
ansible-playbook playbooks/full_install.yaml -i inventory/hosts.yaml
```