from datetime import datetime
import time
import logging
from ocpp.routing import on
from ocpp.v16 import call, call_result
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import Action, RegistrationStatus

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ChargePoint(cp):
    heartbeat_interval = 60
    async def send_authorize(self, id_tag):
        request = call.AuthorizePayload(
            id_tag = id_tag
        )

        response = await self.call(request)
        if response.id_tag_info['status'] == RegistrationStatus.accepted:
            print("===================================")
            print("Auth.req is accepted.")
            print("===================================")

    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
            charge_point_model="CP100",
            charge_point_vendor="GRE System"
        )

        response = await self.call(request)
        if response.status == RegistrationStatus.accepted:
            self.heartbeat_interval = response.interval
            print("===================================")
            print("Connected to central system.")
            print("===================================")

    # async def send_data_transfer(self, vendor_id: str, message_id: str, **kwargs):   
    async def send_data_transfer(self, vendor_id: str, message_id: str, data, **kwargs):   
        request = call.DataTransferPayload(
            vendor_id=vendor_id,
            message_id=message_id,
            data=data
        )

        print('Request for data transfer = ', request)
        response = await self.call(request)

        print('Response = ', response)
        if response.status == "Accepted":
            print("===================================")
            print("Data Transfer to central system: Accepted")
            print(response)
            print("===================================")

    async def send_diagnostics_status_notification(self, status: str):
        request = call.DiagnosticsStatusNotificationPayload(
            status = status
        )

        response = await self.call(request)
        # if response.status == "Accepted":
        print("===================================")
        print("Diagnostics Status Notification to central system")
        print("===================================")

    async def send_firmware_status_notification(self, status):
        request = call.FirmwareStatusNotificationPayload(
            status = status
        )

        response = await self.call(request)
        # if response.status == "Accepted":
        print("===================================")
        print("Firmware Status Notification to central system")
        print("===================================")

    async def send_heartbeat(self):
        request = call.HeartbeatPayload()

        response = await self.call(request)
        print("===================================")
        print("Heartbeat transferred.....")
        print("===================================")

    async def send_meter_value(self):
        cur_time = datetime.now().isoformat()
        request = call.MeterValuesPayload(
            connector_id=1,
            transaction_id=2,
            meter_value=[
                {"timestamp":cur_time,"sampledValue":[{"value":"20","context":"Sample.Periodic","format":"Raw","unit":"Wh"}]},
                {"timestamp":cur_time,"sampledValue":[{"value":"20","context":"Sample.Periodic","format":"Raw","unit":"Wh"}]},
                {"timestamp":cur_time,"sampledValue":[{"value":"30","context":"Sample.Periodic","format":"Raw","unit":"Wh"}]},
                {"timestamp":cur_time,"sampledValue":[{"value":"30","context":"Sample.Periodic","format":"Raw","unit":"Wh"}]}
            ]
        )

        response = await self.call(request)
        print("===================================")
        print("MeterValue transferred.....")
        print("===================================")

    async def send_start_transaction(self, id_tag):
        request = call.StartTransactionPayload(
            connector_id=1,
            id_tag=id_tag,
            meter_start=594157,
            timestamp=datetime.now().isoformat()
            # timestamp='2022-08-06T03:44:55.024Z'
        )

        response = await self.call(request)
        if response.id_tag_info['status'] == RegistrationStatus.accepted:
            print("===================================")
            print("StartTransaction started.")
            print("===================================")

    async def send_stop_transaction(self, reason):
        # request = call.StopTransactionPayload(
        #     id_tag='0000000000150049',
        #     meter_stop=597830,
        #     timestamp='2022-10-26T17:31:50.004Z',
        #     # timestamp=datetime.now().isoformat(),
        #     transaction_id=1,
        # )

        request = call.StopTransactionPayload(
            id_tag = '0000000000150049', 
            meter_stop = 597830, 
            reason = reason, 
            timestamp = datetime.now().isoformat(), 
            transaction_id = 1, 
            transaction_data = [
                {
                    'timestamp' : '2022-10-26T17:31:49.000Z', 
                    'sampledValue' : [
                        {
                            'value' : '3673.80', 
                            'context' : 'Sample.Periodic', 
                            'format' : 'Raw', 
                            'measurand' : 'Energy.Active.Import.Register', 
                            'unit' : 'Wh'
                        },
                        {
                            'value' : '72.44', 
                            'context' : 'Sample.Periodic', 
                            'format' : 'Raw', 
                            'measurand' : 'Temperature', 
                            'unit' : 'Celcius'
                        }
                    ]
                }
            ]
        )


        response = await self.call(request)
        if response.id_tag_info['status'] == RegistrationStatus.accepted:
            print("===================================")
            print("StopTransaction started.")
            print("===================================")

    async def send_status_notification(self, cpstatus):
        request = call.StatusNotificationPayload(
            connector_id=1,
            error_code='NoError',
            status=cpstatus
        )

        response = await self.call(request)
        print("===================================")
        print("StatusNotification transferred.....")
        print("===================================")


    @on(Action.CancelReservation)
    def on_cancel_reservation(self, reservation_id: int, **kwargs):
        logging.info('========== Got a Boot Notification ==========')
        return call_result.CancelReservationPayload(
            status = 'Accepted'      # CancelReservationStatus: Accepted / Rejected
        )

    @on(Action.ChangeAvailability)
    def on_change_availability(self, connector_id: int, type: str, **kwargs):
        logging.info('========== Got a Change Availability ==========')
        return call_result.ChangeAvailabilityPayload(
            status = 'Accepted'
        )

    @on(Action.ChangeConfiguration)
    def on_change_configuration(self, key, value, **kwargs):
        logging.info('========== Got a Change Configuration ==========')
        if key == 'HeartbeatInterval':
            self.heartbeat_interval = int(value)
            ConfigurationStatus = 'Accepted'
        else:
            ConfigurationStatus = 'NotSupported'
        return call_result.ChangeConfigurationPayload(
            status = ConfigurationStatus
        )

    @on(Action.ClearCache)
    def on_clear_cache(self, **kwargs):
        logging.info('========== Got a Clear Cache ==========')
        return call_result.ClearCachePayload(
            status = 'Accepted' # or Rejected
        )

    @on(Action.ClearChargingProfile)
    def on_clear_charging_profile(self, connector_id: int, id: int, **kwargs):
        logging.info('========== Got a Clear Charging Profile ==========')
        if id == 100:
            clearchargingprofilestatus = 'Unknown'
        else:
            clearchargingprofilestatus = 'Accepted'
        return call_result.ClearChargingProfilePayload(
            status = clearchargingprofilestatus
        )

    @on(Action.GetCompositeSchedule)
    def on_get_composite_schedule(self, connector_id: int, duration: int, **kwargs):
        logging.info('========== Got a Get Composite Schedule ==========')
        if duration == 300:
            getcompositeschedulestatus = 'Accepted'
        else:
            getcompositeschedulestatus = 'Rejected'

        return call_result.GetCompositeSchedulePayload(
            status = getcompositeschedulestatus
            # options: connector_id: int, schedule_start: str, charging_schedule: Dict
        )

    @on(Action.GetConfiguration)
    def on_get_configuration(self, key, **kwargs):
        logging.info('========== Got a Get Configuration ==========')
        if key[0] == 'HeartbeatInterval':
            configuration_key = [{'key': 'HeartbeatInterval', 'readonly': False, 'value': str(self.heartbeat_interval)}]
        else:
            configuration_key = [{'key': 'HeartbeatInterval', 'readonly': False, 'value': '500'}]

        return call_result.GetConfigurationPayload(
            configuration_key = configuration_key
        )
    # 'configurationKey': [{'key': 'HeartbeatInterval', 'readonly': False, 'value': '120'}, {'key': 'AuthorizeRemoteTxRequests', 'readonly': False, 'value': 'true'}]

    @on(Action.GetDiagnostics)
    def on_get_diagnostics(self, location: str, **kwargs):
        logging.info('========== Got a Get Diagnostics ==========')
        return call_result.GetDiagnosticsPayload(
            file_name = 'diagnostics_' + datetime.now().strftime('%Y%m%d%H%M%S'),
        )

    @on(Action.RemoteStartTransaction)
    def on_remote_start_transaction(self, id_tag: str, **kwargs):
        logging.info('========== Got a Remote Start Transaction ==========')
        logging.info(kwargs)
        remotestartstatus = 'Accepted'
        return call_result.RemoteStartTransactionPayload(
            status = remotestartstatus
        )

    @on(Action.RemoteStopTransaction)
    def on_remote_stop_transaction(self, transaction_id: int, **kwargs):
        logging.info('========== Got a Remote Stop Transaction ==========')
        return call_result.RemoteStopTransactionPayload(
            status = 'Accepted'
        )

    @on(Action.ReserveNow)
    def on_reserve_now(self, connector_id, expiry_date, id_tag, reservation_id, **kwargs):
        logging.info('========== Got a Reserve Now ==========')
        return call_result.ReserveNowPayload(
            status = 'Accepted'
        )

    @on(Action.Reset)
    def on_reset(self, type):
        logging.info('========== Got a Reset ==========')
        if type == 'Soft':
            reset_status = 'Soft Accepted'
        elif type == 'Hard':
            reset_status = 'Hard Accepted'
        print('Reset Type: ', reset_status)
        return call_result.ResetPayload(
            status = 'Accepted',
        )

    @on(Action.GetLocalListVersion)
    def on_get_local_list_version(self, **kwargs):
        logging.info('========== Got a Get Local List Version ==========')
        return call_result.GetLocalListVersionPayload(
            list_version = -1
        )

    # Update type: Differential / Full
    # list_version, update_type, eval(local_authorization_list)
    @on(Action.SendLocalList)
    def on_send_local_list(self, list_version: int, update_type: str, local_authorization_list, **kwargs):
        logging.info('========== Got a Send Local List ==========')
        return call_result.SendLocalListPayload(
            status = 'Accepted'         # Accepted / Failed /NotSupported / VersionMismatch
        )

    @on(Action.SetChargingProfile)
    def on_set_charging_profile(self, connector_id: int, cs_charging_profiles: str, **kwargs):
        logging.info('========== Got a Set Charging Profile ==========')
        if cs_charging_profiles['charging_profile_purpose'] == 'TxDefaultProfile' or cs_charging_profiles['charging_profile_purpose'] == 'TxProfile':
            status = 'Accepted'
        else:
            status = 'Rejected'
        logging.info('================================================')
        print(kwargs)
        return call_result.SetChargingProfilePayload(
            status = status
        )

    @on(Action.TriggerMessage)
    def on_trigger_message(self, requested_message: str, **kwargs):
        logging.info('========== Got a Trigger Message ==========')
        return call_result.TriggerMessagePayload(
            status = 'Accepted'         # TriggerMessageStatus: Accepted, Rejected, NotImplemented
        )

    @on(Action.UnlockConnector)
    def on_unlock_connector(self, connector_id: int, **kwargs):
        logging.info('========== Got a Unlock Connector ==========')
        return call_result.UnlockConnectorPayload(
            status = 'Unlocked'
        )

    @on(Action.UpdateFirmware)
    def on_update_firmware(self, location: str, retrieve_date: str, **kwargs):
        logging.info('========== Got a Update Firmware ==========')
        return call_result.UpdateFirmwarePayload(
            # pass
        )

    @on(Action.DataTransfer)
    def on_Data_Transfer(self, vendor_id: str, message_id: str, **kwargs):
        logging.info('========== Got a Data Transfer ==========')
        if vendor_id == 'gresystem':
            datatransferstatus = 'Accepted'
        else:
            datatransferstatus = 'Rejected'
        data = eval(kwargs['data'])
        return call_result.DataTransferPayload(
            status=datatransferstatus,
            data=str(data)
        )




