
### 自动安装harbor仓库界面管理的脚本harbor1.5.0_setup.sh

```
#!/bin/bash

harbor1.5.0_setup () {
   yum install epel-release   -y
   yum install axel vim git curl wget lrzsz ansible gcc  python-devel yum-utils -y
   yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
   yum -y install docker-ce docker-compose
   systemctl start docker
   #wget -c http://harbor.orientsoft.cn/harbor-v1.5.0/harbor-offline-installer-v1.5.0.tgz
   #tar xf harbor-offline-installer-v1.5.0.tgz
   sed -i '/^harbor_admin_password/c\harbor_admin_password = 123456' /opt/harbor/harbor.cfg
   sed -i '/^hostname/chostname = 192.168.1.23' /opt/harbor/harbor.cfg
   bash /opt/harbor/install.sh
}

harbor1.5.0_setup
```

