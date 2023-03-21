"""
Misc. IP tools: normalize, handle mapped addresses
"""

from netaddr import IPAddress


def normalize_mapped_address(ipaddr):
    """
    Converts a IPv4-mapped IPv6 address into a IPv4 address. Handles both the
    ::ffff:192.0.2.128 format as well as the deprecated ::192.0.2.128 format.

    :param ipaddr: IP address [str]
    :return: normalized IP address [str]
    """
    ipaddr = IPAddress(ipaddr)
    if ipaddr.is_ipv4_compat() or ipaddr.is_ipv4_mapped():
        ipaddr = ipaddr.ipv4()
    return str(ipaddr)


def get_client_ip(request):
    """
    Get client IP also behind reverse proxy
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_ip_normalized(request):
    return normalize_mapped_address(get_client_ip(request))


# currently, normalize_ip does no more than normalize_mapped_address:
normalize_ip = normalize_mapped_address
