# Importing relevant Opsgenie SDK libraries including the Alert API client
import opsgenie_sdk

class Alert:
	def __init__(self):
		self.conf = self.conf = opsgenie_sdk.configuration.Configuration()
		self.conf.api_key['Authorization'] = '<YOUR_API_KEY_HERE'

		self.api_client = opsgenie_sdk.api_client.ApiClient(configuration=self.conf)
		self.alert_api = opsgenie_sdk.AlertApi(api_client=self.api_client)

	def create(self):
		body = opsgenie_sdk.CreateAlertPayload(
			message='Sample',
			alias='python_sample',
			description='Sample of SDK v2',
			responders=[{
		    	'name': 'SampleTeam',
		    	'type': 'team'
		  	}],
			visible_to=[{
				'name': 'Sample',
		   		'type': 'team'
		   	}],
			actions=['Restart', 'AnExampleAction'],
			tags=['OverwriteQuietHours'],
			details={
				'key1': 'value1',
				'key2': 'value2'},
			entity='An example entity',
			priority='P3'
		)
		try:
			create_response = self.alert_api.create_alert(create_alert_payload=body)
			print(create_response)
			return create_response
		except opsgenie_sdk.ApiException as err:
			print("Exception when calling AlertApi->create_alert: %s\n" % err)

alert = Alert()
alert.create()