# coding=utf-8
import argparse

from tools.get_domains_list import GetDomainsList
from tools.get_ips_list import GetIpsList
from tools.get_ports_detail import GetPortsDetail
from tools.get_ports_list import GetPortsList
from tools.get_websites_detail import GetWebsitesDetail
from tools.postgresql_sync import PostgresqlSync
from tools.websites_worker import WebsitesWorker


def options():
    parser = argparse.ArgumentParser(description='SecBlocks V0.0.2')
    parser.add_argument("-l", "--ports_list", help='get open ports of targets', action="store_true")
    parser.add_argument("-d", "--ports_detail", help='get detail of ports', action="store_true")
    parser.add_argument("-w", "--websites_detail", help='get detail of websites', action="store_true")
    parser.add_argument("-s", "--database_sync", help='synchronize remote postgresql', action="store_true")
    parser.add_argument("-ti", "--txt_ip_to_db", help='insert [ip] into sqlite',
                        action="store_true")
    parser.add_argument("-td", "--txt_domain_to_db", help='insert [domain] into sqlite',
                        action="store_true")
    parser.add_argument("-wp", "--worker_progress", help='show all progress of workers', action="store_true")

    args = parser.parse_args()

    if args.ports_list:
        # 扫描1-65535开放端口
        ports_list = GetPortsList()
        ports_list.run()
        pass
    elif args.ports_detail:
        # 扫描端口的详情
        port_detail = GetPortsDetail()
        port_detail.run()
        pass
    elif args.websites_detail:
        # 扫描网站详情
        websites_detail = GetWebsitesDetail()
        websites_detail.run()
        pass
    elif args.database_sync:
        # 数据同步，从本地postgresql，同步到远程的postgresql
        sql_sync = PostgresqlSync()
        sql_sync.run()
        pass
    elif args.txt_ip_to_db:
        txtfile_path = "targets.txt"
        ipslist = GetIpsList(txt_filename=txtfile_path)
        ipslist.run()
        pass
    elif args.txt_domain_to_db:
        txtfile_path = "targets.txt"
        domainslist = GetDomainsList(txt_filename=txtfile_path)
        domainslist.run()
        pass
    elif args.worker_progress:
        # 显示worker的进度
        worker_obj = WebsitesWorker()
        worker_obj.show_workers_progress()
        pass
    else:
        parser.print_help()
