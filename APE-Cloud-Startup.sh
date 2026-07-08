#!/bin/bash

SESSION="APE-Cloud-Startup"

# 窗口 0: FileBrowser
tmux new-session -d -s $SESSION -n "FileBrowser"
tmux send-keys -t $SESSION:0 "cd /home/sunrise/Desktop/APE-Cloud/FileBrowser/" C-m
tmux send-keys -t $SESSION:0 "go run main.go -p 3000 -a 0.0.0.0" C-m

# 窗口 1: ImageService
tmux new-window -t $SESSION -n "ImageService"
tmux send-keys -t $SESSION:1 "cd /home/sunrise/Desktop/APE-Cloud/" C-m
tmux send-keys -t $SESSION:1 "source venv/bin/activate" C-m
tmux send-keys -t $SESSION:1 "cd ImageService/" C-m
tmux send-keys -t $SESSION:1 "streamlit run service.py --server.port 4000 --server.address 0.0.0.0" C-m

# 窗口 2: LetChat
tmux new-window -t $SESSION -n "LetChat"
tmux send-keys -t $SESSION:2 "cd /home/sunrise/Desktop/APE-Cloud/LetChat/" C-m
tmux send-keys -t $SESSION:2 "pm2 start ./mongodb-linux-aarch64-ubuntu2004-4.4.29/bin/mongod --name 'mongodb-server' -- --dbpath=./mongo-data" C-m
tmux send-keys -t $SESSION:2 "pm2 start app.js --name 'lets-chat-web'" C-m

echo ###---------- APE-Cloud Startup Successfully ----------###
#tmux attach-session -t $SESSION