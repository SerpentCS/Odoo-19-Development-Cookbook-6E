from odoo import http
from odoo.http import request
import xmlrpc.client
import logging

_logger = logging.getLogger(__name__)

class LegacyIntegrationController(http.Controller):

    @http.route('/api/legacy/create_data', type='jsonrpc', auth='public', methods=['POST'], csrf=False)
    def create_data_from_legacy(self, **kwargs):
        """
        REST API endpoint to receive hostel data from a legacy system.
        Validates the caller using Odoo username and password before creating records.
        """
        try:
            # Extract credentials from the incoming payload
            db_name = kwargs.get('db')
            username = kwargs.get('username')
            password = kwargs.get('password')
            data = kwargs.get('data', {})

            # Validate credentials via XML-RPC authentication
            server_url = request.httprequest.host_url.rstrip('/')
            common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % server_url)
            user_id = common.authenticate(db_name, username, password, {})

            if not user_id:
                _logger.warning("Unauthorized access attempt with username: %s", username)
                return {'status': 'error', 'message': 'Unauthorized: Invalid credentials'}

            _logger.info("Authenticated user_id: %s", user_id)

            # Create the hostel room record
            hostel_room = request.env['hostel.room'].with_user(user=user_id).create(data)
            _logger.info("Hostel Room %s created for Legacy System", hostel_room.name)
            return {'status': 'success', 'room_name': hostel_room.name}

        except Exception as e:
            _logger.exception("Error processing legacy data: %s", e)
            return {'status': 'error', 'message': str(e)}