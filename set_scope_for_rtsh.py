from keysight_socket import keysight_socket

scope = keysight_socket('169.254.9.155', 5025)
print(scope.is_connected)

try:
    scope.connect()
    print(scope.is_connected)
    print(scope.set_trigger_holdoff(180e-6))

finally:
    scope.close()
    print(scope.is_connected)
