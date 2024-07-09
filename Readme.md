# Chat service deployment



## Running steps

First `Docker`is required to be intsalled 

1. create necessary directories
```bash
bash create_directory.sh
```

2. Clone service 
```bash
git clone https://github.com/SaqrWare/chat-service.git
```

3. Run dockeer
```bash
docker compose up
```

Use `insomnia`  to test APIs, import collection from `Insomnia_2024-07-09.json`

#### Note

Creating cassandra cluster may take few minutes
