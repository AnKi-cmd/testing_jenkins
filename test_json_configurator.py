import pytest
import re
from src.configurator.json_configurator import *

json_example = "docs/Fog_json_example.json"
bad_json_example = "docs/Fog_json_error_example.json"
correct_file = JSONConfigurator(json_example)
incorrect_file = JSONConfigurator(bad_json_example)

l = ["get_cloud_provider_ip", 	"get_cloud_provider_engine_bm_login",
	 "get_cloud_provider_engine_bm_password", 	"get_cloud_provider_domain",
	 "get_cloud_provider_login", 	"get_cloud_provider_password",
	 "get_terraform_ip", 	"get_terraform_login",
	 "get_terraform_password", 	"get_terraform_vm_name",
	 "get_terraform_domain_name", 	"get_terraform_gateway",
	 "get_terraform_netmask", 	"get_terraform_dns_search",
	 "get_terraform_dns_servers", 	"get_terraform_cpu",
	 "get_terraform_ram",	 "get_terraform_os"]

answers = ["10.0.19.17",	 "YourLogin",
		   "YourPasswd!", 	"server.your.domain",
		   "YourLogin@internal", 	"Passwd",
		   "10.0.0.111", 	"root",
		   "emc", 	"terraform-vm",
		   "terraform.dev.local", 	"10.0.0.1",
		   "255.255.0.0",	"dev.local",
		   "10.0.0.1", "2",
		   "5120", "centos76"]

#tteeests
#Tests can be improved by generating responses

#PROBLEMS WITH:
#get_cloud_provider_templates


def test_get_smt():
	kol = 0
	for fun in l:
		test_correct_file = getattr(correct_file, fun)
		test_incorrect_file = getattr(incorrect_file, fun)
		assert test_correct_file() == answers[kol]
		with pytest.raises(Exception) as err:
			test_incorrect_file()
		assert not re.search("ValidationValueError", str(err))
		kol += 1

