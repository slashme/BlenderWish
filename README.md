# BlenderWish
Server and client setup to allow web-based rendering of Blender animations
Basic project structure:

Server:
  Project contains:
    Name
    .blend file 
    range (list?) of frames to render
    List of frames in progress, with clients identified
    List of blacklisted clients
    Rendered frames
  Server provides:
    .blend file
    Next frame to render
    Rendered frames
  Client-server interaction:
    Client reads the latest number
    Client accepts job
        If existing client:
          If client is marked as busy with a frame:
            If repeat offender: #define threshold offense count
              blacklist
            Else:
              Increment client's offense count
              Re-send frame number that client is working on 
              Client confirms job acceptance
              Server marks frame as in progress
          Else: #client is not busy with a frame
            If frame is still available:
              Server confirms acceptance and marks frame as in progress
              If this was the published latest frame:
                Server updates and publishes new "latest frame"
            Else: #Frame is not available
              Server provides a new frame number
                Client confirms job acceptance
                Server marks frame as in progress
                If this was the published latest frame:
                  Server updates and publishes new "latest frame"
        Else: #Not existing client
          Server registers client (just by IP number at first?)
          Server confirms acceptance and marks frame as in progress
    Client accepts job


