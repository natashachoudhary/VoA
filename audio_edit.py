from pydub import AudioSegment
from pydub.playback import play

loop = AudioSegment.from_wav(r"C:\Personal\LnT\Speech\CoC\Backup\Backup\Sound recordings Max 13-08-2019\COMMAND_MyV_AcousticalSpeedWarning.wav")

#play(loop)

#Repeat 2 times
loop2 = loop * 2
# Get length in milliseconds
length = len(loop2)
# Set fade time
fade_time = int(length * 0.5)
# Fade in and out
faded = loop2.fade_in(fade_time).fade_out(fade_time)
play(faded)
