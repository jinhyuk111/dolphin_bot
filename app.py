import requests
import json
import fingerprint
import random

randomnum = random.randint(0, 100)
replaceData = list(fingerprint.data.keys())

url = "https://anty-api.com/browser_profiles/"
data = {
    "name": f"Loke - Tinder Test #{randomnum}",
    "tags": ["Loke", "Tinder"],
    "platform": "windows",
    "browserType": "anty",
    "mainWebsite": "google",
    "useragent": {
        "mode": "manual",
        "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    },
    "webrtc": {"mode": "altered", "ipAddress": None},
    "canvas": {"mode": "real"},
    "webgl": {"mode": "real"},
    "webglInfo": {
        "mode": "manual",
        "vendor": "NVIDIA Corporation",
        "renderer": "NVIDIA GeForce GT 750M OpenGL Engine",
        "webgl2Maximum": '{"MAX_SAMPLES": 8, "MAX_DRAW_BUFFERS": 8, "MAX_TEXTURE_SIZE": 16384, "MAX_ELEMENT_INDEX": 4294967295, "MAX_VIEWPORT_DIMS": [16384, 16384], "MAX_VERTEX_ATTRIBS": 16, "MAX_3D_TEXTURE_SIZE": 2048, "MAX_VARYING_VECTORS": 31, "MAX_ELEMENTS_INDICES": 150000, "MAX_TEXTURE_LOD_BIAS": 15, "MAX_COLOR_ATTACHMENTS": 8, "MAX_ELEMENTS_VERTICES": 1048575, "MAX_RENDERBUFFER_SIZE": 16384, "MAX_UNIFORM_BLOCK_SIZE": 65536, "MAX_VARYING_COMPONENTS": 124, "MAX_TEXTURE_IMAGE_UNITS": 16, "MAX_ARRAY_TEXTURE_LAYERS": 2048, "MAX_PROGRAM_TEXEL_OFFSET": 7, "MIN_PROGRAM_TEXEL_OFFSET": -8, "MAX_CUBE_MAP_TEXTURE_SIZE": 16384, "MAX_VERTEX_UNIFORM_BLOCKS": 14, "MAX_VERTEX_UNIFORM_VECTORS": 1024, "MAX_COMBINED_UNIFORM_BLOCKS": 70, "MAX_FRAGMENT_UNIFORM_BLOCKS": 14, "MAX_UNIFORM_BUFFER_BINDINGS": 70, "MAX_FRAGMENT_UNIFORM_VECTORS": 1024, "MAX_VERTEX_OUTPUT_COMPONENTS": 128, "MAX_FRAGMENT_INPUT_COMPONENTS": 128, "MAX_VERTEX_UNIFORM_COMPONENTS": 4096, "MAX_VERTEX_TEXTURE_IMAGE_UNITS": 16, "MAX_FRAGMENT_UNIFORM_COMPONENTS": 4096, "UNIFORM_BUFFER_OFFSET_ALIGNMENT": 256, "MAX_COMBINED_TEXTURE_IMAGE_UNITS": 80, "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS": 233472, "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS": 4, "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS": 233472, "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS": 4, "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS": 64}',
    },
    "clientRect": {"mode": "real"},
    "notes": {"content": None, "color": "blue", "style": "text", "icon": "info"},
    "timezone": {"mode": "auto", "value": None},
    "locale": {"mode": "auto", "value": None},
    "proxy": {
        "name": "test proxy",
        "host": "145.239.27.73",
        "port": "13991",
        "type": "socks5",
        "login": "root",
        "password": "321",
    },
    "statusId": 0,
    "geolocation": {
        "mode": "auto",
        "latitude": None,
        "longitude": None,
        "accuracy": None,
    },
    "cpu": {"mode": "manual", "value": 4},
    "memory": {"mode": "manual", "value": 8},
    "screen": {"mode": "real", "resolution": None},
    "audio": {"mode": "real"},
    "mediaDevices": {
        "mode": "real",
        "audioInputs": None,
        "videoInputs": None,
        "audioOutputs": None,
    },
    "ports": {"mode": "protect", "blacklist": "3389,5900,5800,7070,6568,5938"},
    "doNotTrack": False,
    "args": [],
    "platformVersion": "10.15.7",
    "uaFullVersion": "110.0.5304.87",
    "login": "",
    "password": "",
    "appCodeName": "Mozilla",
    "platformName": "MacIntel",
    "connectionDownlink": 10,
    "connectionEffectiveType": "4g",
    "connectionRtt": 100,
    "connectionSaveData": 0,
    "cpuArchitecture": "",
    "osVersion": "10.15.7",
    "vendorSub": "",
    "productSub": "20030107",
    "vendor": "Google Inc.",
    "product": "Gecko",
}

# replace
for i in range(len(replaceData)):
    if replaceData[i] in data:
        data[replaceData[i]] = fingerprint.data[replaceData[i]]
    else:
        print(replaceData[i])
print(data)
# json
payload = json.dumps(data)


# headers = {
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjM0MTMzNCwidXNlcm5hbWUiOiJhbGFnZW5jeXNlcnZpY2VAZ21haWwuY29tIiwicm9sZSI6ImFkbWluIiwidGVhbUlkIjoyMjgzMzk2LCJ0b2tlbkNyZWF0ZWRBdCI6MTY4Mjc4MzAwNH0.YCVpsd_jt0uD5b7sHFadFSVhDomLa4gXjPb0jg-wi04",
#     "Content-Type": "application/json",
# }


# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.status_code)

# print(response.text)
