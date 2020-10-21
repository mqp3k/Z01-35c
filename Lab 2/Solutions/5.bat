@ECHO OFF
ffmpeg\bin\ffmpeg.exe -i %1 -vf "select=gte(n\,1)" -vframes 1 thumbnail.png