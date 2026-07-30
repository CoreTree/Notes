# mDNS for AirPlay
```
mDNS Services;
	_airplay._tcp	(_airplay._tcp.local.)
	_raop._tcp	(_raop._tcp.local.)
```

# Apple TV not playing
- flags=0x10644
- gid=712F0759-5D44-41E7-FAB0AD39E165
- igl=1
- gcgl=1

# Apple TV receiving AirPlay audio
- flags=0x30e44
- gid=19F5D4B2-8A06-4792-923E-8AFA83913238
- igl=0
- gcgl=0
- pgid=19F5D4B2-8A06-4792-923E-8AFA83913238
- pgcgl=0

# Apple TV receiving AirPlay video
- flags=0x30e44
- gid=19F5D4B2-8A06-4792-923E-8AFA83913238
- igl=0
- gcgl=0
- pgid=19F5D4B2-8A06-4792-923E-8AFA83913238
- pgcgl=0

# Apple TV receiving AirPlay screen
- flags=0x30644
- gid=712F0759-5D44-41E7-AB67-FAB0AD39E165
- igl=1
- gcgl=1

# Apple TV playing local media
- flags=0x10644
- gid=FA69F5A2-5574-4E4D-A676-CA7F61A904A3
- igl=1
- gcgl=1


# _raop._tcp
### Following fields appear in the TXT record
| Name | Value | Description |
| :---: | :---: | :---: |
| txtvers | 1 | TXT record version 1 |
| ch | 2 | audio channels: stereo |
| cn | 0,1,2,3 | audio codecs |
| et | 0,3,5 | supported encryption types |
| md | 0,1,2 | supported metadata types |
| pw | false | does the speaker require a password? |
| sr | 44100 | audio sample rate: 44100 Hz |
| ss | 16 | audio sample size: 16-bit |
| tp | UDP | supported transport: TCP or UDP |
| vs | 130.14 | server version 130.14 |
| am | AppleTV2,1 | device model |

### Audio Codecs
| CN | Description |
| :--: | :--: |
| 0 | PCM |
| 1 | Apple Lossless (ALAC) |
| 2 | AAC |
| 3 | AAC ELD (Enhanced Low Delay) |

### Encryption/Authentication Types
| ET | Description |
| :--: | :--: |
| 0 | no encryption |
| 1 | RSA (AirPort Express) |
| 3 | FairPlay |
| 4 | MFiSAP (3rd-party devices) |
| 5 | FairPlay SAPv2.5 |

### Metadata Types
| MD | BIT | Description |
| --- | --- | --- |
| 0 | 17 | tex |
| 1 | 15 | artwork |
| 2 | 16 | progress |
| | 50 | bplist |

### Subtype
	Apple TV = deviceModel has prefix "AppleTV"
	HomePod = deviceModel has prefix "AudioAcessory"
	ThirdPartySpeaker = HasUnifiedAdvertiserInfo or SupportsUnifiedPairSetupAndMFi feature is set
	Unknown = otherwise

### CanBeRemoteControlled
	SupportsBufferedAudio is set, and PINRequired is not set

### State Changes
	Dependings on the state of the device the mDNS record is changed to reflect this. Primarily it is the `flags`, `gid`, `igl`, `gcgl`, `pgid` and `pgcgl` fields that are changed.


## References
- [airplay - service_discovery](https://openairplay.github.io/airplay-spec/service_discovery.html)
