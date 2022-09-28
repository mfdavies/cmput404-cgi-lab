#!/usr/bin/env python3

import os
import json

# Create an empty dictionary
env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value
    #print('{} -> {}'.format(env_key,env_value))

print("Content-Type:application/json")
print()

print(json.dumps(env))