# The telegram bot token
token: str = "8725013278:AAH-3lNqf6Oy2i8XveRxv0BnU4nOjcb3-5c"

# A list of user ids that are allowed to use the bot, if None everyone is allowed
whitelist: list[int] | None = None

# A list of user ids that are not allowed to use the bot, if None everyone is allowed
blacklist: list[int] | None = None

# The logs channel id, if none set to None
logs: int | None = None

# The maximum file size in bytes
max_filesize: int = 50000000

# The maximum cookie file size in bytes (default 1MB)
max_cookie_filesize: int = 1000000

# Maximum number of concurrent downloads allowed per user
max_user_concurrent_downloads: int = 1

# Maximum number of concurrent downloads allowed globally
max_global_concurrent_downloads: int = 2

# How many times to retry a download on transient errors
max_retries: int = 3

# Seconds to wait between retry attempts
retry_delay: int = 5

# The output folder for downloaded files
output_folder: str = "/tmp/satoru"

# The allowed domains for downloading videos
allowed_domains: list[str] = [
    "youtube.com",
    "www.youtube.com",
    "youtu.be",
    "m.youtube.com",
    "youtube-nocookie.com",
    "tiktok.com",
    "www.tiktok.com",
    "vm.tiktok.com",
    "vt.tiktok.com",
    "instagram.com",
    "www.instagram.com",
    "twitter.com",
    "www.twitter.com",
    "x.com",
    "www.x.com",
    "bsky.app",
    "www.bsky.app",
]

# The allowed domains for downloading images via gallery-dl
# None means all domains are allowed
allowed_image_domains: list[str] | None = None

# Secret key used to encrypt/decrypt stored cookies
secret_key: str = "CHANGE_THIS_TO_A_RANDOM_SECRET_KEY"

# Used to solve YouTube challenges
# Keep this as the repository's default if Bun is available.
js_runtime: dict[str, dict[str, str] | None] | None = {
    "bun": {"path": "bun"}
}

# Channel to forward videos to when using /forward
# None disables forwarding
forward_to: int | None = None

# User IDs allowed to forward videos
forward_permissions: list[int] = []
