# entityTypes.listener.attributes.maxSessionFrames

Session incoming window measured in transfer frames for sessions created on this connection. This is the number of transfer frames that may simultaneously be in flight for all links in the session. Setting this value to zero selects the default session window size. Policy settings, if specified, will overwrite this value. The numerical product of maxFrameSize and maxSessionFrames may not exceed 2^31-1. If (maxFrameSize x maxSessionFrames) exceeds 2^31-1 then maxSessionFrames is reduced to (2^31-1 / maxFrameSize). maxSessionFrames has a minimum value of 1. Defaults to 0 (unlimited window).

