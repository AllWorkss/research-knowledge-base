#!/bin/bash
# =============================================================================
# ZenithAlgo Pro - Google Cloud Platform (GCP) Automated Deployment Script
# =============================================================================

echo "========================================================================="
echo "       ZENITHALGO PRO - GOOGLE CLOUD PLATFORM (GCP) DEPLOYMENT           "
echo "========================================================================="
echo ""

# 1. Update System & Install Docker
echo "[1/4] Updating Linux packages & installing Docker..."
sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose git curl

# 2. Enable & Start Docker Service
echo "[2/4] Starting Docker service..."
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# 3. Build Docker Container Image
echo "[3/4] Building ZenithAlgo Pro Docker Container..."
sudo docker-compose build

# 4. Launch Container 24/7 on GCP
echo "[4/4] Launching ZenithAlgo Terminal Container in Background..."
sudo docker-compose up -d

echo ""
echo "========================================================================="
echo " [SUCCESS] ZENITHALGO PRO DEPLOYED ON GOOGLE CLOUD (GCP) SUCCESSFULLY!"
echo " Access your cloud trading terminal at: http://YOUR_GCP_VM_EXTERNAL_IP:8000"
echo "========================================================================="
