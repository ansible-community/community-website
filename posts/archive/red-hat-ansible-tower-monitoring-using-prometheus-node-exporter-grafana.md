---
author: Leonardo Araujo
date: 2020-05-06 00:00 UTC
description: A crucial piece of automation is ensuring that it runs
  flawlessly. Automation Analytics can help by providing insight into
  health state and organizational statistics.
lang: en-us
title: Red Hat Ansible Tower Monitoring Using Prometheus, Node Exporter, and Grafana
---

# Red Hat Ansible Tower Monitoring Using Prometheus, Node Exporter, and Grafana

A crucial piece of automation is ensuring that it runs flawlessly.
[Automation Analytics](https://www.ansible.com/blog/getting-started-with-automation-analytics)
can help by providing insight into health state and organizational
statistics. However, there is often the need to monitor the current
state of  Ansible Tower. Luckily, Ansible Tower does provide metrics via
the API, and they can easily be fed into Grafana.

This blog post will outline how to monitor Ansible Tower environments by
feeding Ansible Tower and operating system metrics into Grafana by using
node_exporter & Prometheus.

To reach that goal we configure Ansible Tower metrics for Prometheus to
be viewed via Grafana and we will use node_exporter to export the
operating system metrics to an operating system (OS)  dashboard in
Grafana. Note that we use Red Hat Enterprise Linux 8 as the OS running
Ansible Tower here. The data flow is outlined below:

![Leonardo Blog update
pic](https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=578&name=Leonardo%20Blog%20update%20pic.png){width="578"
style="width: 578px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=289&name=Leonardo%20Blog%20update%20pic.png 289w, https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=578&name=Leonardo%20Blog%20update%20pic.png 578w, https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=867&name=Leonardo%20Blog%20update%20pic.png 867w, https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=1156&name=Leonardo%20Blog%20update%20pic.png 1156w, https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=1445&name=Leonardo%20Blog%20update%20pic.png 1445w, https://www.ansible.com/hs-fs/hubfs/Leonardo%20Blog%20update%20pic.png?width=1734&name=Leonardo%20Blog%20update%20pic.png 1734w"
sizes="(max-width: 578px) 100vw, 578px"}

As you see, Grafana looks for data in Prometheus. Prometheus itself
collects the data in its database by importing them from node_exporters
and from the Ansible Tower APIs.

In this blog post we assume a cluster of three Ansible Tower instances
and an external database. Also please note that this blog post assumes
an already installed instance of Prometheus and Grafana.

# Setup  of node_exporter

As a first step we will set up node_exporter on the Ansible Tower
servers and the external database. Since node_exporter is not available
in Red Hat Enterprise Linux 8 by default we first have to install it. To
do that we login to our Ansible Tower server, clone the corresponding
git repository and change into the repository directory. See the listing
shown below for reference:

``` 
$ git clone https://github.com/redhat-cop/tower_grafana_dashboards 

$ cd tower_grafana_dashboards/

$ tree
.
├── install_node_exporter.yaml
├── metric_servers.json
└── metric_tower.json

0 directories, 3 files
```

Next, we have to perform the actual installation of node_exporter.
Luckily, a playbook to install it is included. Run the
install_node_exporter.yaml playbook to perform the installation of
node_exporter. 

``` 
$ ansible-playbook install_node_exporter.yaml
...
```

The output of the playbook is shown below:

![Analytics blog
2](https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=1600&name=Analytics%20blog%202.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=800&name=Analytics%20blog%202.png 800w, https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=1600&name=Analytics%20blog%202.png 1600w, https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=2400&name=Analytics%20blog%202.png 2400w, https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=3200&name=Analytics%20blog%202.png 3200w, https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=4000&name=Analytics%20blog%202.png 4000w, https://www.ansible.com/hs-fs/hubfs/Analytics%20blog%202.png?width=4800&name=Analytics%20blog%202.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

After the installation, verify if node_exporter is indeed running and
listens on port 9100. This can easily done with netstat:

![analytics blog
3](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=1600&name=analytics%20blog%203.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=800&name=analytics%20blog%203.png 800w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=1600&name=analytics%20blog%203.png 1600w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=2400&name=analytics%20blog%203.png 2400w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=3200&name=analytics%20blog%203.png 3200w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=4000&name=analytics%20blog%203.png 4000w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%203.png?width=4800&name=analytics%20blog%203.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

Repeat these steps on the other Ansible Tower servers as well as on the
external database.

# Validating Ansible Tower metrics

Next let's shift our focus towards Ansible Tower. Validate that the
Ansible Tower metrics are being displayed correctly by accessing the url
below:

``` 
https://tower.customer.com/api/v2/metrics
```

Accessing the url we should see a listing of all available Ansible Tower
metrics, as shown below:

![analytics blog
4](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=1600&name=analytics%20blog%204.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=800&name=analytics%20blog%204.png 800w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=1600&name=analytics%20blog%204.png 1600w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=2400&name=analytics%20blog%204.png 2400w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=3200&name=analytics%20blog%204.png 3200w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=4000&name=analytics%20blog%204.png 4000w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%204.png?width=4800&name=analytics%20blog%204.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

Let's  set up Prometheus to gather these data. First we need to generate
an [authentication token on Ansible
Tower](https://docs.ansible.com/ansible-tower/latest/html/administration/oauth2_token_auth.html):
the token will grant access to Ansible Tower without the need to enter
username and passwords each time it is accessed.

To generate the token, access the Ansible Tower console and click on
your username that appears at the top of the page. From there, click on
"**Tokens"** and then on the + sign. A new window pops up where you can
define the specifics of the token and finally create it, see the image
below. Choose the scope "read" and click the green "SAVE" button.

![analytics blog
5](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=512&name=analytics%20blog%205.png){width="512"
style="width: 512px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=256&name=analytics%20blog%205.png 256w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=512&name=analytics%20blog%205.png 512w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=768&name=analytics%20blog%205.png 768w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=1024&name=analytics%20blog%205.png 1024w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=1280&name=analytics%20blog%205.png 1280w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%205.png?width=1536&name=analytics%20blog%205.png 1536w"
sizes="(max-width: 512px) 100vw, 512px"}

# Setting up Prometheus to receive metrics

With the token in our hands, we can now configure Prometheus, adding the
node_exporters scrape config and the scrape for Ansible Tower\'s
metrics. Open the configuration of your Prometheus installation with an
editor of your choice: 

``` 
$ vim /etc/prometheus/prometheus.yml
```

Next, add the configuration for Ansible Tower and the operating system.
Below is an example:

``` 
## Scrape Config - Tower
  - job_name: 'tower'
    metrics_path: /api/v2/metrics
    scrape_interval: 5s
    scheme: https
    bearer_token: xxxxxxxxxxxxxxxx (your bearer token)
    static_configs:
    - targets:
      - tower.customer.com

## Add Node Exporter
  - job_name: 'tower-01'
    scrape_interval: 5s
    static_configs:
    - targets: ['172.31.66.203:9100']

  - job_name: 'tower-02'
    scrape_interval: 5s
    static_configs:
    - targets: ['172.31.65.135:9100']

  - job_name: 'tower-db-01'
    scrape_interval: 5s
    static_configs:
    - targets: ['172.31.64.218:9100']
```

Note that the metrics for Ansible Tower are only collected once, while
the operating system metrics are collected for each server: Ansible
Tower helps ensure that all internal metrics are already collected and
shared among all installed servers of the cluster. But each operating
system on each server is independent and thus has independent OS
metrics.

Restart Prometheus to apply the changes:

``` 
$ systemctl restart prometheus
```

Now, access the url http://prometheus.customer.com/targets to validate
that the data are scraped properly. Ensure that , all endpoints are in
UP status as shown below:

![analytics blog
6](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=1600&name=analytics%20blog%206.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=800&name=analytics%20blog%206.png 800w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=1600&name=analytics%20blog%206.png 1600w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=2400&name=analytics%20blog%206.png 2400w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=3200&name=analytics%20blog%206.png 3200w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=4000&name=analytics%20blog%206.png 4000w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%206.png?width=4800&name=analytics%20blog%206.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

# Grafana configuration to import the dashboards

Now let\'s import the dashboards into Grafana. Grafana can be configured
through json files. In the repo mentioned above we provide two json
files to configure two dashboards: metric_servers.json for the OS
metrics, and metric_tower.json for the Ansible Tower metrics. Let's
import them into Grafana to enable the dashboards.

To do that, access your Grafana installation and click on the + sign in
the navigation menu on the left side. Pick **"Folder"**,  enter a
desired name and create it.

Afterwards we have the option to **"Manage Dashboards"**, from where we
can import the prepared json file via upload**.** Select the json file
metric_tower.json, choose the just created folder, change the uid and
choose the datasource as Prometheus as shown below:

![analytics blog
7](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=1558&name=analytics%20blog%207.png){width="1558"
style="width: 1558px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=779&name=analytics%20blog%207.png 779w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=1558&name=analytics%20blog%207.png 1558w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=2337&name=analytics%20blog%207.png 2337w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=3116&name=analytics%20blog%207.png 3116w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=3895&name=analytics%20blog%207.png 3895w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%207.png?width=4674&name=analytics%20blog%207.png 4674w"
sizes="(max-width: 1558px) 100vw, 1558px"}

Initiate the import by pressing the corresponding button. After the
import of metric_tower.json is finished, we repeat the same process for
the metric_servers.json file.

# The new Grafana dashboards

Once both uploads are finished, we can view the imported dashboards:

![analytics blog
8](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=1600&name=analytics%20blog%208.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=800&name=analytics%20blog%208.png 800w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=1600&name=analytics%20blog%208.png 1600w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=2400&name=analytics%20blog%208.png 2400w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=3200&name=analytics%20blog%208.png 3200w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=4000&name=analytics%20blog%208.png 4000w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%208.png?width=4800&name=analytics%20blog%208.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

In this Ansible Tower metrics dashboard, you can now see the following
information:

-   Ansible Tower Version 
-   Ansible Automation Platform Version
-   number of tower nodes
-   number of hosts available in the license
-   number of hosts used
-   total users
-   jobs successful
-   jobs failed
-   quantity by type of job execution
-   graphics showing the number of jobs running and pending jobs
-   graph showing the growth of the tool showing the amount of workflow,
    hosts, inventories, jobs, projects, organizations, etc.

In the Operating System metrics dashboard, we have the following
information:

-   Uptime
-   total vcpus
-   total memory
-   cpu iowait
-   memory consumption
-   cpu busy
-   Swap
-   filesystem consumption
-   disk iops
-   system load
-   used space graph
-   graphics with disk writing and reading, network traffic and network
    sockets.

![analytics blog
9](https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=512&name=analytics%20blog%209.png){width="512"
style="width: 512px;"
srcset="https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=256&name=analytics%20blog%209.png 256w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=512&name=analytics%20blog%209.png 512w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=768&name=analytics%20blog%209.png 768w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=1024&name=analytics%20blog%209.png 1024w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=1280&name=analytics%20blog%209.png 1280w, https://www.ansible.com/hs-fs/hubfs/analytics%20blog%209.png?width=1536&name=analytics%20blog%209.png 1536w"
sizes="(max-width: 512px) 100vw, 512px"}

# Takeaways and where to go next

In this post, we demonstrate how to create a monitoring of your Ansible
Tower environment using node_exporter to export metrics from the OS and
Prometheus collecting the metrics of the Ansible Tower api, we include
the OS consumption dashboards and Ansible Tower metrics, so that you
have a view more managerial of your environment, such as capacity,
licensing and jobs in execution, using graphics and counters, you can
identify problems and take actions quickly.

If you\'re interested in detailed views across your entire automation
environment, you can also try Automation Analytics on
[cloud.redhat.com](https://cloud.redhat.com/).
