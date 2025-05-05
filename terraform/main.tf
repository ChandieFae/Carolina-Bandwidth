Carolina-Bandwidth/
└── terraform/
    └── main.tf

    provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "carolina_bandwidth" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "CarolinaBandwidthServer"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install -y docker.io git
              git clone https://github.com/ChandieFae/Carolina-Bandwidth.git
              cd Carolina-Bandwidth
              docker-compose -f deployment/docker-compose.yml up --build -d
              EOF

  vpc_security_group_ids = [aws_security_group.cb_sg.id]
}

resource "aws_security_group" "cb_sg" {
  name        = "cb_security_group"
  description = "Allow web and SSH access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

