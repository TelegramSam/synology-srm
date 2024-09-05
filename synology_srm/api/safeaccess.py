# -*- coding: utf-8 -*-

from synology_srm.api import Api
import json
import time


class ApiSafeAccess(Api):
    """API SafeAccess.

    Handles the SYNO.SafeAccess API namespace.
    """

    def get_status(self):
        """Gets the status of all safe access config groups."""
        response = self.http.call(
            endpoint='entry.cgi',
            api='SYNO.SafeAccess.AccessControl.ConfigGroup',
            params={
                "additional": json.dumps(["total_timespent","reward"])
            },
            method='get',
            version=1,
        )
        return response['config_groups']



    def pause(self, config_group_id):
        """Pauses the devices of a safeaccess group."""
        response = self.http.call(
            endpoint='entry.cgi',
            api='SYNO.SafeAccess.AccessControl.ConfigGroup',
            params={
                "config_group_id": config_group_id,
                "pause": json.dumps(True)
            },
            method='set',
            version=1,
        )

        return response['success']
    
    def resume(self, config_group_id):
        """Unpauses the devices of a safeaccess group."""
        response = self.http.call(
            endpoint='entry.cgi',
            api='SYNO.SafeAccess.AccessControl.ConfigGroup',
            params={
                "config_group_id": config_group_id,
                "pause": json.dumps(False)
            },
            method='set',
            version=1,
        )

        return response['success']
    
    def reward(self, config_group_id, minutes):
        reward_start = int(time.time())
        reward_end = reward_start + minutes*60
        response = self.http.call(
            endpoint='entry.cgi',
            api='SYNO.SafeAccess.AccessControl.ConfigGroup.Reward.Ultra',
            params={
                "config_group_id": config_group_id,
                "ultra_rewards": json.dumps([{"available":reward_start,"expired":reward_end}])
            },
            method='set',
            version=1,
        )
        return response['success']

    def reward_cancel(self, config_group_id):
        response = self.http.call(
            endpoint='entry.cgi',
            api='SYNO.SafeAccess.AccessControl.ConfigGroup.Reward.Ultra',
            params={
                "config_group_id": config_group_id,
                "ultra_rewards": json.dumps([])
            },
            method='set',
            version=1,
        )
        return response['success']