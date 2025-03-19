

import subprocess

# someFilename = subprocess.getoutput('yt-dlp --print filename https://youtu.be/CilN0KTNkoI')
# # # then pass someFilename to FFmpeg
# #
# # print(someFilename.rsplit('.')[0])
#
# # print(subprocess.getoutput('yt-dlp --print filename https://youtu.be/0JeWiuuProI'))
#
# someFileType = subprocess.getoutput('yt-dlp --print filename -o "%(ext)s" https://youtu.be/CilN0KTNkoI')
# # print(someFileType)

someFilename, someFileType = subprocess.getoutput('yt-dlp --print filename https://youtu.be/CilN0KTNkoI'), subprocess.getoutput('yt-dlp --print filename -o "%(ext)s" https://youtu.be/CilN0KTNkoI')
print(someFilename.rsplit('.'+someFileType)[0])
