info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# replace * with +
info_parts = info.split(':')
new_info = "+".join(info_parts)
print(new_info)
