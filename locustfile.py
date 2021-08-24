#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import json
import queue
from locust import HttpUser,TaskSet,task,between

class Ncar_Login(TaskSet):
	@task(1)
	def work_user_top(self):
		headers={"content-type":"application/json"}
		data={"data":{"channel":1,"algorithm":"BASE64","passWd":"YWJjLjEyMw==","userNm":"eXVlag=="}}
		with self.client.post("/api/v3/iw-framework/login/simpleLogin",name="login",headers=headers,data=json.dumps(data),catch_response=True) as response:
			if response.status_code==200 and response.json()['status']['status']==0:
				response.success()
			else:
				response.failure("登录 接口异常！")
				print(response.text)

class WebsiteUser(HttpUser):
	tasks = [Ncar_Login]
	host='XXXX'
	wait_time = between(1,3)
