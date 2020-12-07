from youtube_transcript_api import YouTubeTranscriptApi
import json
import replace


srt = YouTubeTranscriptApi.get_transcript('veMFCFyOwFI')

with open('yt.txt', 'w') as file:
    # file.writelines('%s\n' % i for i in srt)
    json.dump(srt, file)

print('done')