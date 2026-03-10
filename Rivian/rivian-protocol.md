## (Theoretical) Current Music Auth Flow

```mermaid
sequenceDiagram
    participant Vehicle as R1T
    participant RivianServer as Rivian Server
    participant Phone as iPhone
    participant MusicService as Apple Music

    Vehicle ->> RivianServer: (Music Service) Auth Request
    RivianServer ->> RivianServer: AppServiceToken used to get QRCode
    RivianServer ->> Vehicle: QR Code Data (URL or authCode)
    Phone ->> Vehicle: User Scans QR Code
    Phone ->> MusicService: Phone authenticates with Music Service API
    MusicService ->> MusicService: Authenticates user
    MusicService ->> Phone: Returns status. If valid, returns valid Bearer+MUT
    Phone ->> RivianServer: Callback URI passes back Bearer & MUT
    RivianServer ->> Vehicle: Authenticates vehicle
```

## (Theoretical Alt.) Current Music Auth Flow

```mermaid
sequenceDiagram
    participant Vehicle as R1T
    participant RivianServer as Rivian Server
    participant Phone as iPhone
    participant MusicService as Apple Music

    Vehicle ->> RivianServer: (Music Service) Auth Request
    RivianServer ->> RivianServer: AppServiceToken used to get QRCode
    RivianServer ->> Vehicle: QR Code Data (URL or authCode)
    Vehicle ->> Phone: User Scans QR Code
    Phone ->> MusicService: Phone authenticates with Music Service API
    MusicService ->> MusicService: Authenticates user
    MusicService ->> Phone: Returns status. If valid, returns valid Bearer+MUT
    Phone ->> Vehicle: Callback URI passes back Bearer & MUT
```

Based on existing experience, the current Music Authentication Flow involves Rivian's server to maintain authentication. As part of that process, the user's access token is exposed to Rivian (and potentially other Third Parties) in order to live stream music on the vehicle potentially creating a Privacy concern if correct.

### Recommended Music Auth Flow (Apple Music cont.)

```mermaid
sequenceDiagram
    participant Vehicle as R1T
    participant MusicService as Apple Music

    alt Music Streaming
    Vehicle ->> MusicService: Play Music
    MusicService ->> Vehicle: Music Data (Artwork URL, Song URI, anything to play the music)
    alt Artwork
    Vehicle ->> MusicService: Fetches Artwork URL
    MusicService ->> Vehicle: Receives & loads Artwork image
    end
    alt Now Playing
    Vehicle ->> MusicService: Fetches Music
    MusicService ->> Vehicle: Receives Music data, and starts playing
    end
    end
```

## (Theoretical) Authenticated

```mermaid
sequenceDiagram
    participant Vehicle as R1T
    participant RivianServer as Rivian Server
    participant MusicService as Apple Music
    participant Phone as iPhone

    Vehicle ->>+RivianServer: <Play Music>
    RivianServer ->> MusicService: <Play Music>
    MusicService ->> RivianServer: <Music Data (Album, Artist, other music info)>
    RivianServer ->> Vehicle: <Music Data (Album, Artist, other music info)>
```
