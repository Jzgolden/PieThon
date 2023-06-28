# Installing Emoji library

import emoji

# Print a single emoji
print(emoji.emojize(":thumbs_up:"))

# Print multiple emojis
print(emoji.emojize(":thumbs_up: :smile: :rocket:"))

# Use emojis in strings
message = "I love coding! " + emoji.emojize(":rocket:")
print(message)
