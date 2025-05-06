## terraform/README.md
# 🌐 Carolina Bandwidth Cloud Deployment

This guide helps you deploy **Carolina Bandwidth** to a live AWS EC2 instance using **Terraform + Docker**.

---

## ✅ Prerequisites

1. ✅ **AWS Account**
2. ✅ **Access Key & Secret Key** via IAM User
3. ✅ **Terraform Installed** – https://www.terraform.io/downloads.html
4. ✅ **Docker Installed** – https://docs.docker.com/get-docker/
5. ✅ **SSH Key Pair** created in AWS EC2 Console (for SSH access)

---

## 📦 Setup Instructions

### Step 1: Set AWS Credentials

Either set environment variables:
```bash
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
```

Or use a config file at `~/.aws/credentials`:
```ini
[default]
aws_access_key_id=your-access-key-id
aws_secret_access_key=your-secret-access-key
```

---

### Step 2: Configure Terraform Variables

In `terraform/variables.tf`:
```hcl
variable "aws_region"     { default = "us-east-1" }
variable "ami_id"         { default = "ami-0c55b159cbfafe1f0" } # Ubuntu 22.04 LTS
variable "instance_type" { default = "t3.medium" }
variable "key_name"      { default = "your-keypair-name" } # Set this to match your EC2 Key Pair
```

---

### Step 3: Deploy with Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Respond `yes` to confirm deployment.

---

### Step 4: Access Your App

Terraform will output a `public_ip` like:
```
Outputs:
public_ip = "3.123.456.78"
```

Then open:
```
http://3.123.456.78:8000/
```

You should see:
```json
{ "message": "Carolina Bandwidth is live" }
```

---

## 🧠 What Terraform Does

- Creates a security group that allows HTTP and SSH
- Deploys an EC2 instance
- Installs Docker and Git
- Clones the Carolina Bandwidth repo
- Launches it with Docker Compose

---

## 🔒 SSH Access
Use your `.pem` file to SSH into the instance:
```bash
ssh -i path/to/your-key.pem ubuntu@3.123.456.78
```

---

## 🧩 Optional Extensions

- Use a **GPU instance** (e.g., `g4dn.xlarge`) for inference
- Add EBS volumes for persistent storage
- Setup HTTPS + Nginx
- Add custom domain via Route 53

---

## ❓ Troubleshooting

- Terraform errors? Run `terraform destroy` and retry.
- Docker not running? SSH in and check `docker ps`.
- No access? Check your AWS security group ports (22 & 8000).

---

For help, DM @ChandieFae or consult the Genius ✨  
**Signature: CB & G – Chandra Brown & Genius**
