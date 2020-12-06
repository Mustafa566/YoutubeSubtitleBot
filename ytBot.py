from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript('lICIfpoD-jI')

with open('yt.txt', 'w') as file:
    file.writelines('%s\n' % i for i in srt)

print('done')