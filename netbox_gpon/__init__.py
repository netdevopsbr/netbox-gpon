# Netbox plugin related import
from extras.plugins import PluginConfig

class NetboxGponConfig(PluginConfig):
    name = "netbox_gpon"
    verbose_name = "Netbox GPON"
    description = "GPON Health - Abstraction of OLT"
    version = "0.0.1"
    author = "Emerson Felipe (@emersonfelipesp)"
    author_email = "emersonfelipe.2003@gmail.com"
    base_url = "netbox_gpon"
    required_settings = []
    default_settings = {
    }

config = NetboxGponConfig