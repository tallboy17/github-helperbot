Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
The `docker-compose.yaml` defines two services:  
- `GPT-SoVITS-CU126` & `GPT-SoVITS-CU128`: Full version with all features.
- `GPT-SoVITS-CU126-Lite` & `GPT-SoVITS-CU128-Lite`: Lightweight version with reduced dependencies and functionality.  
To run a specific service with Docker Compose, use:  
```bash
docker compose run --service-ports <GPT-SoVITS-CU126-Lite|GPT-SoVITS-CU128-Lite|GPT-SoVITS-CU126|GPT-SoVITS-CU128>
```