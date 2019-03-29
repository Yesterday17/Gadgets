# Proxifier

## How To Use

You can use Whitelist.ppx to visit all websites in China directly, and all the other sites via proxy.
The default proxy is `socks5://localhost:1080`. You can change it.

**NOTE: Add your proxy to direct list!!!**

## Build

You should follow the steps below:

1. Get ip-range of china [here][ip-range].
2. Make it [ip.txt][ip-txt-link]-like (Find & Replace).
3. Rename it to `ip.txt`.
4. Run `to_seg.py`, or just execute `run.bat` with `ip.txt` and `to_set.py` in the same folder.
5. Copy the content of `range.txt`to Proxifier Proxification Rules.(Note it has length limit, so you need to split the file to different rules.)

[ip-range]: http://www.ip2location.com/blockvisitorsbycountry.aspx
[ip-txt-link]: ./ip.txt

## Credits

https://www.cnblogs.com/wpjamer/p/8820174.html
