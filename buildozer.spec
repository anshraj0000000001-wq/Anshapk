[app]

# App details
title = ANSH Studio Pro
package.name = anshuploader
package.domain = org.anshtech
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
orientation = portrait
fullscreen = 1

# Python & dependencies
requirements = python3,kivy,requests,plyer

# Permissions (important for storage + internet)
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android SDK/NDK versions
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Other buildozer options
log_level = 2
