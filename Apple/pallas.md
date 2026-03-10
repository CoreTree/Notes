# Pallas
Pallas is a authoritative server component to mobileassetd that runs on all internet-connected Apple devices. (Note that mobileassetd does not run things like the AirTag or other accessories, but could potentially run on a device like the Studio Display based on WatchOS functionality for updating assets.)

## Asset Types
Also known as Asset Specifiers (RE: Xcode's Bundle Indentifiers), this explicitly defines separate assets that can be updated via the mobileasset/pallas request pattern. Pallas is authoritative, and mobileasset is beholden to whatever Pallas returns.

It's worth noting that I have not tried to overwrite any responses returned by Pallas and I would not expect anything to be guaranteed here (but SUs have a process that prevents spoofing the response, not sure about other processes or daemons on the device).

### UnifiedAssetFramework (UAF)
One of the more common asset types is the [Unified Asset Framework (UAF)](https://theapplewiki.com/wiki/UnifiedAssetFramework). Per the AppleWiki, "Not much is known about UnifiedAssetFramework other than its abbreviation 'UAF' and that it relates to Siri and Apple Intelligence models or features."

## Servers
Easiest TLDR ever;
- (current) https://gdmf.apple.com/v2/assets
- (old) https://mesu.apple.com

### MESU
Mesu was an original asset server that hosted XML files before REST requests were possible. With a few changes and some APIs that became more common, instead of needing a bigger CDN to handle requests, servers that could dynamically update and manage content via APIs took over. Something something, I'm rambling, so don't mind me.

Example (source: [applewiki](https://theapplewiki.com/wiki/MobileAsset#Mesu)): [`https://mesu.apple.com/assets/macos/com_apple_MobileAsset_TimeZoneUpdates/com_apple_MobileAsset_TimeZoneUpdate.xml`](https://mesu.apple.com/assets/macos/com_apple_MobileAsset_TimeZoneUpdates/com_apple_MobileAsset_TimeZoneUpdate.xml)

## GDMF (Pallas)
Pallas is the updated server with two different clients that manage access to this server. Trial (publishing) and mobileasset (client). Here's an example request to Pallas;

```python
import base64
import requests
import json

data = {
    "AssetAudience": "02d8e57e-dd1c-4090-aa50-b4ed2aef0062", #This is no longer valid for macOS 26.0+
    "ClientVersion": 2,
    "AssetType": "com.apple.siri.understanding",
    "CertIssuanceDay": "2023-12-10", #This has since been updated to some time in 2024-12 or something
    "TrainName": "Crystal" #This isn't a current version, it's macOS 15.0
}
headers = {
    "Content-Type": "application/json",
    "Host": "gdmf.apple.com",
    "Content-Length": str(len(json.dumps(data)))
}
url = "https://gdmf.apple.com/v2/assets"
req = requests.post(url, headers=headers, json=data, verify=False)
if req.status_code == 200:
    message = req.text.split('.')[1] + '=='
    print(base64.b64decode(message))
else:
    print(req.text)
```

## Some Links/References
- I have a personal exploratory repo. If available, it would be at [pallas.py](https://github.com/riigess/pallas.py) otherwise, this doc serves as a reference for that information
- [The Apple Wiki page on MobileAsset](https://theapplewiki.com/wiki/MobileAsset)